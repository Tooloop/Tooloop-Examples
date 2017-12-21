#!/bin/bash
URL="vollstock.de"

if [ $EUID == 0 ]; then
    su tooloop -c "chromium-browser --noerrdialogs --kiosk --incognito $URL" &
else
    chromium-browser --noerrdialogs --kiosk --incognito $URL &
fi

exit 0