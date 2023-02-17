def getAmbientSound(enabled: bool, noiseCancelling: int, volume: int, voice: bool):
    enabledValue = 16 if enabled else 0
    return [0, 0, 0, 8, 104, 2, enabledValue, 2, noiseCancelling, 1, voice, volume]

def getPacket(data: list):
    packetPrefix = [12, 0]
    packet = packetPrefix + data
    return packet

def getCrcPacket(packet: list): 
    crc = 0

    for b in packet:
        crc += b

    crcPacket = [62] + packet + [crc] + [60]

    return crcPacket
