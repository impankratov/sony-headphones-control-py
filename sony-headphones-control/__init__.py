#!/usr/bin/env python3

import sys
import bluetooth
import control

addr = None
mode = None

if len(sys.argv) < 3:
    print("Invalid arguments, please specify BT address and desired mode")
    sys.exit(0)
else:
    addr = sys.argv[1]
    mode = sys.argv[2]
    print("Searching for {}...".format(addr))

uuid = "96cc203e-5068-46ad-b32d-e316f5e069ba"
service_matches = bluetooth.find_service(uuid=uuid, address=addr)

if len(service_matches) == 0:
    print("Couldn't find the device service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
host = first_match["host"]

ambientSoundBytes = None

if mode == 'noise-cancelling':
    # Noise cancelling ?
    ambientSoundBytes = control.getAmbientSound(True, 2, 0, False)

elif mode == 'wind-cancelling':
    # Wind cancelling ?
    ambientSoundBytes = control.getAmbientSound(True, 1, 0, False)

elif mode == 'ambient-sound':
    # Ambient sound
    ambientSoundBytes = control.getAmbientSound(True, 0, 19, False)

elif mode == 'disable':
    # Disabled ambient sound control
    ambientSoundBytes = control.getAmbientSound(False, 0, 0, False)

else:
    print('Unknown mode, exiting')
    sys.exit(0)

print("Connecting to {} to enable {}".format(host, mode))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

# print('ambientSoundBytes', ambientSoundBytes)
packetBytes = control.getPacket(ambientSoundBytes)
# print('packetBytes', packetBytes)
packetCrcBytes = control.getCrcPacket(packetBytes)
# print('packetCrcBytes', packetCrcBytes)
result = bytes(packetCrcBytes)
# print('result', result)

sock.send(result)
sock.close()
