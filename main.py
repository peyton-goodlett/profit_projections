'''
You will the user to enter the following information:

Total number of items to project profit (Best to keep it between 2 -5)
Item name
Number of items sold by the company for each item
Selling price of each item
Expected percentage of increase each year for number sold 
Expected price increase each year for each items (can be percentage or flat amount)
Number of years the projection should be forecasted.
'''

def profitProj(name, price, numSold, percentIN, priceIN, years):
    projections = []
    initProfit = price * numSold
    for i in range(years):
        numSold *= percentIN
        price *= priceIN
        projections.append(price * numSold)
        
