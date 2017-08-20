import datetime
allCustomerData = {'customer1': {'owed': {datetime.datetime(2017, 6, 27, 1, 54, 9): '1000'},
               'paid': {datetime.datetime(2017, 6, 27, 1, 54, 9): '500'}}}
allFoodAmountData = {'customer1': {datetime.date(2017, 1, 3): '10',
               datetime.date(2017, 1, 4): '15'},
 'customer2': {datetime.date(2017, 1, 2): '20',
               datetime.date(2017, 1, 3): '25'},
 'customer3': {datetime.date(2017, 1, 4): '30',
               datetime.date(2017, 1, 5): '35'}}
allOtherCustomerData = {'customer1': {datetime.date(2017, 6, 26): '4.5',
               datetime.date(2017, 6, 28): 3,
               datetime.date(2017, 6, 30): 8}}