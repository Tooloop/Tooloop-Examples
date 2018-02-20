#!/bin/bash

IDLETIME=60
RESET_COMMAND="/bin/bash /assets/presentation/reset-kiosk.sh"

$RESET_COMMAND
xidlerun -t $IDLETIME -c "$RESET_COMMAND" &

exit 0
