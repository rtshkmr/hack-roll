import requests
import from bottle import run, post, response, request as bottle_request


if __name__ == '__main__':  
    run(host='localhost', port=8080, debug=True)