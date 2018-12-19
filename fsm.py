from transitions.extensions import GraphMachine
from utils import *
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from make_post import *
from uploadtoimgur import *

class TocMachine(GraphMachine):
    # def __init__(self, **machine_configs):
    #     self.machine = GraphMachine(
    #         model=self,
    #         **machine_configs
    #     )

    # def is_going_to_state1(self, event):
    #     if event.get("message"):
    #         text = event['message']['text']
    #         return text.lower() == 'go to state1'
    #     elif event.get("postback"):
    #         text = event['postback']['title']
    #         return text.lower() == 'go to state1'
    #     return False

    # def is_going_to_state2(self, event):
    #     if event.get("message"):
    #         text = event['message']['text']
    #         return text.lower() == 'go to state2'
    #     return False

    # def on_enter_state1(self, event):
    #     print("I'm entering state1")
    #     sender_id = event['sender']['id']
    #     responese = send_text_message(sender_id, "I'm entering state1")
    #     self.go_back()

    # def on_exit_state1(self):
    #     print('Leaving state1')

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")
    #     sender_id = event['sender']['id']
    #     # response = send_postback(sender_id)
    #     # response = send_image_url(sender_id)#,"https://i.imgur.com/o7lmGSy.png")
    #     response = send_generic(sender_id)
    #     # responese = send_text_message(sender_id, "I'm entering state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print('Leaving state2')
    count = 1
    cred = credentials.Certificate('./serviceAccount.json')

    # 初始化firebase，注意不能重複初始化
    firebase_admin.initialize_app(cred)

    # 初始化firestore
    db = firestore.client()

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_user(self):
        return True
        # if event.get("message"):
        #     text = event['message']['text']
        #     return text.lower() == 'start'
        # return False

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower()!='about' and text.lower()!='post' and text.lower()!='getinfo' :
                return True
            else:
                return False
        if event.get("postback"):
            text = event['postback']['title']
            if text.lower()!='about' and text.lower()!='post' and text.lower()!='getinfo' :
                return True
            else:
                return False
            # return text.lower() == 'about'
        # return bool(text.strip())
        # return text.lower() == 'go to state1'

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'about'
        if event.get("postback"):
            text = event['postback']['title']
            return text.lower() == 'about'
        return False
        # return text.lower() == 'about'

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'post'
        if event.get("postback"):
            text = event['postback']['title']
            return text.lower() == 'post'
        return False
        # return text.lower() == 'post'

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'getinfo'
        if event.get("postback"):
            text = event['postback']['title']
            return text.lower() == 'getinfo'
        return False
        # return text.lower() == 'getinfo'

    def is_going_to_class(self, event):
        if event.get("message"):
            text = event['message']['text']
            return bool(text.strip())
        return False
        # return bool(text.strip())

    def is_going_to_date(self, event):
        if event.get("message"):
            text = event['message']['text']
            return bool(text.strip())
        return False
        # return bool(text.strip())

    def is_going_to_time(self, event):
        if event.get("message"):
            text = event['message']['text']
            return bool(text.strip())
        return False
        # return bool(text.strip())

    def on_enter_user(self):
        # sender_id = event['sender']['id']
        # msg = "I'm entering user\nkey :\n about \n post \n getinfo\n"
        # responese = send_text_message(sender_id, msg)
        print("I'm entering user")
        # print('CURRENT STATE: ' + machine.state)
        # print("key :\n about \n post \n getinfo\n")
        # postback button
        # 1. about timing chatbot
        # 2. I want to share my event...
        # 3. I want to get events' info...


    def on_enter_state1(self,event):
        sender_id = event['sender']['id']
        msg = "Please push the following button or\nkey the following command :\n about \n post \n getinfo\n"
        responese = send_postback(sender_id, msg)
        # sender_id = event['sender']['id']
        # msg = "please key start"
        # responese = send_text_message(sender_id, msg)
        # print("I'm entering state1")
        # print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self,event):
        sender_id = event['sender']['id']
        msg = "「好的街舞活動，應該要讓更多人知道。」\n\n不管是教室成果展、party、battle、熱舞社迎新舞展....，\n只要是與街舞相關的大小活動，都歡迎告訴我\n\n我將固定更新於 Facebook 粉專的置頂貼文，並新增圖片至粉專相簿中，曝光您的活動！\n\n 若有人向我詢問相關活動，我也會向他們推薦您的活動！\n\n還等什麼，趕快按下'post'向我介紹你的活動吧！"
        response = send_postback(sender_id,msg)
        # responese = send_text_message(sender_id, msg)
        # print("I'm entering state2")
        # print('CURRENT STATE: ' + machine.state)
        # print("my name is bot bot")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self,event):
        sender_id = event['sender']['id']
        msg = "告訴我你的活動名稱！"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering state3")
        # print('CURRENT STATE: ' + machine.state)
        # print("what is the event's name?")
        # self.go_back()


    def on_enter_state4(self,event):
        sender_id = event['sender']['id']
        msg = "Tell me the date/month!\nI can reply you what event will take place!\nPlease key the date/month in this format\nMM/DD      EX:11/31\nM      EX:7\nMM     EX:12"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering state4")
        # print('CURRENT STATE: ' + machine.state)
        # print("enter the date\nI can tell you what event will take place on the day!\n")
        # print("please key the date in this format\nMMDD     EX:1231\nMM      EX:11")
        # self.go_back()

    def on_enter_getpost(self,event):
        text = event['message']['text']
        sender_id = event['sender']['id']
        flag = text.find('/')
        if flag == -1:
            flag = False
        else:
            flag = True
        if flag :
            tmp = text.split('/')
            docs =  self.db.collection('timing_event').where('month','==',int(tmp[0])).where('date','==',int(tmp[1])).get()
            for doc in docs:
                doc = doc.to_dict()
                response1 = send_image_url(sender_id,doc['imgurl'])
        else :
            docs =  self.db.collection('timing_event').where('month','==',int(text)).get()
            for doc in docs:
                doc = doc.to_dict()
                response1 = send_image_url(sender_id,doc['imgurl'])
        msg = "Here are all the events!!\nHave a nice day!^^"
        responese = send_postback(sender_id, msg)
        # ensure the input format is correct
        # find all the imageURL in firebase
        # send all the image back to client
        # print("I'm entering getpost")
        # print('CURRENT STATE: ' + machine.state)
        # print("this is all the event on the day!!\nhave a noce day!^^")
        self.go_back()

    def on_enter_class(self,event):
        # update database
        collection_ref = list(self.db.collection('timing_event').get())
        self.count = len(collection_ref) + 2
        doc_name = "event%d" % self.count
        doc = {}
        doc['title'] = event['message']['text']
        self.db.collection('timing_event').document(doc_name).set(doc)
        # reply
        sender_id = event['sender']['id']
        msg = "活動類別(限單選)\n請輸入以下選項：\nParty, Workshop, Dance Camp, Lecture, Showcase, Battle, Audition"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering class")
        # print('CURRENT STATE: ' + machine.state)
        # print("what is the event's class?")
        # self.go_back()

    def on_enter_date(self,event):
        # update database
        doc = {}
        doc['class'] = event['message']['text']
        doc_name = "event%d" % self.count
        self.db.collection('timing_event').document(doc_name).update(doc)
        # reply
        sender_id = event['sender']['id']
        msg = "活動日期/日期區間(Ex:11/31)"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering date")
        # print('CURRENT STATE: ' + machine.state)
        # print("what is the event's date?")
        # self.go_back()

    def on_enter_time(self,event):
        # update database
        text = event['message']['text']
        tmp = text.split('/')
        doc = {}
        doc['month'] = int(tmp[0])
        doc['date'] = int(tmp[1])
        doc_name = "event%d" % self.count
        self.db.collection('timing_event').document(doc_name).update(doc)
        # reply
        sender_id = event['sender']['id']
        msg = "活動時段"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering time")
        # print('CURRENT STATE: ' + machine.state)
        # print("what is the event's time?")
        # self.go_back()

    def on_enter_location(self,event):
        # update database
        doc = {}
        doc['time'] = event['message']['text']
        doc_name = "event%d" % self.count
        self.db.collection('timing_event').document(doc_name).update(doc)
        # reply
        sender_id = event['sender']['id']
        msg = "活動地點"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering location")
        # print('CURRENT STATE: ' + machine.state)
        # print("what is the event's the location?")
        # self.go_back()

    def on_enter_website(self,event):
        # update database
        doc = {}
        doc['location'] = event['message']['text']
        doc_name = "event%d" % self.count
        self.db.collection('timing_event').document(doc_name).update(doc)
        # reply
        sender_id = event['sender']['id']
        msg = "活動網址"
        responese = send_text_message(sender_id, msg)
        # print("I'm entering website")
        # print('CURRENT STATE: ' + machine.state)
        # print("what is the event's website URL??")
        # self.go_back()

    def on_enter_makepost(self,event):
        # update database
        doc = {}
        doc['url'] = event['message']['text']
        doc_name = "event%d" % self.count
        self.db.collection('timing_event').document(doc_name).update(doc)
        # reply
        # making post based on database 
        doc = self.db.collection('timing_event').document(doc_name).get().to_dict()
        makepost(doc,self.count)
        # upload image
        imgurl = upload2imgur(self.count)
        # update database
        doc = {}
        doc['imgurl'] = imgurl
        doc_name = "event%d" % self.count
        self.db.collection('timing_event').document(doc_name).update(doc)
        # send image to client
        sender_id = event['sender']['id']
        msg = "This is the post will be show!!\nif have any problem, feel free to contact us!"
        response1 = send_image_url(sender_id,imgurl)
        response2 = send_postback(sender_id, msg)
        # print("I'm entering makepost")
        # print('CURRENT STATE: ' + machine.state)
        # call make_post()
        # upload the image to imgur
        # send the image back to client
        # print("this is the post will be show!!\nif have any problem, feel free to contact us!")
        self.go_back()
