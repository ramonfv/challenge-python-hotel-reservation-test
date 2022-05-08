import math

# Function that assing the expression for fidelity program 
def __hasFidelity__(fidelityProgram):
    if fidelityProgram == 'Regular':
        return False
    elif fidelityProgram == 'Rewards':
        return True
    else:
        raise Exception("Invalid expression for fidelity: " + fidelityProgram)

# The class Hotel have methods for get name of hotel, get classification and get the days od week
class Hotel:
    def __init__(self, name, classification, weekValue, weekValueFidelity,  weekendValue,  weekendValueFidelity):
        self.name = name
        self.classification = classification
        self.weekValue = weekValue
        self.weekendValue = weekendValue
        self.weekValueFidelity = weekValueFidelity
        self.weekendValueFidelity = weekendValueFidelity

    def getClassification(self):
        return self.classification 

    def getName(self):
        return self.name       
    
    def dailyValue(self, fidelity, dayOfWeek):
        if dayOfWeek in ["mon", "tues", "wed", "thur", "fri"]:
            if fidelity:
               return self.weekValueFidelity
            return self.weekValue 
        elif dayOfWeek in ["sat", "sun"]:
            if fidelity:
                return self.weekendValueFidelity
            return self.weekendValue
        else:
            raise Exception("Invalid day of week: " + dayOfWeek)

# function that get the best price for hotel
def get_cheapest_hotel(input):   #DO NOT change the function's name
    
    checkIn = input.split(':')
    fidelity = __hasFidelity__(checkIn[0])

    lakewood = Hotel('Lakewood', 3, 110, 80, 90, 80)
    bridgewood = Hotel('Bridgewood', 4, 160, 110, 60, 50)
    ridgewood = Hotel('Ridgewood', 5, 220, 100, 150, 40)
    hotels = [lakewood, bridgewood, ridgewood]

    hotelPrices = {
        hotels[0]:[],
        hotels[1]:[],
        hotels[2]:[],
    }

# get the days od week and assign the corresponding price
    daysOfWeek = checkIn[1].split(',')
    for beginIndex in daysOfWeek:
        endIndex = beginIndex[beginIndex.find("(")+1:beginIndex.find(")")]
        for hotel in hotels:
            prices = hotelPrices[hotel]
            priceForDay = hotel.dailyValue(fidelity, endIndex)
            prices.append(priceForDay)
            hotelPrices[hotel] = prices
    
    bestPrice = math.inf
    bestHotel = hotels[0]

# sum days of week and return the best value for holtel
    for hotel in hotels:
        prices = hotelPrices[hotel]
        totalPrice = sum(prices)
        if totalPrice < bestPrice:
            bestPrice = totalPrice
            bestHotel = hotel
        elif totalPrice == bestPrice and hotel.getClassification() > bestHotel.getClassification():
            bestHotel = hotel
    
    return bestHotel.getName() 
