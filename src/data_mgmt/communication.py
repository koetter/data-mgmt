import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from markdown import markdown
import pymsteams
import logging
from . import configuration as conf


def send_mail(receivers, subject, markdown_text ):
    if "smtp" in conf.secrets["conn"]:
        smtp_conf = conf.secrets["conn"]["smtp"]
        print(smtp_conf)
        html_text = markdown(markdown_text)
        message = MIMEMultipart()
        message["From"] = smtp_conf["sender"]
        message["To"] = ", ".join(receivers)
        message["Subject"] = subject
        message.attach(MIMEText(html_text, "html"))
        str_message = message.as_string()
        try:
            with smtplib.SMTP(smtp_conf["host"], smtp_conf["port"]) as smtpObj:
                if smtp_conf["login"] != "":
                    smtpObj.login(smtp_conf.login, smtp_conf.pwd)
                
                smtpObj.sendmail(smtp_conf["sender"], receivers, str_message)
                logging.info("Mail sendt to {0}".format(receivers))
                print("Message was send")
        except smtplib.SMTPException:
            logging.error("Couldn't initiate SMTP service!")
            print("Couldn't initiate SMTP service!")

    else:
        logging.critical("SMTP service is not configured!")

def send_sms(receivers, test):
    pass

def send_teams_message(text_message, channel):
    if channel in conf.secrets["comm"]:
        webhook = conf.secrets["comm"][channel]
    else:
        print(f"Webhook for {channel} is not configured")
        exit

    myTeamsMessage = pymsteams.connectorcard(webhook)
    myTeamsMessage.text(text_message)
    myTeamsMessage.send()