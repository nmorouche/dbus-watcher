echo "Pairing..."
sudo pkill -f LCDDisplay.py
python /home/pi/Documents/PA/AVRCP/dbus-watcher/LCDDisplay.py " " " " &
sudo pkill -f LCDDisplay.py
python /home/pi/Documents/PA/AVRCP/dbus-watcher/LCDDisplay.py "Appairage" "En cours..." &
expect disconnect_BT.expect
sleep 3
expect connect_BT.expect > expect_script.log
chmod 777 expect_script.log
sleep 2

echo "Trusting and connecting.."
device_mac_address=$(cat expect_script.log | grep -Pom 1 "(?<=Device ).*(?= Paired)")
echo mac address is $device_mac_address
if [ $device_mac_address ] ; then
            expect trust_BT.expect $device_mac_address
else
            echo "No device connected"
fi
expect discoverable_off.expect
sudo pkill -f LCDDisplay.py
python /home/pi/Documents/PA/AVRCP/dbus-watcher/LCDDisplay.py " " " " &
sleep 2
sudo pkill -f LCDDisplay.py
#rm -f expect_script.log
