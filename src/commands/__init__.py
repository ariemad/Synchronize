from . import start
from . import show
from . import set

command = type('command', (), {'start': start.start, 'set': set.set, 'show': show.show})