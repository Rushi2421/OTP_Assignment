
from twilio.rest import Client
import random
import sms
import smtplib
import re

client = Client(sms.account_sid, sms.Auth_token)

def generate_OTP():                                   # generate OTP
    global otp
    otp= ''.join([str(random.randint(0, 9)) for i in range(6)])

fotp=generate_OTP()

def validate_mobile(num):                             # validating mobile numbebr
    return len(num) == 10 and num.isdigit()

def send_otp_over_mobile(target_no):                  #send OTP On SMS
    if (validate_mobile(target_no)):
        target_no = "+91" + target_no
        message = client.messages.create(
            body="\nYour OTP is "+str(otp),
            from_=sms.twilio_no,
            to=sms.target_no
        )
        print(message.body)

    else:
        print("INVALID MOBILE NUMBER!")
        target_no = input("ENTER AGAIN: ")
        validate_mobile(target_no)
        send_otp_over_mobile(target_no)



def validate_email(mail):                              # validiate email id with Natural langauge Processing
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,mail):
        return True;
    else:
        return False;



def send_otp(mail):                                     #send OTP via Email
    if (validate_email(mail)):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('rushirapashe11@gmail.com', 'qzlxjfftbfieqwmu')
        msg = 'HELLO YOUR OTP IS ' + str(otp)
        server.sendmail('rushirapashe11@gmail.com', mail, msg)
        server.quit()
        print("OTP sent! ")
        print("Your OTP is",str(otp))
    else:
        print("INVALID MAIL!")
        mail = input("ENTER AGAIN: ")
        validate_email(mail)
        send_otp(mail)


#__Menu__

print("\n========================================Welcome to generate OTP========================================")
print("\n                                   <------CHOOSE PLATFORM------>                              \n\n1.SMS:\n2.Email:")
ans = input("\nENTER YOUR CHOICE:\n")

if (ans.lower() == "1"):

    number = input("ENTER YOUR MOBILE NUMBER: ")
    validate_mobile(number)
    send_otp_over_mobile(number)

elif (ans.lower() == "2"):

    recipent = input("ENTER YOUR MAIL ID:\n ")
    send_otp(recipent)

