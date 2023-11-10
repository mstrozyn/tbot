import tbot

from tbot import tc

@tbot.testcase
def uname_test():
    with tbot.ctx.request(tbot.role.BoardLinux, reset=False) as targetLinux:
        targetLinux.exec0("uname", "-a")

@tbot.testcase
def ip_test():
    with tbot.ctx.request(tbot.role.BoardLinux, reset=False) as targetLinux:
        targetLinux.exec0("ip", "addr")

@tbot.testcase
def all():
    tc.testsuite(
        uname_test,
        ip_test
    )
