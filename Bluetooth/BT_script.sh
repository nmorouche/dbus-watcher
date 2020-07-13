#!usr/bin/sh

echo "Pairing..."
sudo pkill -f LCDDisplay.py
python /home/pi/Documents/PA/AVRCP/dbus-watcher/LCDDisplay.py " " " " &
sudo pkill -f LCDDisplay.py
python /home/pi/Documents/PA/AVRCP/dbus-watcher/LCDDisplay.py "Appairage" "En cours..." &
expect /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/disconnect_BT.expect
sleep 3
expect /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/connect_BT.expect > /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/expect_script.log
chmod 777 expect_script.log
sleep 2

echo "Trusting and connecting.."
device_mac_address=$(cat /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/expect_script.log | grep -Pom 1 "(?<=Device ).*(?= Paired)")
echo mac address is $device_mac_address
if [ $device_mac_address ] ; then
            expect /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/trust_BT.expect $device_mac_address
else
            echo "No device connected"
fi
expect /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/discoverable_off.expect
sudo pkill -f LCDDisplay.py
python /home/pi/Documents/PA/AVRCP/dbus-watcher/LCDDisplay.py " " " " &
sleep 2
sudo pkill -f LCDDisplay.py
rm -f /home/pi/Documents/PA/AVRCP/dbus-watcher/Bluetooth/expect_script.log
