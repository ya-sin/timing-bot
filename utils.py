import requests
import os
from local import *

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_generic(id):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[
                        {
                            "title":"Welcome!",
                            "image_url":"https://i.imgur.com/o7lmGSy.png",
                            "subtitle":"We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://github.com/jw84/messenger-bot-tutorial",
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://developers.facebook.com/docs/messenger-platform/send-messages"
                            },
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"https://imgur.com/a/XcGYZWO",
                                    "title":"View Website"
                                },{
                                    "type":"postback",
                                    "title":"Start Chatting",
                                    "payload":"DEVELOPER_DEFINED_PAYLOAD"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
def send_postback1(id):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{"id":id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"about",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"post",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"getinfo",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
def send_postback(id,msg):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{"id":id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":msg,
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"about",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"post",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"getinfo",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_image_url(id,img_url):#, img_url):
    print("ha")
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        # "recipient":{
        #     "id": id
        # },
        # "message":{
        #     "attachment":{
        #         "type":"image",
        #         "payload":{
        #             "attachment_id": "2209441962660937",
        #             # "url":"https://i.imgur.com/ZfD2mIR.png",
        #             # "is_reusable": true
        #         }
        #     }
        # }
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type":"image",
                "payload":{
                    "url": img_url,
                    "is_reusable": True
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send image: " + response.text)
    return response
"""
def send_button_message(id, text, buttons):
    pass
"""
