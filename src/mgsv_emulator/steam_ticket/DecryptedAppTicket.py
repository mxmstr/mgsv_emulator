import struct

class AppTicketV1:
    def __init__(self):
        self.TicketSize = 0
        self.TicketVersion = 0
        self.Unk2 = 0
        self.UserData = []

    def reset(self):
        self.TicketSize = 0
        self.TicketVersion = 0
        self.Unk2 = 0
        self.UserData.clear()

    def serialize(self):
        buffer = bytearray()
        buffer.extend(struct.pack('<I', self.TicketSize))
        buffer.extend(struct.pack('<I', self.TicketVersion))
        buffer.extend(struct.pack('<I', self.Unk2))
        buffer.extend(struct.pack('<I', len(self.UserData)))
        buffer.extend(self.UserData)
        return buffer

    def deserialize(self, buffer):
        if len(buffer) < 16:
            return False

        self.TicketSize, self.TicketVersion, user_data_size, self.Unk2 = struct.unpack('<IIII', buffer[:16])
        if len(buffer) < (user_data_size + 16):
            return False

        self.UserData = buffer[16:16 + user_data_size]
        return True

class AppTicketV2:
    LicenseBorrowed = 0x00000002
    LicenseTemporary = 0x00000004

    def __init__(self):
        self.TicketSize = 0
        self.TicketVersion = 0
        self.SteamID = 0
        self.AppID = 0
        self.Unk1 = 0
        self.Unk2 = 0
        self.TicketFlags = 0
        self.TicketIssueTime = 0
        self.TicketValidityEnd = 0

    def reset(self):
        self.TicketSize = 0
        self.TicketVersion = 0
        self.SteamID = 0
        self.AppID = 0
        self.Unk1 = 0
        self.Unk2 = 0
        self.TicketFlags = 0
        self.TicketIssueTime = 0
        self.TicketValidityEnd = 0

    def serialize(self):
        buffer = bytearray()
        buffer.extend(struct.pack('<I', self.TicketSize))
        buffer.extend(struct.pack('<I', self.TicketVersion))
        buffer.extend(struct.pack('<Q', self.SteamID))
        buffer.extend(struct.pack('<I', self.AppID))
        buffer.extend(struct.pack('<I', self.Unk1))
        buffer.extend(struct.pack('<I', self.Unk2))
        buffer.extend(struct.pack('<I', self.TicketFlags))
        buffer.extend(struct.pack('<I', self.TicketIssueTime))
        buffer.extend(struct.pack('<I', self.TicketValidityEnd))
        return buffer

    def deserialize(self, buffer):
        if len(buffer) < 40:
            return False

        self.TicketSize, self.TicketVersion, self.SteamID, self.AppID, self.Unk1, self.Unk2, \
        self.TicketFlags, self.TicketIssueTime, self.TicketValidityEnd = struct.unpack('<IIQIIIIII', buffer[:40])
        return True

class AppTicketV4:
    def __init__(self):
        self.AppIDs = []
        self.HasVACStatus = False
        self.VACStatus = 0
        self.HasAppValue = False
        self.AppValue = 0

    def reset(self):
        self.AppIDs.clear()
        self.HasVACStatus = False
        self.HasAppValue = False

    def serialize(self):
        appids = self.AppIDs
        if len(appids) == 0:
            appids.append(0)

        appid_count = min(len(appids), 140)
        buffer_size = appid_count * 4 + 2
        buffer = bytearray()
        buffer.extend(struct.pack('<H', appid_count))

        for i in range(appid_count):
            buffer.extend(struct.pack('<I', appids[i]))

        if self.HasVACStatus:
            buffer.extend(struct.pack('<I', self.VACStatus))

        if self.HasAppValue:
            buffer.extend(struct.pack('<I', self.AppValue))

        return buffer

    def deserialize(self, buffer):
        if len(buffer) < 2:
            return False

        appid_count = struct.unpack('<H', buffer[:2])[0]
        if len(buffer) < (appid_count * 4 + 2) or appid_count >= 140:
            return False

        self.AppIDs = list(struct.unpack(f'<{appid_count}I', buffer[2:2 + appid_count * 4]))
        buffer = buffer[2 + appid_count * 4:]

        self.HasVACStatus = False
        self.HasAppValue = False

        if len(buffer) >= 4:
            self.HasVACStatus = True
            self.VACStatus = struct.unpack('<I', buffer[:4])[0]
            buffer = buffer[4:]

        if len(buffer) >= 4:
            self.HasAppValue = True
            self.AppValue = struct.unpack('<I', buffer[:4])[0]

        return True

class DecryptedAppTicket:
    def __init__(self):
        self.TicketV1 = AppTicketV1()
        self.TicketV2 = AppTicketV2()
        self.TicketV4 = AppTicketV4()

    def deserialize_ticket(self, buffer):
        if not self.TicketV1.deserialize(buffer):
            return False

        buffer = buffer[16 + len(self.TicketV1.UserData):]
        if not self.TicketV2.deserialize(buffer):
            return False

        if self.TicketV2.TicketVersion > 2:
            buffer = buffer[40:]
            if not self.TicketV4.deserialize(buffer):
                return False

        return True

    def serialize_ticket(self):
        self.TicketV1.TicketSize = len(self.TicketV1.UserData) + 40 + 2 + (
                    (1 if len(self.TicketV4.AppIDs) == 0 else len(self.TicketV4.AppIDs)) * 4) + (
                                              4 if self.TicketV4.HasVACStatus else 0) + (
                                              4 if self.TicketV4.HasAppValue else 0)
        self.TicketV2.TicketSize = self.TicketV1.TicketSize - len(self.TicketV1.UserData)

        buffer = self.TicketV1.serialize()
        buffer += self.TicketV2.serialize()
        buffer += self.TicketV4.serialize()

        return buffer
