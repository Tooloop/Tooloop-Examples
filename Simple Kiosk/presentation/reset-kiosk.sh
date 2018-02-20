#!/bin/bash

URL="file:///assets/data/index.html"
COMMAND="chromium-browser --noerrdialogs --kiosk --incognito $URL"

if [ $EUID == 0 ]; then
    pkill chromium
    sleep 0.1
    su tooloop -c "$COMMAND" &
else
    pkill chromium
    sleep 0.1
    $COMMAND &
fi

exit 0
