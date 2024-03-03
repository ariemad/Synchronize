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
        "show": show.show,
        "validate": validate.validate,
    },
)
