from kodi_six import xbmc, xbmcaddon, xbmcplugin, xbmcgui, xbmcvfs
from six.moves.urllib.parse import parse_qs, quote_plus, urlparse, parse_qsl
from six import PY2
dialog = xbmcgui.Dialog()
translatePath = xbmc.translatePath if PY2 else xbmcvfs.translatePath
import sys,urllib,os,base64,re,shutil
import kodi
import client
import dom_parser2
import cache
import log_utils
import pyxbmct
# from xbmcvfs import translatePath


def deleteThumbnails():
    thumbnailPath = translatePath('special://thumbnails');
    databasePath = translatePath('special://database')
    msg="Deleted the following Thumnail"
    if os.path.exists(thumbnailPath)==True:
        for root, dirs, files in os.walk(thumbnailPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                for f in files:
                    try:
                        msg="\n%s"%os.path.join(root, f)
                        os.unlink(os.path.join(root, f))
                    except:
                        xbmcgui.Dialog().ok("Error", "Unable to remove %s"%os.path.join(root, f))
                    pass

    # xbmcgui.Dialog().ok("Info", msg)

    text13 = os.path.join(databasePath,"Textures13.db")
    if os.path.exists(text13)==True:
        try:
            os.unlink(text13)
        except:
            xbmcgui.Dialog().ok("Error", "Texture13 not removed. %s"% text13)
        pass

def cache_Cleanup():
    try:
        # Resolve the cache path
        cache_path = translatePath("special://cache/")
        xbmc.log(f"[Clear Cache] Resolved cache path: {cache_path}", level=xbmc.LOGDEBUG)

        # Verify path existence
        if not os.path.exists(cache_path):
            xbmcgui.Dialog().ok("Error", "Cache path not found. Operation aborted.")
            xbmc.log(f"[Clear Cache] Cache path not found: {cache_path}", level=xbmc.LOGERROR)
            return

        # Confirm action with the user
        dialog = xbmcgui.Dialog()
        if not dialog.yesno(
            "Clear Cache",
            f"This will delete all files in the cache directory:\n\n{cache_path}\n\nDo you want to continue?",
        ):
            xbmcgui.Dialog().ok("Canceled", "No changes were made.")
            return

        # Delete cache contents
        for item in os.listdir(cache_path):
            item_path = os.path.join(cache_path, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                xbmc.log(f"[Clear Cache] Deleted: {item_path}", level=xbmc.LOGDEBUG)
            except Exception as e:
                xbmc.log(f"[Clear Cache] Failed to delete {item_path}: {str(e)}", level=xbmc.LOGERROR)

        xbmcgui.Dialog().ok("Success", "Cache has been cleared successfully.")
        xbmc.log("[Clear Cache] Cache cleared successfully.", level=xbmc.LOGINFO)

    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"An error occurred while clearing the cache: {str(e)}")
        xbmc.log(f"[Clear Cache] Critical Error: {str(e)}", level=xbmc.LOGERROR)



def Clear_Cache():
        # cache_Cleanup()
        deleteThumbnails()
