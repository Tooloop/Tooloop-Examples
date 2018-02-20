#!/bin/bash

COMMAND="chromium-browser --noerrdialogs --kiosk --incognito /assets/presentation/slideshow.html"

if [ $EUID == 0 ]; then
    su tooloop -c "$COMMAND" &
else
    $COMMAND &
fi

exit 0
