import shutil
import os
import json
from zipfile import ZipFile

if not os.path.exists('user'):
    os.makedirs('user')

with open('user/.user-rev', 'w+') as fp:
    fp.write('CUSTOM @ fffffff')

with open('files.json', 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)

for src in list(obj.keys()):
    dest = obj[src]
    if '/' in dest:
        if not os.path.exists('user/{}'.format(
                              dest[:dest.rfind('/')])):
            os.makedirs('user/{}'.format(dest[:dest.rfind('/')]))
        for folder in range(len(dest.split('/'))-1):
            with open('user/{}/.directory'.format('/'.join(
                      dest.split('/')[:folder+1])), 'w+') as fp:
                pass
    shutil.copyfile('../{}'.format(src), 'user/{}'.format(dest))

with ZipFile('robot.zip', 'w') as zp:
    zp.write('info.yaml')
    zp.write('overlay.sr2020.2.squash')
    zp.write('wifi.yaml')
    for folderName, subfolders, filenames in os.walk('user'):
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            zp.write(filePath)
