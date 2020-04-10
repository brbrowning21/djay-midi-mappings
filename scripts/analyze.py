import os
import glob
import plistlib
import csv


filepaths = [
    '/Applications/djay Pro 2.app/Contents/Resources/MIDI Mappings',
    # '/Users/brbrowning21/Music/djay Pro 2/MIDI Mappings'
]

csvfile = open('outputcsv.csv', 'w', newline='')
fieldnames = [
    'filename',
    'hidElementKey',
    'keyPath',
    'controlType',
    'midiChannel',
    'midiData',
    'midiMessageType',
    'midiMaxValue',
    'midiMinValue',
    'flipped'
]
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

for path in filepaths:
    for xml_file in glob.glob(path + '/*.djayMidiMapping'):
        p = plistlib.load(open(xml_file, 'rb'))

        if 'outputs' in p:
            for o in p['outputs']:
                o['filename'] = xml_file
                writer.writerow(o)

