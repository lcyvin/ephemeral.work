from lib.enums.base import BaseEnum

class Locales(BaseEnum):
    EN = ()
    FR = ()

    @classmethod
    def __getitem__(self, item):
        v = None
        item = item.upper()
        if hasattr(self, item):
            v = getattr(self, item)
        return v

    @classmethod
    def __gatattr__(self, item):
        return self.__getitem__(item)

    @classmethod
    def get(self, item):
        return self.__getitem__(item)
