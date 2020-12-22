import smtplib #simple mail transfer protocol 
import speech_recognition as rec
#import pyttsx3   # for speech to text it will talk to us
from email.message import EmailMessage #this module imports the formate of the email

listener = rec.Recognizer()
#talker = pyttsx3.init()
#function for talking   in place of print you can use 'talk'
#def talk(text):
   # talker.say(text)
   # talker.runAndWait()

def get_text():
    try:
        with rec.Microphone() as source:
            print('listening...')
            sound=listener.listen(source)
            information = listener.recognize_google
            print(information)
            return information.lower()
    except:
        pass

def send_mail(receiver,subject,content):
    server=smtplib.SMTP('smtp.domain_name',port_number)
    server.starttls()
    server.login('sender mail','sender mail password')
    #make sure you enabled the less secure app access
    email = EmailMessage()
    email['From'] = 'sender mail '
    email['To'] = receiver
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email)


email_list= {
    #you can add list of mails or from the files method
    #example 
    'test' : 'test@email.com'
}

def mail_send_info():
    #you can add another module and make it talk back to you 
    print('say the list or batch that u want to send or u can add excel sheet to it like using file opening method)
    listname = get_text()
    receiver =email_list[listname]
    print('the subject of your email')
    subject =get_text()
    print('content of the mail')
    content = get_text()
    send_mail(receiver,subject,content)
    print('your email is sent')
    print('do you want me to send more emails')
    send_more_mails =get_info()
    if 'yes' in send_more_mails:
        mail_send_info()


mail_send_info()
