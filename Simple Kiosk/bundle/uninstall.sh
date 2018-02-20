#!/bin/sh

# remove all files we have copied to data folder
rm /assets/data/index.html
rm /assets/data/particles.min.js
rm /assets/presentation/reset-kiosk.sh

# delete transparent cursor
rm -fr /home/tooloop/.icons/default
openbox --restart