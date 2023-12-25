from email.message  import EmailMessage

import ssl
import smtplib


class Email2Sender:


    def create_email_body(email_body):
        email_sender = "johnsaxe90@gmail.com"
        email_password= "hukyoxlhcpduyrin"
        email_receiver =['mr.akshitgupta@gmail.com','gupta@dynamitenetwork.com', 'musson@dynamitenetwork.com']
        body = ''
        body = email_body
        subject="""Websites Status Check"""
        em = EmailMessage()
        em['From'] =  email_sender
        em['To'] = ','.join(email_receiver)
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())



