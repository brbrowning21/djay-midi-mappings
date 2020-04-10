
# USBID

`USBID` is (Vendor ID << 4) + Product ID

Vendor ID: 0x2580
Product ID: 0x0005

`2*(16^7)+5*(16^6)+8*(16^5)+5`

```
<key>USBID</key>
<integer>629145605</integer>
```



# Default output

```
<key>output</key>
<dict/>
```

means output on midiChannel + 1 (one channel up), same
note (midiData), 0 as min and 127 as max

# Modifiers

Secret modifierState and modifier1, etc.

# midiMessageType

Note On/Off: omitted
Control Change (CC): 3

# output.keyPath = "modifierState.modifier1"

```
<dict>
	<key>keyPath</key>
	<string>modifierState.modifier1</string>
	<key>midiMaxValue</key>
	<integer>64</integer>
</dict>
```

Shows up as channel 1

# Modular DJ MidiPipe

Need to create virtual inputs of the same name "Modular DJ"

It *is* possible to map hidden outputs, using the `<outputs>` tag.
TODO: does the outputs tag need to go after `<endpointName>`?

# AST Builder

Monitor `.djayMidiMapping` file, look for changes
When a change is detected, read the file.
Build up a template (options? isn't there a formalized XML structure for this?)
that template can be used to

Wait why do we need to generate the XML elements? Why not just parse the existing (valid) mappings?

# Notes

`<key>version</key>`
ranges from 1 to 4

What does that mean?
Can different versions have different tags?

