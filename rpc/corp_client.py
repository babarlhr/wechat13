# coding=utf-8

from wechatpy.enterprise import WeChatClient

# 用于agent应用API交互的client
client = None

# 用于通讯录API交互的client
txl_client = None

# 当前Agent
current_agent = None

UUID_OPENID = {}
OPENID_UUID = {}
OPENID_UID = {}
UID_UUID = {}

def init_client(appid, secret):
    global client
    client = WeChatClient(appid, secret)
    return client

def init_txl_client(appid, secret):
    global txl_client
    txl_client = WeChatClient(appid, secret)
    return txl_client

def chat_send(db,uuid, msg):
    _dict = UUID_OPENID.get(db,None)
    if _dict:
        openid = _dict.get(uuid,None)
        if openid:
            client.message.send_text(current_agent, openid, msg)
    return -1
