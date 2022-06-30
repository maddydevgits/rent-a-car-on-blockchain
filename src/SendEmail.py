import boto3
from botocore.exceptions import ClientError
import random

accessKey='' # ask admin to share accessKey
secretAccessKey='' # ask admin to share secret
region='us-east-1'

def verifyIdentity(a):
    client=boto3.client('ses',aws_access_key_id=accessKey,aws_secret_access_key=secretAccessKey,region_name=region)
    response = client.verify_email_identity(EmailAddress = a)
    print(response)


def sendmessage(sub,walletaddr,pickup,dropoff,pickupdate,dropoffdate,pickuptime,cartype,phoneno,r):
    client=boto3.client('ses',aws_access_key_id=accessKey,aws_secret_access_key=secretAccessKey,region_name=region)
    SENDER = "otp.service@makeskilled.com"
    RECIPIENT = r
    SUBJECT = sub
    BODY_HTML = """<html>
        <head></head>
        <body>
        <h1>"""+SUBJECT+"""</h1>
        <p> Your Wallet Address """+str(walletaddr)+""" .<br> <br>
        Your Pickup """+str(pickup)+""" . <br/><br/>
        Your Dropoff """+str(dropoff)+""" . <br/><br/>
        Your Email Id """+str(r)+""" . <br/><br/>
        Your Pickup Date """+str(pickupdate)+""" . <br/><br/>
        Your Dropoff Date """+str(dropoffdate)+""" . <br/><br/>
        Your Pickup Time """+str(pickuptime)+""" . <br/><br/>
        Your Car Type """+str(cartype)+""" . <br/><br/>
        Your Phoneno """+str(phoneno)+""" . <br/><br/>
        Thanks, <br>
        Make Skilled Dev Team <br>
        </p>
        </body>
        </html>
    """
    # The character encoding for the email.
    CHARSET = "UTF-8"
    try:
        #Provide the contents of the email.
        response = client.send_email(Destination={'ToAddresses': [RECIPIENT,],},
        Message={'Body': {'Html': {'Charset': CHARSET,'Data': BODY_HTML,},
        'Text': {'Charset': CHARSET,'Data': ""},},
        'Subject': {'Charset': CHARSET,'Data': SUBJECT,},},
        Source=SENDER)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        return True