<<<<<<< Updated upstream

from . import *
=======
import sys
from . import main, setup

rc = 1
try:
    main()
    rc = 0
except Exception as e:
    print('Error: %s' % e, file=sys.stderr)
sys.exit(rc)
>>>>>>> Stashed changes
