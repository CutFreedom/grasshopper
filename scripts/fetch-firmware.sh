#!/bin/sh
#
# Download ALL known firmware binaries to the current directory
#
# ------
# For codenames and versions, see:
#   https://github.com/CutFreedom/grasshopper/wiki/Firmware
# or
#   https://help.cricut.com/hc/en-us/articles/360009504953-How-do-I-find-the-current-firmware-version-on-my-machine-
#

BASE=https://imgservice.cricut.com/design-public-mirror1/software/Firmware

curl --remote-name $BASE/Zorro/FirmwareZorro-1.091.bin
curl --remote-name $BASE/Helium/FirmwareHelium-3.091.bin
curl --remote-name $BASE/Helium2/FirmwareHelium2-5.120.bin
curl --remote-name $BASE/Warro/FirmwareWarro-2.098.bin
curl --remote-name $BASE/Athena/FirmwareAthena-4.175.bin

# Download some non-current, if they are still available
curl --remote-name $BASE/Warro/FirmwareWarro-2.095.bin
