#!/bin/bash

URL="file:///assets/data/index.html"

# List of Chromium Command Line Switches
# https://peter.sh/experiments/chromium-command-line-switches/
COMMAND="chromium-browser \
--kiosk \
--bwsi \
--overscroll-history-navigation=1 \
--incognito \
--disable-infobars \
--disable-translate \
--no-default-browser-check \
--no-first-run \
--disable-translate-new-ux \
--num-raster-threads=4 \
--enable-zero-copy \
--noerrdialogs \
--class=TooloopKiosk \
$URL"

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
