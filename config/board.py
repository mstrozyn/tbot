import tbot

from tbot.machine import board, connector, linux

class RemoteLab(connector.SSHConnector, linux.Bash):
    hostname = "tester"
    username = "tester"
    port = 3333

class Board(connector.ConsoleConnector, board.PowerControl, board.Board):
    baudrate = 115200
    serial_port = "/dev/ttyS0"

    def poweron(self):
        with tbot.ctx.request(tbot.role.LabHost) as labHost:
            tbot.log.message("Power on the board")
            labHost.exec0("/home/tester/utils/reboot.py", "-p", "/dev/ttyS0", "--ps2000")

    def poweroff(self):
        with tbot.ctx.request(tbot.role.LabHost) as labHost:
            tbot.log.message("Power off the board")
            pass

    def connect(self, machine):
        return machine.open_channel("/home/tester/picocom/picocom", "-b", str(self.baudrate), self.serial_port)

class BoardUBoot(board.Connector, board.UBootAutobootIntercept, board.UBootShell):
    prompt = "=> "

class BoardLinux(board.Connector, board.LinuxBootLogin, linux.Bash):
    login_prompt = "board login: "
    username = "tester"
    password = "tester"

def register_machines(ctx):
    ctx.register(RemoteLab, tbot.role.LabHost)
    ctx.register(Board, tbot.role.Board)
    ctx.register(BoardUBoot, tbot.role.BoardUBoot)
    ctx.register(BoardLinux, tbot.role.BoardLinux)
