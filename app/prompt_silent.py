import sys
from setup import client

command = ' '.join(sys.argv[1:])
client.disable_logging()
client.generate(command)