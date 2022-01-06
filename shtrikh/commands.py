from shtrikh import xor_control_sum


class Command:
    def __init__(self):
        self.data = bytearray()

    def get_data(self):
        ret = len(self.data).to_bytes(1, byteorder="big") + self.data
        return ret + xor_control_sum(ret).to_bytes(1, byteorder="big")

    def add_admin_password(self):
        self.data.append(0x1e)  # password
        self.data.append(0x00)
        self.data.append(0x00)
        self.data.append(0x00)

    def add_len_and_crc(self):
        ret = len(self.data).to_bytes(1, byteorder="big") + self.data
        return ret + xor_control_sum(ret).to_bytes(1, byteorder="big")


class Beep(Command):
    def __init__(self):
        super().__init__()
        self.data.append(0x13)  # command beep
        self.add_admin_password()


class PrintLine(Command):
    def __init__(self, text):
        super().__init__()
        self.data.append(0x17)  # print standart line
        self.add_admin_password()
        self.data.append(0b01000010)  # print at check ribbon
        self.data += bytearray(text.encode('cp1251'))


class PrintBoldLine(Command):
    def __init__(self, text):
        super().__init__()
        self.data.append(0x12)  # print standart line
        self.add_admin_password()
        self.data.append(0b01000010)  # print at check ribbon
        self.data += bytearray(text.encode('cp1251'))


class PullPaper(Command):
    def __init__(self, lines_count):
        super().__init__()
        self.data.append(0x29)  # print standart line
        self.add_admin_password()
        self.data.append(0b00000010)  # print at check ribbon
        self.data += lines_count.to_bytes(1, byteorder="big")


class CashierReport(Command):
    def __init__(self):
        super().__init__()
        self.data.append(0x44)  # command cashier report
        self.add_admin_password()
