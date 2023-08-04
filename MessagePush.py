# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import smtplib
import time
import urllib
from email.mime.text import MIMEText
import requests


def DingTalkRebot(ding_secret, ding_token, title, info):
    timestamp = str(round(time.time() * 1000))
    secret = ding_secret
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    rebot_address = "https://oapi.dingtalk.com/robot/send?access_token="
    head = {"content-type": "application/json"}
    message = {"msgtype": "text", "text": {"content": title+f"{info}"}}
    requests.post(rebot_address + ding_token + "&timestamp=" + timestamp + "&sign=" + sign, json=message, headers=head)


def PushPlus(pushplus_token, title, info):
    url = 'http://www.pushplus.plus/send'
    data = {"token": pushplus_token, "title": title, "content": info}
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=body, headers=headers)


def ServerTurbo(serverturbo_token, title, info):
    token = serverturbo_token
    url = "https://sctapi.ftqq.com/"
    requests.get(url + "/" + token + ".send?title=" + title + "&desp=" + info)


def Send_Email(EMAIL_SENDER_USERNAME, EMAIL_SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT, EMAIL_RECEIVER, title, info):
    if EMAIL_SENDER_USERNAME is None or EMAIL_SENDER_USERNAME == '@':
        return
    smtp = smtplib.SMTP()
    smtp.connect(SMTP_SERVER, SMTP_PORT)
    smtp.login(EMAIL_SENDER_USERNAME, EMAIL_SENDER_PASSWORD)
    message = MIMEText(info, 'plain', 'utf-8')
    message['Subject'] = title
    message['From'] = EMAIL_SENDER_USERNAME
    message['To'] = EMAIL_RECEIVER
    smtp.sendmail(EMAIL_SENDER_USERNAME, EMAIL_RECEIVER, message.as_string())
    smtp.quit()
