# -*- coding: utf-8 -*-

from productinfo import productIdGenerate, sneakerSize
from stockx import StockXAPI
import random

from StockxResource.productinfo import supremesize, supremeIdGenerate, supremePantsIdGenerate, HoodieIdGenerate, \
    JacketIdGenerate, HatIdGenerate

stockx = StockXAPI()

datacmd = "insert into aaa_goods(productid,productimg,productname,productlongname,isaaa,pmdesc,specifics,price," \
          "marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("

def sneakers():
    file1 = open('data.txt', 'w')
    sneakers = stockx.search_items('jordan',output_data=['name', 'retailPrice', ['market', 'lastSale'], ['media', 'smallImageUrl']])

    for sneaker in sneakers:
        product_id_poll = productIdGenerate()  # a list with all product id
        file1.write(datacmd)

        n = sneakers.index(sneaker)
        productid = product_id_poll[n]

        imgurl = sneaker['smallImageUrl']

        name = sneaker['name']

        size = sneakerSize()

        retail_price = sneaker['retailPrice']
        market_price = sneaker['lastSale']

        file1.write("\"" + str(productid) + "\"" + "," + "\"" + str(imgurl) + "\"" + "," + "\"" + str(name) + "\"" + "," + "\"" + str(name) + "\"" + "," + "0" + "," + "0" + "," + "\"" + str(size) + "\"" + "," + str(retail_price) + "," + str(market_price) + "," + "103541" + "," + "103543" + "," + "\"" + "sneakers" + "\"" + "," + "\"" + "4858" + "\"" + "," + "200" + "," + "5" + ");")
        file1.write("\n")
        file1.write("\n")
    file1.close()

def supreme_test():
    file2 = open('data2.txt', 'w')
    supremes = stockx.search_items('supreme',output_data=['name', 'retailPrice', ['market', 'lastSale'], ['media', 'smallImageUrl']])

    for supreme in supremes:
        product_id_poll = supremeIdGenerate()  # a list with all product id
        file2.write(datacmd)
        n = len(supremes)
        productid = product_id_poll[n]

        imgurl = supreme['smallImageUrl']

        name = supreme['name']

        size = supremesize()

        retail_price = supreme['retailPrice']
        market_price = supreme['lastSale']

        file2.write("\"" + str(productid) + "\"" + "," + "\"" + str(imgurl) + "\"" + "," + "\"" + str(
            name) + "\"" + "," + "\"" + str(name) + "\"" + "," + "0" + "," + "0" + "," + "\"" + str(
            size) + "\"" + "," + str(retail_price) + "," + str(
            market_price) + "," + "103541" + "," + "103543" + "," + "\"" + "supreme" + "\"" + "," + "\"" + "4858" + "\""
                    + "," + "200" + "," + "5" + ");")
        file2.write("\n")


def supreme_pants():
    file2 = open('data3.txt', 'w')
    supremes = stockx.search_items('supreme pants', output_data=['name', 'retailPrice', ['market', 'lastSale'],
                                                           ['media', 'smallImageUrl']])

    for supreme in supremes:
        product_id_poll = supremePantsIdGenerate()  # a list with all product id
        file2.write(datacmd)
        n = len(supremes)
        productid = product_id_poll[n]

        imgurl = supreme['smallImageUrl']

        name = supreme['name']

        size = supremesize()

        retail_price = supreme['retailPrice']
        market_price = supreme['lastSale']

        file2.write("\"" + str(productid) + "\"" + "," + "\"" + str(imgurl) + "\"" + "," + "\"" + str(
            name) + "\"" + "," + "\"" + str(name) + "\"" + "," + "0" + "," + "0" + "," + "\"" + str(
            size) + "\"" + "," + str(retail_price) + "," + str(
            market_price) + "," + "103541" + "," + "103543" + "," + "\"" + "supreme" + "\"" + "," + "\"" + "4858" + "\""
                    + "," + "200" + "," + "5" + ");")
        file2.write("\n")
    file2.close()




def hoodie():
    file2 = open('data6.txt', 'w')
    hoodies = stockx.search_items('jacket', output_data=['brand', 'name', 'retailPrice', ['market', 'lastSale'],
                                                           ['media', 'smallImageUrl']])

    for hoodie in hoodies:
        product_id_poll = JacketIdGenerate()  # a list with all product id
        file2.write(datacmd)
        n = len(hoodies)
        productid = product_id_poll[n]

        brand = hoodie['brand']
        imgurl = hoodie['smallImageUrl']

        name = hoodie['name']

        size = supremesize()

        retail_price = hoodie['retailPrice']
        market_price = hoodie['lastSale']

        file2.write("\"" + str(productid) + "\"" + "," + "\"" + str(imgurl) + "\"" + "," + "\"" + str(
            name) + "\"" + "," + "\"" + str(name) + "\"" + "," + "0" + "," + "0" + "," + "\"" + str(
            size) + "\"" + "," + str(retail_price) + "," + str(
            market_price) + "," + "103575" + "," + "105555" + "," + "\"" + str(brand) + "\"" + "," + "\"" + "4858" + "\""
                    + "," + "200" + "," + "5" + ");")
        file2.write("\n")
    file2.close()



hoodie()