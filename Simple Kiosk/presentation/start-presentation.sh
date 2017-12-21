#!/bin/bash

URL="file:///assets/data/index.html"
su tooloop -c "chromium-browser --noerrdialogs --kiosk --incognito $URL" &

exit 0