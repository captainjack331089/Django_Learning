import random

def productIdGenerate():

    productidpool = []
    for i in range(20000):
        productidpool.append(random.randint(1,20000))
    return productidpool

def supremeIdGenerate():

    productidpool = []
    for i in range(20000):
        productidpool.append(random.randint(20000,40000))
    return productidpool

def sneakerSize():
    sizepool = [7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17,17.5,18]
    l = len(sizepool)
    size = sizepool[random.randint(0,l-1)]

    return size

def supremesize():
    sizepool = ['S','M','L','XL']
    l = len(sizepool)
    size = sizepool[random.randint(0, l - 1)]

    return size
