#!/usr/bin/env python3
#
# Simple script to extract the "app.asar" Electron application.
#
# USAGE:
#   $ ./unpack.py /path/to/mounted/dmg outputAppDir
#

import sys
import os.path
import struct
import json

import asar

ASAR_PATH = 'Contents/Resources/app.asar'


def open_archive(fname):
    "Open an ASAR archive."

    # FORMAT:
    #   UINT32: size of HEADER_SIZE (always 4)
    #   UINT32: size of HEADER field (including SIZE value)
    #   UINT32: size of HEADER field
    #   STRING: header
    #     UINT32: length of HEADER
    #     BYTES: header content
    #
    # NOTE: the HEADER STRING might be shorter than the HEADER FIELD.
    #   Padding has been observed, which pads the content out to a
    #   longer FIELD than the actual HEADER content.
    #
    fp = open(fname, 'rb')
    leader = fp.read(16)

    hdr_len = struct.unpack('<I', leader[12:16])[0]
    hdr = fp.read(hdr_len).decode('utf-8')
    files = json.loads(hdr)

    # Files begin after the HEADER_SIZE and HEADER fields.
    baseoffset = 8 + struct.unpack('<I', leader[4:8])[0]

    return asar.AsarArchive(fname, fp, files, baseoffset)


def unpack_archive(sourcedir, destdir):
    for fn in os.listdir(sourcedir):
        if fn.endswith('.app'):
            archive = open_archive(os.path.join(sourcedir, fn, ASAR_PATH))
            break
    else:
        print('ERROR: could find .app subdir')
        sys.exit(1)

    archive.extract(destdir)


if __name__ == '__main__':
    unpack_archive(sys.argv[1], sys.argv[2])
