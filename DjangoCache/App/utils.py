import random


def get_color():
    return random.randrange(256)

def generate_code():
    source  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ01234567890'
    code = ""
    for i in range(4):
        code += random.choice(source)


    return code