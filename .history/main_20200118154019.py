from telegram.ext import Updater, CommandHandler
import requests
import re


# API call to source, get json (url is obtained):
contents = requests.get('https://random.dog/woof.json').json()

image_url = contents['url']

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
    

def get_tasks():
    response = requests.get('https://nowwat.herokuapp.com/api/tasks.json').json()
    def extract_list(obj):
        return obj.map(lambda item: item.title)
    tasks = extract_list(response)
    return tasks

# sending the image:
#    we require:
#       -  the image URL
#       -  the recipient's ID: group/user id

def bop(bot, update):
    # image url:
    url = get_url()
    # recipient's ID:
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    
def getTaskList(bot, update):
    taskList = get_tasks()
    chat_id = update.message.chat_id
    for task in taskList:
        bot.sendMessage(chat_id, task, Markdown);
    
    


def main():
    updater = Updater('982938821:AAHiN0-7hIPahKJm6lWPyQ0UupOsuhP1GsQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()