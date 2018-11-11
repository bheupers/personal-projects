'''
Script to capture fritzbox traffic
'''

import re
import getpass
import sys
import os
import hashlib
from urllib.parse import urlencode
from urllib.request import urlopen

IFACE='1-lan'
SIDFILE='/tmp/fritz.sid'
FRITZBOX='http://fritz.box'
FRITZUSER=''


def makeDots(str):
    newstr = ''
    for c in str:
        if ord(c) > 255:
            newstr += '.'
        else:
            newstr += c
    return newstr.encode('ascii', 'replace')


def main():
    password = getpass.getpass()
    print (password)
    if len(password) == 0:
        print("Password required")
        sys.exit(0)

    start = urlopen(FRITZBOX + '/login_sid.lua')
    mybytes = start.read()
    mystr = mybytes.decode("utf8")
    start.close()

    p = re.compile(r'<Challenge>([a-f0-9]{8})', re.MULTILINE)
    m = p.search(mystr)
    if m:
        challenge = m.group(1)
    else:
        print (" No challenge ")
        sys.exit(0)

    # Compute response
    # password = makeDots(password)
    response = challenge + '-' + password
    lresponse = []
    for c in response:
        lresponse.extend((c, chr(0)))
    response = ''.join(lresponse)
    response = challenge + '-' + hashlib.md5(response.encode('ascii', 'ignore')).hexdigest()

    post_data = [('response', response), ('username', '')]
    f = urlopen(FRITZBOX + '/login_sid.lua', urlencode(post_data).encode("utf-8"))
    mybytes = f.read()
    mystr = mybytes.decode("utf8")
    f.close()
    p = re.compile(r'<SID>([a-f0-9]{16})', re.MULTILINE)
    m = p.search(mystr)
    if m:
        # SID = m.group(1).encode('ascii', 'replace')
        SID = m.group(1)
        print(f"SID {SID}")
        with open(SIDFILE, 'w') as sid_file:
            sid_file.write(SID)
    else:
        print ("No SID ")
        sys.exit(0)

    capture = urlopen(FRITZBOX + f'/cgi-bin/capture_notimeout?ifaceorminor={IFACE}&snaplen=&capture=Start&sid={SID}')
    file_name = 'capture.eth0'

    f = open(file_name, 'wb')
    meta = capture.info()
    # file_size = int(meta.getheaders("Content-Length")[0])
    # print ('Downloading: %s Bytes: %s' % (file_name, file_size) )


    count = 0
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = capture.read(block_sz)
        count += 1

        if count > 20:
            s = urlopen(FRITZBOX + f'/cgi-bin/capture_notimeout?iface={IFACE[2:]}&minor={IFACE[:2]}&type=1&capture=Stop&sid={SID}')

        if not buffer or count > 1000:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d" % (file_size_dl)
        status = status + chr(8) * (len(status) + 1)
        print (status + ',')

    f.close()

if __name__ == "__main__":
    main()
