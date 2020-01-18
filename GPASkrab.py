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

class GPASkrab(BotHandlerMixin, Bottle):
    with open('api.json', 'r') as f:
        datastore = json.load(f)
        datastore = datastore['GPASkrabAPI']
        print('test')
    BOT_URL = 'https://api.telegram.org/bot'+datastore+'/'

    def __init__(self, *args, **kwargs):
        super(GPASkrab, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")
    mod = 0
    ques = 0
    def prepare_data_for_answer(self, data):
        message = self.get_message(data)
        chat_id = self.get_chat_id(data)
        if(message== "/start" or message ==  "hi"):
            print ("constraint: /start but this is "+ message)
            answer = "Hi skrub, what do you wish to do \n/Ask to ask a question or /Answer to answer a question"

        elif (message=="/Ask" or message ==  "/ask"):
            answer = "Hi skrub, what mod are you asking help for? (example:/ CS2030)"

        elif (message=="/Answer" or message ==  "/answer"):
            answer = "Hi warrior, what mod can you save ass in? (example: CS2030)"
        elif(len(message)<8):
            mod = message
            json_data = requests.get('https://buttend.herokuapp.com/api/questions.json').json()
            print(len(json_data))
            for entry in json_data:
                entry['answer_body'] = data['message']['text']
            print(json_data[0])
            item_id =  '1'
            print(item_id)
            url_ = 'https://buttend.herokuapp.com/api/questions/'+item_id+'.json'
            requests.patch(url= url_,json = json_data[0])    
            print('post successful') 

            
            answer = "Okay noted that is an easy mod but oh well... submit your question(min 8 char)"
        else:
            ques = message
            answer = "Cool we have sent it to the GPA Warriors they will take care of it. In the mean time buck up"
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
    app = GPASkrab()
    app.run(host='localhost', port=8080, debug=True)