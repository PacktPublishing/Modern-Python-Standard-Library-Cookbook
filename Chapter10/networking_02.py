import imaplib
import re
from email.parser import BytesParser


class IMAPReader:
    ENCODING = 'utf-8'
    LIST_PATTERN = re.compile(
        r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)'
    )
    
    def __init__(self, host, username, password, ssl=True):
        if ssl:
            self._imap = imaplib.IMAP4_SSL(host)
        else:
            self._imap = imaplib.IMAP4(host)
        self._imap.login(username, password)

    def folders(self):
        """Retrieve list of IMAP folders"""
        resp, lines = self._imap.list()
        if resp != 'OK':
            raise Exception(resp)

        entries = []
        for line in lines:
            flags, _, name = self.LIST_PATTERN.match(
                line.decode(self.ENCODING)
            ).groups()
            entries.append(dict(
                flags=flags,
                name=name.strip('"')
            ))
        return entries

    def messages(self, folder, limit=10, peek=True):
        """Return ``limit`` messages from ``folder``

        peek=False will also fetch message body
        """
        resp, count = self._imap.select('"%s"' % folder, readonly=True)
        if resp != 'OK':
            raise Exception(resp)
        
        last_message_id = int(count[0])
        msg_ids = range(last_message_id, last_message_id-limit, -1)
        
        mode = '(BODY.PEEK[HEADER])' if peek else '(RFC822)'

        messages = []
        for msg_id in msg_ids:
            resp, msg = self._imap.fetch(str(msg_id), mode)
            msg = msg[0][-1]

            messages.append(BytesParser().parsebytes(msg))
            if len(messages) >= limit:
                break
        return messages

    def get_message_body(self, message):
        """Given a message for which the body was fetched, returns it"""
        body = []
        if message.is_multipart():
            for payload in message.get_payload():
                body.append(payload.get_payload())
        else:
            body.append(message.get_payload())
        return body

    def close(self):
        """Close connection to IMAP server"""
        self._imap.close()

mails = IMAPReader('imap.gmail.com', 
                   USER_NAME, 
                   PASSWORD,
                   ssl=True)
folders = mails.folders()
for msg in mails.messages('INBOX', limit=4, peek=False):
    print(msg['Date'], msg['Subject'])
    # print(mails.get_message_body(msg))
