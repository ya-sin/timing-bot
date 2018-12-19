from bottle import Bottle,route, run, request, abort, static_file

import sys
import os
# from io import BytesIO
from fsm import TocMachine
from local import *
# import sqlite3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils import send_postback,send_image_url,send_postback1

app = Bottle()

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

cred = credentials.Certificate('./serviceAccount.json')

# 初始化firebase，注意不能重複初始化
# firebase_admin.initialize_app(cred)

# 初始化firestore
# db = firestore.client()

# doc = {
#   'name': "QQ哥",
#   'email': "bbbbb@gmail.com"
# }

# 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用

# 語法
# doc_ref = db.collection("集合名稱").document("文件id")

# doc_ref = db.collection("test-app").document("student_02")
# path = "test-app"
# path3 = "pyradise_students"
# path2 = "test-app/student_03"
# doc_ref = db.document(path2)
# collection_ref = db.collection(path)
# students_ref = db.collection(path3)
# update
# contacts = {
#     'email': 'abc1@gmail.com',
#     'phone': '0910123456'
# }
# doc = {
#     'contacts': contacts,
#     'updateAt': firestore.SERVER_TIMESTAMP,
#     'email': firestore.DELETE_FIELD
# }
# doc = {
#     'contacts.email': 'abc1223@gmail.com'
# }
# doc = {
#     'email': firestore.DELETE_FIELD
# }
# doc_ref.delete()
# doc_ref.update()
# doc_ref提供一個set的方法，input必須是dictionary

# doc_ref.set(doc)
# try:
# gets = doc_ref.get()
# docs = students_ref.get()
# docs = collection_ref.where('number','>=', 1).get()
# for doc in docs:
#     doc.reference.delete()
    # print("文件內容為：{}".format(doc.to_dict()))
# except:
#     print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))

machine = TocMachine(
    states=[
        'fake',
        'user',
        'state1',
        'state2',
        'state3',
        'class',
        'date',
        'time',
        'location',
        'makepost',
        'website',
        'state4',
        'getpost'
    ],
    transitions=[
        {
            'trigger': 'gotouser',
            'source': 'fake',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'getname',
            'source': 'state3',
            'dest': 'class',
            'conditions': 'is_going_to_class'
        },
        {
            'trigger': 'getclass',
            'source': 'class',
            'dest': 'date',
            'conditions': 'is_going_to_date'
        },
        {
            'trigger': 'getdate',
            'source': 'date',
            'dest': 'time',
            'conditions': 'is_going_to_time'
        },
        {
            'trigger': 'gettime',
            'source': 'time',
            'dest': 'location',
            'conditions': 'is_going_to_time'
        },
        {
            'trigger': 'getlocation',
            'source': 'location',
            'dest': 'website',
            'conditions': 'is_going_to_time'
        },
        {
            'trigger': 'getwebsite',
            'source': 'website',
            'dest': 'makepost',
            'conditions': 'is_going_to_time'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'getinput',
            'source': 'state4',
            'dest': 'getpost',
            'conditions': 'is_going_to_time'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'makepost',
                'getpost'
            ],
            'dest': 'user'
        }
    ],
    initial='fake',
    auto_transitions=False,
    show_conditions=True,
)


@app.route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge
    else:
        abort(403)

@app.route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)
    if body['object'] == "page":
        # if body['entry'][0].get("standby") :
        #     event = body['entry'][0]['standby'][0]
        # else:
        event = body['entry'][0]['messaging'][0]
    if machine.state == 'state3':
        machine.getname(event)
    elif machine.state == 'class':
        machine.getclass(event)
    elif machine.state == 'date':
        machine.getdate(event)
    elif machine.state == 'time':
        machine.gettime(event)
    elif machine.state == 'location':
        machine.getlocation(event)
    elif machine.state == 'website':
        machine.getwebsite(event)
    # elif machine.state == 'makepost':
    #     machine.getpost(text)
    elif machine.state == 'state4':
        machine.getinput(event)
    elif machine.state == 'fake':
        sender_id = event['sender']['id']
        # msg = "I'm entering user\nkey :\n about \n post \n getinfo\n"
        # responese = send_text_message(sender_id, msg)
        response1 = send_image_url(sender_id,"https://i.imgur.com/Jo0FvJ0.jpg")
        response2 = send_postback(sender_id,"welcom to timing bot!^^")
        machine.gotouser()
    else:
        machine.advance(event)
        return 'OK'

    # if body['object'] == "page":
    #     # if body['entry'][0].get("standby") :
    #     #     event = body['entry'][0]['standby'][0]
    #     # else:
    #     event = body['entry'][0]['messaging'][0]
    #     machine.advance(event)
        # return 'OK'

@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

if __name__ == "__main__":
    # run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
    else:
        app.run(host='localhost', port=3000, debug=True, reloader=True)