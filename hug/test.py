#https://github.com/timothycrosley/hug#why-hug
import hug

@hug.get()
def hello():
    return "hello"


@hug.get('/happy_birthday')
def happ_birthday(name,age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())

@hug.get('/grent/{event}')
def grent(event:str):
    greetings = "Happy"
    if event == "Christmas":
        greetings = "Merry"
    if event == "wishes":
        greetings = "Warm"
    return "{greetings}  {event}!".format(**locals())