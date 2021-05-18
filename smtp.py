import smtplib
from email.utils import  formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def send_email(server, email, password, to, cc, subject, body, attachement):

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = ', '.join(to)
    msg['cc'] = ', '.join(cc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))
    part1 = MIMEBase('application', "octet-stream")
    part1.set_payload(open(attachement, "rb").read())
    encoders.encode_base64(part1)
    part1.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(attachement))
    msg.attach(part1)

    smtp = smtplib.SMTP(server, port=587)
    ehlo_res = smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)
    res = smtp.sendmail(email, to+cc, msg.as_string())
    smtp.close()
