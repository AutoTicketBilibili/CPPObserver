import io

import BasicVoid
import Config.ConfigLoader
import Config.ConfigUpdate
import Observer.ObserverTicketType
import Observer.ObserverNotice
from BasicVoid import *


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
    sendInfo("欢迎使用CPPObserver")
    sendInfo("作者By MossCG")
    Config.ConfigLoader.loadConfig()
    checkEULA()
    BasicInfo.headers["Cookie"] = BasicInfo.config["cookies"]
    if BasicInfo.config["enableTicketTypeCheck"]:
        Observer.ObserverTicketType.runObserver()
    if BasicInfo.config["enableNoticeCheck"]:
        Observer.ObserverNotice.runObserver()


def checkEULA():
    if BasicInfo.config["eula"]:
        return
    sendInfo("在使用本软件前请先同意EULA（最终用户许可协议）")
    sendWarn("本软件仅供学习交流，使用所造成的一切后果与作者无关！")
    while True:
        sendInfo("如果你同意EULA，请输入：true 并回车")
        result = BasicVoid.getInput()
        if result == "true":
            sendSuccess("已同意EULA！")
            break
    Config.ConfigUpdate.updateConfig("eula", "true")


if __name__ == "__main__":
    main()
