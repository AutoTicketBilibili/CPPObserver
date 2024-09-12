import BasicInfo
from BasicVoid import sendInfo


def sendBroadcast(message):
    if not BasicInfo.config["botEnable"]:
        return
    data = {
        "token": BasicInfo.config["botToken"],
        "type": "broadcast",
        "message": message
    }
    BasicInfo.sessionBot.post(BasicInfo.config["botAddress"],
                              headers=BasicInfo.headers,
                              json=data,
                              timeout=(9.05, 15.05))
    sendInfo("正在发送信息......")