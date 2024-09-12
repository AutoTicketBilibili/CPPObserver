import BasicInfo
from BasicVoid import sendInfo


def sendMail(message):
    if not BasicInfo.config["mailEnable"]:
        return
    data = {
        "token": BasicInfo.config["mailToken"],
        "mailTitle": "CPP变动提醒",
        "mailSenderName": "CPPObserver",
        "mailContent": message
    }
    BasicInfo.sessionBot.post(BasicInfo.config["mailAddress"],
                              headers=BasicInfo.headers,
                              json=data,
                              timeout=(9.05, 15.05))
    sendInfo("正在发送邮件......")