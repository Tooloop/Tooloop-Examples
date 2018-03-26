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
                file.write('COMMAND="chromium-browser --kiosk --bwsi --incognito --class=TooloopKiosk --disable-infobars --no-default-browser-check --no-first-run --noerrdialogs $URL"\n')
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
