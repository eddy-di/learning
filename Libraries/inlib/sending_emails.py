from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib
# email package with subpackage mime (Multipurpose Internet Mail Extensions) standart that defines the format for email messages
# multipart is a subpackage of mime that exposes MIMEMultipart class which allows to send both html and plain text content

template = Template(Path(r"Libraries\inlib\template_html.html").read_text())

message = MIMEMultipart()
message["from"] = "Mirlanov Eldiyar"
message["to"] = "eddy.di.minur@gmail.com"
message["subject"] = "This is test message"
body = template.substitute({"name": "Eddie"})
# MIMEText object allows to insert text into a body of mail
message.attach(MIMEText(body, "html"))
# MIMEText object allows to insert text into a body of mail
message.attach(MIMEImage(Path("Libraries/inlib/gj.png").read_bytes()))
# lines 6-10 represent a mail message object to send it need to use smtp server

with smtplib.SMTP(host="smtp.yandex.com", port=465) as smtp:
    smtp.ehlo()  # hello message in smtp protocol, basically it says to smtp protocol "I'm a client and I want to send an email"
    smtp.starttls()  # tls = transport layaer security it encrypts all the commands that are sent to smtp
    smtp.login("eddy.di@yandex.com", "SuSJv5%oE44kQx3$")
    smtp.send_message(message)
    print("Sent...")
# some error occured when doing it, will v=come to it later
