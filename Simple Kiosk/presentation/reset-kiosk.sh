#!/bin/bash

URL="file:///assets/data/index.html"

# List of Chromium Command Line Switches
# https://peter.sh/experiments/chromium-command-line-switches/
COMMAND="chromium-browser --kiosk --bwsi --incognito --class=TooloopKiosk --disable-infobars --no-default-browser-check --no-first-run --noerrdialogs $URL"

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
