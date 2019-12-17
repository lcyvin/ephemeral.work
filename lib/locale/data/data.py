class LocaleItemPathException(Exception):
    pass


class Data:
    def __init__(self, ld_raw):
        self.ld_raw = ld_raw

    def get(self, item):
        val = self.ld_raw.get(item)
        if isinstance(val, dict):
            val = Data(val)
        return val

    def __getattr__(self, name):
        return self.get(name)
