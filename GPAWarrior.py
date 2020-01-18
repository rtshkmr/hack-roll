import requests
from bottle import (  
    run, post, response, request as bottle_request
)
import json

with open('api.json', 'r') as f:
        datastore = json.load(f)
        datastore = datastore['GPAWarriorAPI']
BOT_URL = 'https://api.telegram.org/bot'+ datastore +'/' # <--- add your telegram token here; it should be like https://api.telegram.org/bot12345678:SOMErAn2dom/


def command(data):
    try:
        replyMessage = data['message']['reply_to_message']
        print(replyMessage)
        answer = 'it is a reply message'
        chat_id = get_chat_id(data)
        json_data = {
                "chat_id": chat_id,
                "text": answer,
            } 
        return json_data

    except:
        userInput = data['message']['text']
        if userInput == '/start':
            answer = "My oh my... So you think you think you're good enough to be a GPA Warrior\nUse /savealife to start"
            chat_id = get_chat_id(data)
            json_data = {
                "chat_id": chat_id,
                "text": answer,
            } 
            return json_data
        
        elif userInput == '/savealife':
            answer = "Input the modules you think you're good at in the following format: \nCS2040\nCS2030\nMA1101R "
            chat_id = get_chat_id(data)
            json_data = {
                "chat_id": chat_id,
                "text": answer,
            }
            return json_data
        
        elif len(userInput) <= 6:
            answer="Modules Inputed"
            chat_id = get_chat_id(data)
            json_data = {
                "chat_id": chat_id,
                "text": answer,
            }
            return json_data
        
def get_chat_id(data):  
    """
    Method to extract chat id from telegram request.
    """
    chat_id = data['message']['chat']['id']

    return chat_id


def get_message(data):  
    """
    Method to extract message id from telegram request.
    """
    message_text = data['message']['text']
    return message_text
def send_message(prepared_data):  
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """ 
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)  # don't forget to make import requests lib

@post('/')
def main():  
    data = bottle_request.json
    print(data)
    answer_data = command(data)
    send_message(answer_data)  # <--- function for sending answer
    return response  # status 200 OK by default

if __name__ == '__main__':  
    run(host='localhost', port=8080, debug=True)

