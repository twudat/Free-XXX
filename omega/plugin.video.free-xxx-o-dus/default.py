from kodi_six import xbmc, xbmcaddon, xbmcplugin, xbmcgui, xbmcvfs
from six.moves.urllib.parse import parse_qs, quote_plus, urlparse, parse_qsl
from six import PY2

import sys
import kodi
import re
import urllib
import os
import shutil
import base64
import time
import requests
from resources.lib.modules import downloaderrepo as tools
from resources.lib.modules import extract
from resources.lib.modules import utils
from resources.lib.modules import mainmenu
from resources.lib.modules import parental
from resources.lib.modules import firstStart
from resources.lib.modules import addon_able
parentalCheck = parental.parentalCheck


def main(argv=None):
    if sys.argv:
        argv = sys.argv
    queries = utils.parse_query(sys.argv[2])
    mode = queries.get('mode', None)
    utils.url_dispatcher.dispatch(mode, queries)
    if kodi.get_setting('dev_debug') == 'true':
        utils.url_dispatcher.showmodes()


if __name__ == '__main__':
    firstStart.run()
    parentalCheck()
    sys.exit(main())
