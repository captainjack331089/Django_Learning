# -*- coding: utf-8 -*-

from productinfo import productIdGenerate, sneakerSize
from stockx import StockXAPI
import random

from StockxResource.productinfo import supremesize, supremeIdGenerate

stockx = StockXAPI()

datacmd = "insert into aaa_goods(productid,productimg,productname,productlongname,isaaa,pmdesc,specifics,price," \
          "marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("



file1 = open('data.txt', 'w')
file2 = open('data2.txt', 'w')

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
    file2.write("\n")
