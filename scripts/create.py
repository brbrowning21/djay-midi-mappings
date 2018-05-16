import lxml.etree as ET
import os

FILE = '/Users/brbrowning21/Music/djay Pro 2/MIDI Mappings/outputs_keyPath_options.txt'
F_OUT = '/Users/brbrowning21/Music/djay Pro 2/MIDI Mappings/outputs_keyPath_options_midigen.xml'

root_outputs_array = ET.Element('array')

def plist_kv(ele, key_text, value_type, value_text):
    k = ET.SubElement(ele, 'key')
    k.text = key_text
    v = ET.SubElement(ele, value_type)
    v.text = value_text

with open(FILE, 'r') as f_in:

    i = 0

    for line in f_in:
        d = ET.Element('dict')
        plist_kv(d, 'controlType', 'string', 'control')
        plist_kv(d, 'keyPath', 'string', line.strip())
        plist_kv(d, 'midiChannel', 'integer', '0')
        plist_kv(d, 'midiData', 'integer', str(i))
        plist_kv(d, 'midiMessageType', 'integer', '3')

        root_outputs_array.append(d)

        i += 1

    f_out = open(F_OUT, 'wb')
    f_out.write(ET.tostring(root_outputs_array, pretty_print=True))
