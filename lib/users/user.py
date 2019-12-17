from lib.locale import Locale


class User:
    def __init__(self, user_name=None, user_email=None, locale='en'):
        self.user_name = user_name
        self.user_email = user_email
        self.is_logged_in = False
        self.user_locale = locale
        self.locale = Locale(self.user_locale)
