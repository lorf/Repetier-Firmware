# Repetier configuration for Anet A8-B with local mods

This repo tracks configuration changes specific to my printer. For generic
Repetier Firmware please browse to
https://github.com/repetier/Repetier-Firmware.

## Modifications

Following modifications were made so far:
* `Configuration.h` from `boards/Zonestar P802M` was copied over to this
  directory  and was fine-tuned for stock Anet A8-B;
* X-axis min endstop changed to NC;
* Calibrated hot-end thermistor and added user thermistor table;
* Autolevel sensor ([Mini Differential IR
  Z-probe](https://miscsolutions.wordpress.com/mini-height-sensor-board/),
  active-high output) connected instead of Z min endstop. Z probe X/Y position
  is set using `Z_PROBE_(X|Y)_OFFSET`. `Z_PROBE_Z_OFFSET_MODE` set to 1 as it
  measures the distance to the coating surface;
* X/Y 0 coordinates are positioned at the center of the bed using `X_MIN_POS`,
  `Y_MIN_POS`. `Z_PROBE_(X|Y)(1|2|3)`, `ZHOME_(X|Y)_POS`,
  `DISTORTION_(X|Y)(MIN|MAX)` modified accordingly.

## Building firmware

Firmware is built and uploaded using [PlatformIO](http://platformio.org/),
configuration is in [platformio.ini](platformio.ini).

## Start G-code

I use the following start G-code in Slic3r:

```
M104 S[first_layer_temperature] ; set extruder temperature
M140 S[first_layer_bed_temperature] ; set desired heat bed temperature
M116 ; wait for all temperatures
G91 ; use relative coords
G1 Z10 F10000 ; lift nozzle
G90 ; use absolute coords
G28 X Y ; home X and Y
G1 X0 Y0 F10000; position on the center of the bed
G32 ; autolevel
G1 Z5 F10000
G1 X0 Y0 F10000
```
