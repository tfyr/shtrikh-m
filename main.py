import serial

from shtrikh.commands import Beep, PullPaper, PrintLine, PrintBoldLine

from shtrikh.pos import Pos

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
    print(ser.name)
    commands = (
        Beep(),
        PrintBoldLine('Евгений Онегин.'),
        PullPaper(1),
        PrintLine('Мой дядя самых честных правил'),
        PrintLine('Когда не в шутку занемог'),
        #CassirReport(),
    )

    pos = Pos(ser)
    for current_command in commands:
        pos.proccess(current_command)
