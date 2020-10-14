from flask import Flask, render_template,session,redirect,url_for,request
def otpmsg(phone,otp):
    try:
        import requests
        import json
        URL = 'https://www.way2sms.com/api/v1/sendCampaign'
        otp="Your OTP is "+str(otp)+"\n For more information visit https://salonport.com"
        # get request
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
            'apikey':'QFWDXYU32CC7GCQSLL62GAJ8FCCPPU58',
            'secret':'XWUKJXZE9SSTCOYE',
            'usetype':'stage',
            'phone': phone,
            'message':otp,
            'senderid':'ABCDAE'
            }
            return requests.post(reqUrl, req_params)
        response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
    except Exception as e:
        print(e)
def sendmail(Email,otp):
    try:
        import smtplib
        import os
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.message import EmailMessage
        from email.utils import make_msgid
        import mimetypes
        # me == my email address
        # you == recipient's email address
        me = "salon.businesssb@gmail.com"
        you = Email
        msg = EmailMessage()
        # generic email headers
        msg['Subject'] = 'OTP'
        msg['From'] = 'salon.businesssb@gmail.com'
        msg['To'] = Email
        # set the plain text body
        msg.set_content('This is a mail for OTP.')
        # now create a Content-ID for the image
        image_cid = make_msgid(domain='xyz.com')
        # if `domain` argument isn't provided, it will
        # use your computer's name
        # set an alternative html body
        msg.add_alternative("""\
        <html>
            <body>
                <img height=200rem width=100% src="cid:{image_cid}">
                <br>
                <h1>OTP = {otp}<h1>

            </body>
        </html>
        """.format(image_cid=image_cid[1:-1],otp=otp), subtype='html')
        with open('static/img/background.jpg', 'rb') as img:
            # know the Content-Type of the image
            maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
            # attach it
            msg.get_payload()[1].add_related(img.read(),
                                                 maintype=maintype,
                                                 subtype=subtype,
                                                 cid=image_cid)
        # Send the message via local SMTP server.
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("salon.businesssb@gmail.com","@mitH@ritw@l")
        server.sendmail(me,you,msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
