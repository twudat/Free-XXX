from kodi_six import xbmc, xbmcaddon, xbmcplugin, xbmcgui, xbmcvfs
from six.moves.urllib.parse import parse_qs, quote_plus, urlparse, parse_qsl
from six import PY2

import os
import re
import sys
import requests
import base64
import time
from resources.lib.modules import downloaderrepo as tools
from resources.lib.modules import extract
from resources.lib.modules import addon_able
translatePath = xbmc.translatePath if PY2 else xbmcvfs.translatePath
addon_id = 'plugin.video.free-xxx-o-dus'
checkfile = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'addon.xml'))
addonPath = os.path.join(os.path.join(translatePath(
    'special://home'), 'addons'), 'plugin.video.free-xxx-o-dus')
AddonTitle = '[COLOR pink][B]FREE-XXX-O-DUS[/B][/COLOR]'
dialog = xbmcgui.Dialog()
REPO = translatePath(os.path.join(
    'special://home/addons', 'repository.free-xxx-o-dus'))



# This bit really only get called from scrapers
def checkupdates():
    s = open(checkfile, 'r').read()
    a = re.findall('<addon\s+id=.+?version="(.*?)"', s, flags=re.DOTALL)[0]
    b = requests.get(
        'https://github.com/twudat/free-xxx/raw/main/addons.xml').text
        # 'https://raw.githubusercontent.com/twudat/free-xxx-o-dus/main/addons.xml').text

    c = re.findall(
        '<addon\s+id="plugin.video.free-xxx-o-dus".+?version="(.*?)"', b, flags=re.DOTALL)[0]
    if a == c:
        pass
    else:
        dialog.ok("[COLOR red][B]WARNING[/B][/COLOR]",
                  "[COLOR yellow]None Supported Version Of FREE-XXX-O-DUS Or Addon Out Of Date, Use Official Version From Twudat Repo, You May Just Need To Update Your Addon[/COLOR]")
        quit()
