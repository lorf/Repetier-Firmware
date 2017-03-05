# Repetier configuration for Anet A8-B with local mods

This repo tracks configuration changes specific to my printer. For generic Repetier Firmware please browse to https://github.com/repetier/Repetier-Firmware.

Following modifications were made so far:
* `Configuration.h` from `boards/Zonestar P802M` was copied over to this directory  and was fine-tuned for stock Anet A8-B;
* X-axis min endstop changed to NC;
* Calibrated hot-end thermistor and added user thermistor table;
* Autolevel sensor ([Mini Differential IR Z-probe](https://miscsolutions.wordpress.com/mini-height-sensor-board/), active-high output) connected instead of Z min endstop. `Z_PROBE_Z_OFFSET_MODE` set to 1 as it measures the distance to the coating surface;
* X/Y 0 coordinates are positioned at the center of the bed using `X_MIN_POS`, `Y_MIN_POS`. `Z_PROBE_(X|Y)(1|2|3)`, `ZHOME_(X|Y)_POS`, `DISTORTION_(X|Y)(MIN|MAX)` modified accordingly.

Firmware is built and uploaded using [PlatformIO](http://platformio.org/), configuration is in [platformio.ini](platformio.ini).
