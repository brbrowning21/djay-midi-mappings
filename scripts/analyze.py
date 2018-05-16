import lxml.etree as ET
import os
import glob

filepaths = [
    '/Applications/djay Pro 2.app/Contents/Resources/MIDI Mappings',
    '/Users/brbrowning21/Music/djay Pro 2/MIDI Mappings'
]

for path in filepaths:
    for xml_file in glob.glob(path + '/*.djayMidiMapping'):
        xml = ET.parse(xml_file)
        root = xml.getroot()
        keys = root[0].findall('key')
        for key in keys:
            if key.text == 'outputs':
                # print(xml_file)
                outputs = key.getnext()
                for output_dict in outputs:
                    for dict_key in output_dict.findall('key'):
                        if dict_key.text == 'keyPath':
                            print(dict_key.getnext().text)
