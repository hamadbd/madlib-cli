#def read_template(path):
#def parse_template(text):
#def merge()


welcome = """
Hello there ..
in this game you are supposed to guess the right words
you should answer some questioins and based on them we will give you some funny quotes :)
"""


def view_answers(arr):
    print('Make Me A Video Game! I the'+ arr[0]+' and '+arr[0]+ arr[1]+' have '+arr[2]+' '+arr[1]+'s' +arr[0]+ 'sister and plan to steal her '+arr[0]+ ' '+arr[1]+'!')
    print('What are a '+arr[4]+ 'and backpacking ' +arr[5]+ '')


def questions_to_ask():
    print(welcome)
    array = []
    array[0] = input("say an adjective ")
    array[1] = input("pick a first name ")
    array[2] = input("choose a Past Tense Verb ")
    array[3] = input("now time to pick a Plural Noun ")
    array[4] = input("choose a Large Animal ")
    array[5] = input("now a Small Animal ")
    array[6] = input("what girls name should we use ")
    array[7] = input("choose Number 1-50 ")
    while array[7] > 50 or array[7] < 1:
        print("not what we agreed on ,, try again ")
        array[7] = input("choose Number 1-50 ")
    view_answers(array)

questions_to_ask()


