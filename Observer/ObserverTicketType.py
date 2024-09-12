import threading
import time

import API.APIGetTicketTypeList
import API.APIBroadcast
import API.APIMail
import BasicVoid

task = "票种监听"


def runObserver():
    BasicVoid.sendInfo("正在启动"+task+"线程......")
    thread = threading.Thread(target=observer, name=task+"线程", args=())
    thread.start()


def observer():
    ticketList = []
    ticketName = ""
    while True:
        try:
            time.sleep(1)
            newList = []
            data = API.APIGetTicketTypeList.getTicketTypeList()
            for typeTicket in data["ticketTypeList"]:
                price = typeTicket["ticketPrice"]/100
                newList.append(typeTicket["ticketName"]+" ￥"+str(price))

            if ticketName != data["ticketMain"]["name"]:
                if ticketName == "":
                    BasicVoid.sendInfo("当前监听展演："+data["ticketMain"]["eventName"])
                if ticketName != "":
                    message = "票名更新提醒\n"
                    message += ("原名：" + ticketName + "\n")
                    message += ("现名：" + data["ticketMain"]["name"])
                    BasicVoid.sendInfo(message)
                    API.APIBroadcast.sendBroadcast(message)
                    API.APIMail.sendMail(message)

            if ticketList != newList:
                if ticketList:
                    message = "票种更新提醒\n"
                    message += (data["ticketMain"]["eventName"] + "\n")
                    message += "票种如下："
                    for ticket in newList:
                        message += "\n"
                        message += ticket
                    BasicVoid.sendInfo(message)
                    API.APIBroadcast.sendBroadcast(message)
                    API.APIMail.sendMail(message)

            ticketName = data["ticketMain"]["name"]
            ticketList = newList
        except Exception as e:
            BasicVoid.sendWarn(str(repr(e)))
            BasicVoid.sendWarn(task+"报错啦！再试试！")

