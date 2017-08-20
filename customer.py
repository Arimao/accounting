# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:32:06 2017

@author: greenerworld
"""
import pprint, customersInfoSaved, datetime, pandas
from datetime import timedelta

customers = customersInfoSaved.allCustomerData
foodAmountTable = customersInfoSaved.allFoodAmountData
customerOtherInfos = customersInfoSaved.allOtherCustomerData

def add_customer():
    customerNameTemporary = input("Name: ")
    for x in customers.keys():
        if x == customerNameTemporary:
            print('This name already exists. Please try again.')
            return add_customer()
    customerOwedTemporary = input("Owed: ")
    customerPaidTemporary = input("Paid: ")
    customerStartingYear = input("Year: ")
    customerStartingMonth = input('Month :')
    customerStartingDay = input('Day: ')
    customerFoodAmount = input('Amount: ')
    customerFoodPriceTemp = input('Price: ')
    customers[customerNameTemporary] = {}
    customers[customerNameTemporary]['owed'] = {}
    customers[customerNameTemporary]['owed'][datetime.datetime(int(customerStartingYear), int(customerStartingMonth) ,int(customerStartingDay), int('{d.hour}'.format(d=datetime.datetime.now())), int('{d.minute}'.format(d=datetime.datetime.now())), int('{d.second}'.format(d=datetime.datetime.now())))] = customerOwedTemporary
    customers[customerNameTemporary]['paid'] = {}
    customers[customerNameTemporary]['paid'][datetime.datetime(int(customerStartingYear), int(customerStartingMonth) ,int(customerStartingDay), int('{d.hour}'.format(d=datetime.datetime.now())), int('{d.minute}'.format(d=datetime.datetime.now())), int('{d.second}'.format(d=datetime.datetime.now())))] = customerPaidTemporary
    foodAmountTable[customerNameTemporary] = {}
    foodAmountTable[customerNameTemporary][datetime.date(int(customerStartingYear), int(customerStartingMonth) ,int(customerStartingDay))] = customerFoodAmount
    customerOtherInfos[customerNameTemporary] = {}
    customerOtherInfos[customerNameTemporary][datetime.date(int(customerStartingYear), int(customerStartingMonth) ,int(customerStartingDay)) - timedelta(days=1)] = customerFoodPriceTemp
    saveToFile()
    return

def net_owed(customerName):
    customerNetOwed = 0
    for x in customers[customerName]['owed'].values():
        customerNetOwed += float(x)
    for x in customers[customerName]['paid'].values():
        customerNetOwed -= float(x)
    print(round(customerNetOwed, 2))
    return

def dates_between(start_date, end_date):
    delta = end_date - start_date
    for x in range(delta.days+1):
        y = start_date + timedelta(days=x)
        print(y.strftime('%d/%m/%Y'))
        
def createNewDates():
    for x in foodAmountTable.keys():
        maxi = max(foodAmountTable[x].keys())
        if foodAmountTable[x][maxi] != '':
            temp = maxi + timedelta(days=1)
            foodAmountTable[x][temp] = ''
    saveToFile()
    return

def saveToFile():
    customersInfoSaved = open('customersInfoSaved.py', 'w')
    customersInfoSaved.write('import datetime')
    customersInfoSaved.write('\nallCustomerData = ' + pprint.pformat(customers))
    customersInfoSaved.write('\nallFoodAmountData = ' + pprint.pformat(foodAmountTable))
    customersInfoSaved.write('\nallOtherCustomerData = ' + pprint.pformat(customerOtherInfos))
    customersInfoSaved.close()
    return

def foodTable():
    print(pandas.DataFrame(foodAmountTable).T.fillna('--'))
    return

def xd():
    return 'wtf'

def cutOffAccount(customerName):
    temp = 0
    customerStartingYear = input("YearS: ")
    customerStartingMonth = input('MonthS: ')
    customerStartingDay = input('DayS: ')
    customerEndingYear = input("YearE: ")
    customerEndingMonth = input('MonthE: ')
    customerEndingDay = input('DayE: ')
    customerStartingDate = datetime.date(int(customerStartingYear), int(customerStartingMonth) ,int(customerStartingDay))
    customerEndingDate = datetime.date(int(customerEndingYear), int(customerEndingMonth) ,int(customerEndingDay))
    while customerStartingDate != customerEndingDate + timedelta(days=1):
        basePriceDate = max(customerOtherInfos[customerName])
        for x in range(len(customerOtherInfos[customerName].keys()) - 1,-1,-1):
            if basePriceDate > customerStartingDate:
                basePriceDate = list(customerOtherInfos[customerName])[x]
        try:
            temp += float(foodAmountTable[customerName][customerStartingDate]) * float(customerOtherInfos[customerName][basePriceDate])
        except(KeyError):
            pass
        customerStartingDate += timedelta(days=1)
        print(str(customerStartingDate) + 'alo')
    return temp
    
def customerTable(customerName):
    print(customerName.center(20))
    for x, y in foodAmountTable[customerName].items():
        basePriceDate = max(customerOtherInfos[customerName])
        for z in range(len(customerOtherInfos[customerName].keys()) - 1,-1,-1):
            if basePriceDate > x:
                basePriceDate = list(customerOtherInfos[customerName])[z]
        totalDailyPrice = float(y) * float(customerOtherInfos[customerName][basePriceDate])
        print(str(x).ljust(10) + y.rjust(10) + str(customerOtherInfos[customerName][basePriceDate]).rjust(10) + str(totalDailyPrice).rjust(10))
