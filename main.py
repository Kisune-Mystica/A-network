import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.#gmail.com', 25)

server.ehlo()

with open('#password.txt', 'r') as f:
    password = f.read()

server.login('#your mail', password)

msg= MIMEMultipart()
msg['From'] = '#your mail'
msg['To'] = '#recepient mail'
msg['Subject'] = 'Hello Kitsune Coolest Youtuber'

with open('#message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = '#picture.jpeg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('#your mail', '#recepient mail', text)


#run

#msg wth picture
