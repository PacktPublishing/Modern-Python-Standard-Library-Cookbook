EMAILS = [
    {'sender': 'author1@domain.com', 'subject': 'First email',
     'body': 'This is my first email'},
    {'sender': 'author2@domain.com', 'subject': 'Second email',
     'body': 'This is my second email'},
]

import cmd
import shlex

class MyMail(cmd.Cmd):
    intro = 'Simple interactive email client.'
    prompt = 'mymail> '

    def __init__(self, *args, **kwargs):
        super(MyMail, self).__init__(*args, **kwargs)
        self.selected_email = None

    def do_list(self, line):
        """list

        List emails currently in the Inbox"""
        for idx, email in enumerate(EMAILS):
            print('[{idx}] From: {e[sender]} - {e[subject]}'.format(
                    idx=idx, e=email
            ))

    def do_read(self, emailnum):
        """read [emailnum]

        Reads emailnum nth email from those listed in the Inbox"""
        try:
            idx = int(emailnum.strip())
        except:
            print('Invalid email index {}'.format(emailnum))
            return

        try:
            email = EMAILS[idx]
        except IndexError:
            print('Email {} not found'.format(idx))
            return

        print('From: {e[sender]}\n'
              'Subject: {e[subject]}\n'
              '\n{e[body]}'.format(e=email))
        # Track the last read email as the selected one for reply.
        self.selected_email = idx

    def do_reply(self, message):
        """reply [message]

        Sends back an email to the author of the received email"""
        if self.selected_email is None:
            print('No email selected for reply.')
            return

        email = EMAILS[self.selected_email]
        print('Replied to {e[sender]} with: {message}'.format(
            e=email, message=message
        ))

    def do_send(self, arguments):
        """send [recipient] [subject] [message]

        Send a new email with [subject] to [recipient]"""
        # Split the arguments with shlex
        # so that we allow subject or message with spaces.
        args = shlex.split(arguments)
        if len(args) < 3:
            print('A recipient, a subject and a message are required.')
            return

        recipient, subject, message = args[:3]
        if len(args) >= 4:
            message += ' '.join(args[3:])

        print('Sending email {} to {}: "{}"'.format(
            subject, recipient, message
        ))

    def complete_send(self, text, line, begidx, endidx):
        # Provide autocompletion of recipients for send command.
        return [e['sender'] for e in EMAILS if e['sender'].startswith(text)]

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    MyMail().cmdloop()
