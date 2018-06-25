# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, abort
from os import chown
from pwd import getpwnam
from grp import getgrnam

class InstalledApp(object):

    def __init__(self, flask):
        super(InstalledApp, self).__init__()

        # default homepage
        self.homepage = 'file:///assets/data/index.html';

        # connect flask routes to tooloop api calls
        self.add_routes(flask)



    def add_routes(self, flask):
        
        @flask.route('/simple-kiosk/change-homepage', methods=['POST'])
        def change_homepage():
            if not request.form or not 'homepage' in request.form:
                abort(400)

            try:
                self.homepage = request.form['homepage'];

                file = open('/assets/presentation/reset-kiosk.sh','w') 

                file.write('#!/bin/bash\n')
                file.write('\n')
                file.write('URL="'+self.homepage+'"\n')
                file.write('\n')
                file.write('# List of Chromium Command Line Switches\n')
                file.write('# https://peter.sh/experiments/chromium-command-line-switches/\n')
                file.write('COMMAND="chromium-browser \\\n')
                file.write('--kiosk \\\n')
                file.write('--bwsi \\\n')
                file.write('--overscroll-history-navigation=1 \\\n')
                file.write('--incognito \\\n')
                file.write('--disable-infobars \\\n')
                file.write('--disable-translate \\\n')
                file.write('--no-default-browser-check \\\n')
                file.write('--no-first-run \\\n')
                file.write('--disable-translate-new-ux \\\n')
                file.write('--num-raster-threads=4 \\\n')
                file.write('--enable-zero-copy \\\n')
                file.write('--noerrdialogs \\\n')
                file.write('--class=TooloopKiosk \\\n')
                file.write('$URL"\n')
                file.write('\n')
                file.write('if [ $EUID == 0 ]; then\n')
                file.write('    pkill chromium\n')
                file.write('    sleep 0.1\n')
                file.write('    su tooloop -c "$COMMAND" &\n')
                file.write('else\n')
                file.write('    pkill chromium\n')
                file.write('    sleep 0.1\n')
                file.write('    $COMMAND &\n')
                file.write('fi\n')
                file.write('\n')
                file.write('exit 0\n')

                file.close() 
            
                uid = getpwnam('tooloop').pw_uid
                gid = getgrnam('tooloop').gr_gid
                chown('/assets/presentation/reset-kiosk.sh', uid, gid)

                return jsonify({'message':'homepage changed'})

            except Exception as e:
                abort(500)
