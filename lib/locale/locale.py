import json
from lib.locale.data import Data
from lib.enums import Locales


class Locale:
    def __init__(self, locale):
        self.locale = locale
        if not Locales.get(self.locale):
            self.locale = 'en'

        self.data = None

    def page(self, page):
        ld_raw = self._get_page_locale_data(page)
        self.data = Data(ld_raw)
        return self

    def _get_page_locale_data(self, page):
        lc_file = open('templates/locales/{}/{}.json'.format(self.locale, page))
        locale_info = json.load(lc_file)
        return locale_info
