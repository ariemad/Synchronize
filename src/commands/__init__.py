from . import start
from . import show
from . import set
from . import validate

command = type(
    "command",
    (),
    {
        "start": start.start,
        "set": set.set,
        "showLog": show.showLog,
        "showConfig": show.showConfig,
        "validate": validate.validate,
    },
)
