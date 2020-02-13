'''This script allows user to send sms to different users using phone number
please enter phone number with country code. For example a Indian phone number is +910000000000'''
import requests
rsep=requests.post('https://textbelt.com/text',{
    'phone': input("Enter phone number"),
    'message': input('Enter message'),
    'key': 'textbelt'
})
if rsep.json()['success']:
    print("Message is sent")
else:
    print("Something went wrong. Please try again")
print(rsep.json())