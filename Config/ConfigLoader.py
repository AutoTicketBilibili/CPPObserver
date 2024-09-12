import json
import os.path

import BasicInfo
from BasicVoid import sendInfo
from Config import ConfigUpdate


def loadConfig():
    if not os.path.isfile("config.json"):
        sendInfo("配置文件不存在！重新生成配置文件！")
        BasicInfo.config = {
            "eula": False,
            "cookies": "",
            "botEnable": True,
            "botAddress": "http://127.0.0.1:9999/API",
            "botToken": "1234567890",
            "mailEnable": True,
            "mailAddress": "http://127.0.0.1:7654/API",
            "mailToken": "1234567890",
            "eventID": "1729",
            "enableTicketTypeCheck": True,
            "enableNoticeCheck": True
        }
        ConfigUpdate.writeConfig()
        return
    fileConfig = open("config.json", 'r', encoding='utf-8')
    BasicInfo.config = json.load(fileConfig)
    sendInfo("已读取配置文件")
