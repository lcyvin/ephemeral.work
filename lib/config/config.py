# Config class default will contain values which do not change
# between various execution modes. We will load
# a new class over BaseConfig with ENV variables assigned to
# the class values needed to run in PROD/DEBUG/Et Al.

import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

