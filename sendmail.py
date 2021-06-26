#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import os
import configparser

class mail:
    def __init__(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        configPath = os.path.join(proDir,"config.ini")
        parser = configparser.ConfigParser()
        parser.read(configPath,encoding='UTF-8')
        send_mail = {}
        send_mail = parser.items('sendmail')
        self.host_server = send_mail[0][1]
        self.sender_qq = send_mail[1][1]
        self.pwd = send_mail[2][1]
        self.sender_qq_mail = send_mail[3][1]
        self.mail_title = send_mail[4][1]
    def mail(self,str,e_mail):
    #qq邮箱smtp服务器
        
        #收件人邮箱
        receiver = e_mail

        #邮件的正文内容
        mail_content = str
        #邮件标题       若需要修改自行设置
        mail_title = self.mail_title    

        #ssl登录
        smtp = SMTP_SSL(self.host_server)
        #set_debuglevel()参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(self.host_server)
        smtp.login(self.sender_qq, self.pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = self.sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(self.sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
