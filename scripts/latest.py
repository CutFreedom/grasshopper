#!/usr/bin/env python3
#
# Simple script to fetch "latest.json" files for information about
# the latest platform executables.
#

import time
import json
import http.client


DESIGN_HOST = 'staticcontent.cricut.com'
DESIGN_ROOT = '/a/software'

PLATFORMS = {
    'osx-native',
    'win32-native',
    }

#    'osx-plugin',


def fetch_latest(platform):
    conn = http.client.HTTPSConnection(DESIGN_HOST)
    path = f'{DESIGN_ROOT}/{platform}/latest.json'
    print('PATH:', path)
    conn.request('GET', path)
    r = conn.getresponse()
    content = r.read()
    return json.loads(content)


def latest_info():
    for p in PLATFORMS:
        data = fetch_latest(p)
        #print('DATA:', data)
        print('PLATFORM:', p)
        print('  rollout start:', time.ctime(data['rolloutStart']))
        print('            end:', time.ctime(data['rolloutEnd']))
        print(f'     base: {data["baseVersion"]} via "{DESIGN_ROOT}/{p}/{data["baseInstallFile"]}"')
        print(f'  rollout: {data["rolloutVersion"]} via "{DESIGN_ROOT}/{p}/{data["rolloutInstallFile"]}"')
        # also: paused, rolloutUpdateFile, rolloutUpdateFileHash, enforcedFeatureConfig

if __name__ == '__main__':
    latest_info()
