from shtrikh import STX, ACK, NAK, ENQ, lrc


class Pos():
    def __init__(self, serial):
        self.ser = serial

    def parse_data(self, data):
        print("parsing data: ", data)


    def wait_answer(self):
        j = 0
        ret = self.ser.read()
        if ret == STX:
            length = self.ser.read()
            data = self.ser.read(int.from_bytes(length, byteorder='big'))
            cs = self.ser.read()  # todo check control sum
            if lrc(length + data).to_bytes(1, "big") == cs:
                self.ser.write(ACK)
                self.parse_data(data)
                return True
            else:
                self.ser.write(NAK)
                j += 1
        return False

    def send_command(self, command):
        i = 0
        while i < 10:
            self.ser.write(STX)
            self.ser.write(command.get_data())
            if self.ser.read() == ACK:
                if self.wait_answer():
                    return True
            i += 1
        return False

    def proccess(self, command):
        while True:
            self.ser.write(ENQ)  # ENQ
            ret = self.ser.read()
            if ret == ACK:
                if self.wait_answer():
                    break
            elif ret == NAK:
                if self.send_command(command):
                    break
            else:
                continue

