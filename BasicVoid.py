import asyncio
import datetime
import sys

import aiofiles

import BasicInfo


def sendSuccess(message):
    sendMsg("32", "[Success] " + message)


def sendInfo(message):
    sendMsg("37", "[Info] " + message)


def sendWarn(message):
    sendMsg("31", "[Warn] " + message)


def sendMsg(color, message):
    fullMessage = "[" + datetime.datetime.now().strftime('%H:%M:%S %f')[:-2] + "]" + message
    colorMessage = "\033[0;" + color + "m" + fullMessage + "\033[0m"
    print(colorMessage)
    # asyncio.run(writeMsg(fullMessage))
    sys.stdout.flush()


async def writeMsg(message):
    async with aiofiles.open('logs.txt', mode='a') as f:
        await f.write(message + '\n')


def getInput():
    return sys.stdin.readline().strip()
