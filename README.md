# 「青鸟殷勤」python自动化任务消息推送

> 基于[DingDing群聊机器人](https://open.dingtalk.com/document/robots/custom-robot-access)、[PushPlus](https://www.pushplus.plus/)、[ServerTurbo](https://sct.ftqq.com/)、[smtp邮件服务](https://baike.baidu.com/item/SMTP)的远程在线消息推送。
>
## 如何调用

```
# 导入文件
import MessagePush

title = "标题"
content = "内容"

# 使用钉钉webhook机器人
ding_secret = "钉钉机器人签名"
ding_token = "钉钉机器人Token"
DingTalkRebot(ding_secret, ding_token, title, content)

# 使用PushPlus
pushplus_token = “Pushplus的推送token”
PushPlus(pushplus_token, title, content)

# 使用ServerTurbo
serverturbo_token = "Server酱的token"
ServerTurbo(serverturbo_token, title, content)

# 使用SMTP邮件服务
username = “xxxx@xxx.xxx” # 发送人邮箱地址
password = "" # 发送人邮件密码
server = "smtp邮件服务器地址" # smtp.xxxx.xxxx
port = "邮件服务器端口" # 默认25
receiver = "收件人邮件地址" # 收件人地址
Send_Email(username, password, server, port, receiver, title, content)
```
> 除推送文字信息外还可支持其他内容推送，具体请看各部分官方文档