import requests
from bottle import Bottle, response, request as bottle_request
import json

class BotHandlerMixin:  
    BOT_URL = None

    def get_chat_id(self, data):
        """
        Method to extract chat id from telegram request.
        """
        chat_id = data['message']['chat']['id']

        return chat_id

    def get_message(self, data):
        """
        Method to extract message id from telegram request.
        """
        message_text = data['message']['text']

        return message_text

    def send_message(self, prepared_data):
        """
        Prepared data should be json which includes at least `chat_id` and `text`
        """       
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)

def foo():
    global mod
    global ques

class GPASkrab(BotHandlerMixin, Bottle):
    with open('api.json', 'r') as f:
        datastore = json.load(f)
        datastore = datastore['GPASkrabAPI']
        print('test')
    BOT_URL = 'https://api.telegram.org/bot'+datastore+'/'

    def __init__(self, *args, **kwargs):
        super(GPASkrab, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")
  
    def prepare_data_for_answer(self, data):
        message = self.get_message(data)
        chat_id = self.get_chat_id(data)
        answer = 0
        if(message== "/start" or message ==  "hi"):
            print ("constraint: /start but this is "+ message)
            answer = "Hi skrub, what do you wish to do \n/Ask to ask a question or /Answer to answer a question"
        elif (message=="/Ask" or message ==  "/ask"):
            answer = "Hi skrub, what mod are you asking help for? (input in the following example: #stu CS2030)"
        elif (message=="/Answer" or message ==  "/answer"):
            answer = "Hi warrior, what mod can you save ass in? (example: #tea CS2030)"
        elif (message[:4] == "#stu"):
            mod = message[5:]
            answer = "cool now send the question for "+ mod + " like this #Que i need help"
        elif (message[:4] == "#Ans"):
            Ans = message
            answer = "Thank you warrior you are a champion"
        elif (message[:4] == "#Que" or message[:4] == "#que" ):
            #print(mod)
            ques = message[5:]
            print(ques)
            json_data = {
                "module_code" : mod,
                "question_body": ques,
                "answer_body": "",
                "answered": false,
                "asker_id":data['message']['chat']['id'],
                "created_at":"",
                "updated_at":""
            }
            print(json_data)
            requests.post(url= url_,json = json_data)    
            print('post succeed')
            answer = "Cool we have sent it to the GPA Warriors they will take care of it. In the mean time buck up"
      # if (message[:4]=="#tea"):
            #     answer = "Please help this poor soul, Warrior. Here you go! If you choose to help use #Ans at the front"
            # else:
            #     answer = "Just post your dumb question here you dubfk with the tag #Que at the front"
        elif(len(message[4:])<8 and (message[:4] == '#tea' or message[:4] == '#Tea')):
            mod = message[5:]
            print(mod)
            json_data = requests.get('https://buttend.herokuapp.com/api/questions.json').json()
            for entry in json_data:
                print(entry['module_code']+ ' and '+ mod)
                if entry['module_code'] == mod:
                    DraftMessage = 'Questionid: ' + str(entry['asker_id']) + '\nQuestion:' + entry['question_body']+'\n reply to this message if you want to answer it'
                    print(DraftMessage)
                    chat_id = self.get_chat_id(data)
                    json_data = {
                        "chat_id": chat_id,
                        "text": DraftMessage,
                    } 
                    print(json_data)
                    self.send_message(json_data)
            
                    
        else:
            answer = 'oops'

        json_data = {
            "chat_id": chat_id,
                "text": answer,
        } 
        return json_data

    def post_handler(self):
        data = bottle_request.json
        print(data)
        answer_data = self.prepare_data_for_answer(data)
        self.send_message(answer_data)
        return response

if __name__ == '__main__':  
    foo()
    app = GPASkrab()
    app.run(host='localhost', port=8080, debug=True)