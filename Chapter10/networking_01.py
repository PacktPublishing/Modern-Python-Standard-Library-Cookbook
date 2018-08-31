    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    from smtplib import SMTP


    class EmailSender(object):
        def __init__(self, host="localhost", port=25, login="", password=""):
            self._host = host
            self._port = int(port)
            self._login = login
            self._password = password
        
        def send(self, sender, recipient, subject, body):
            header_charset = 'UTF-8'
            body_charset = 'UTF-8'

            sender_name, sender_addr = parseaddr(sender)
            recipient_name, recipient_addr = parseaddr(recipient)

            sender_name = str(Header(sender_name, header_charset))
            recipient_name = str(Header(recipient_name, header_charset))

            msg = MIMEText(body.encode(body_charset), 'plain', body_charset)
            msg['From'] = formataddr((sender_name, sender_addr))
            msg['To'] = formataddr((recipient_name, recipient_addr))
            msg['Subject'] = Header(subject, header_charset)

            smtp = SMTP(self._host, self._port)
            try:
                smtp.starttls()
            except:
                pass
            smtp.login(self._login, self._password)
            smtp.sendmail(sender, recipient, msg.as_string())
            smtp.quit()


es = EmailSender('mail.myserver.it', 
                 login=EMAIL_ADDRESS, 
                 password=PASSWORD)
es.send(sender='Sender <no-reply@senders.net>', 
        recipient=EMAIL_ADDRESS,
        subject='Hello my friend!',
        body='''Here is a little email for you''')