import lxml.etree as ET
import os
import glob
import plistlib
import csv
import json

filepaths = [
   '/Applications/djay Pro 2.app/Contents/Resources/MIDI Mappings',
    # '/Users/brbrowning21/Music/djay Pro 2/MIDI Mappings'
]

# Iterate through all output sections of every factor MIDI mapping

csvfile = open('all_output.csv', 'w', newline='')
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
    'flipped',
    'inGlobalSection',
    'buttonMode',
    'pickupMode',
    'rotarySensitivity',
    'condition'
]
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

for path in filepaths:
    for xml_file in glob.glob(path + '/*.djayMidiMapping'):
        p = plistlib.load(open(xml_file, 'rb'))

        if 'controls' in p:
            for c in p['controls']:
                if 'output' in c:

                    o = c['output']

                    # Throw out empty dict tag
                    if not o:
                        continue

                    # Want to write a row that
                    # is the combination of two
                    # dicts
                    d = {**c, **c['output']}
                    del d['output']
                    # print(asdf)
                    # print(json.dumps(asdf, indent=4))
                    # exit()
                    d['filename'] = xml_file
                    d['inGlobalSection'] = False
                    writer.writerow(d)

        if 'outputs' in p:
            for o in p['outputs']:
                o['filename'] = xml_file
                o['inGlobalSection'] = True
                writer.writerow(o)

