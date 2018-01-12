#!/bin/bash
URL="file:///assets/data/index.html"

if [ $EUID == 0 ]; then
    su tooloop -c "chromium-browser --noerrdialogs --kiosk --incognito $URL" &
else
    chromium-browser --noerrdialogs --kiosk --incognito $URL &
fi

exit 0