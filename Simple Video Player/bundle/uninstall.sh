#!/bin/sh

# remove all files we have copied to data folder
rm /assets/data/tooloop-greeter*

# we have installed it, we should remove it also
apt -y purge mplayer
