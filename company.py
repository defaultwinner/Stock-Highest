import sys
import os
import csv
import urllib2
import unittest

def getHighestPrices(file):
    with open(file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        stock_highest = {}                      # Dictionary containing Highest Stock prices for companies 
        company_list = []

        i = 0
        
        for row in reader:
            if i==0:                            #Initializing the dictionary
                for col in list(row)[2:]:
                    stock_highest[col] = {'price':0}
                    company_list.append(col)
            else:
                prices = list(row)[2:]
                for n in xrange(len(prices)):
                    try:
                        if stock_highest[company_list[n]]['price'] < float(urllib2.unquote(prices[n])):
                            stock_highest[company_list[n]]['price'] = float(urllib2.unquote(prices[n]))
                            stock_highest[company_list[n]]['year'] = list(row)[0]
                            stock_highest[company_list[n]]['month'] = list(row)[1]
                    except Exception,e:
                        print e
                        pass
            i += 1
        return stock_highest


if __name__ =='__main__':
    file = sys.argv[1]
    stock_highest = getHighestPrices(file)
    print stock_highest
