#!/bin/sh

python avrcp_watcher.py &
python Bluetooth/bluetooth_pairing.py &
python master_volume_watcher.py &

