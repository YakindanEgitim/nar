import os

exec("from .{0} import *".format(os.environ.get("NAR_ENVIRONMENT", "dev")))
