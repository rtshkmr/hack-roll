import requests
import json
from bottle import run, post, response, request as bottle_request



if __name__ == '__main__':  
    app = TelegramBot()
    app.run(host='localhost', port=8080)