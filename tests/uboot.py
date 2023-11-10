import tbot

from tbot import tc

@tbot.testcase
def bdinfo_test():
    with tbot.ctx.request(tbot.role.BoardUBoot, reset=False) as targetUBoot:
        targetUBoot.exec0("bdinfo")

@tbot.testcase
def version_test():
    with tbot.ctx.request(tbot.role.BoardUBoot, reset=False) as targetUBoot:
        targetUBoot.exec0("version")

@tbot.testcase
def all():
    tc.testsuite(
        bdinfo_test,
        version_test
    )
