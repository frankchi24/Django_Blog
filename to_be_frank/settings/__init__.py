from .base import *
from .production import *
if os.environ['DEBUG']==True:
    try:
        from .local import *
    except:
        pass
