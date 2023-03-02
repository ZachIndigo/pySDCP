 # pySDCP
Sony SDCP / PJ Talk projector control 

Python **3** library to query and control Sony Projectors using SDCP (PJ Talk) protocol  over IP.

##Features:
* Autodiscover projector using SDAP (Simple Display Advertisement Protocol)
* Query and change power status
* Query and change mute status
* Toggle input between HDMI-1 and HDMI-2

## More features
The SDCP protocol allow to control practically everything in projector, i.e. resolution, brightness, 3d format...
If you need to add a command:

- add the name and code into COMMANDS dictionary, i.e.

```
 COMMANDS = {
     "SET_POWER": 0x0130,
+    "SET_MUTE": 0x0030,
     "CALIBRATION_PRESET": 0x0002,
     "ASPECT_RATIO": 0x0020,
     "INPUT": 0x0001,
     "GET_STATUS_ERROR": 0x0101,
     "GET_STATUS_POWER": 0x0102,
     "GET_STATUS_LAMP_TIMER": 0x0113
 }
```

- if necessary, add additional information to _protocols.py_, i.e.:

```
+MUTE_STATUS = {
+    "MUTE": 0,
+    "UNMUTE": 1
+}
```

- add function to _\_\_init.py\_\__ implementing the new command, i.e.

```
+    def set_mute(self, mute=True):
+        self._send_command(action=ACTIONS["SET"], command=COMMANDS["SET_MUTE"],
+                           data=POWER_STATUS["START_UP"] if mute else POWER_STATUS["STANDBY"])
+        return True
```

### Protocl Documnetation:
* [Link](https://www.digis.ru/upload/iblock/f5a/VPL-VW320,%20VW520_ProtocolManual.pdf)
* [Link](https://docs.sony.com/release//VW100_protocol.pdf)


#Supported Projectors
Supported Sony projectors should include:
* VPL-VW515
* VPL-VW520
* VPL-VW528
* VPL-VW665
* VPL-VW315
* VPL-VW320
* VPL-VW328
* VPL-VW365
* VPL-VW100
* VPL-HW65ES
* VPL-FHZ700L

## Installation 
`pip install git+https://github.com/ZachIndigo/pySDCP`

## Examples


Sending any command will initiate autodiscovery of projector if none is known and will cary on the command. so just go for it and maybe you get lucky:
```
import pySDCP

my_projector = pySDCP.Projector()

my_projector.get_power()
my_projector.set_power(True)
```

Skip discovery to save time or if you know the IP of the projector
```
my_known_projector = pySDCP.Projector('10.1.2.3')
my_known_projector.set_HDMI_input(2)
```

# Credits
This project is a fork of [pySDCP by
Galala7](https://github.com/Galala7/pySDCP).
This plugin is based on [sony-sdcp-com](https://github.com/vokkim/sony-sdcp-com) NodeJS library by [vokkim](https://github.com/vokkim).

## See also
 [homebridge-sony-sdcp](https://github.com/Galala7/homebridge-sony-sdcp) Homebridge plugin to control Sony Projectors.
 
