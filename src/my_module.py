import math

class Client:
    def __init__(self,SAP):
        if SAP == 'Regular':
            self.fidelity = False
        elif SAP == 'Rewards':
            self.fidelity = True
        else:
            raise Exception("invalid") 

    def hasFidelity(self):
        return self.fidelity   


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
    
    def dailyValue(self, client, dayOfWeek):
        if dayOfWeek in ["mon", "tues", "wed", "thur", "fri"]:
            if client.hasFidelity():
               return self.weekValueFidelity
            return self.weekValue 
        elif dayOfWeek in ["sat", "sun"]:
            if client.hasFidelity():
                return self.weekendValueFidelity
            return self.weekendValue
        else:
            raise Exception("Invalid day of week: " + dayOfWeek)



def get_cheapest_hotel(input):   #DO NOT change the function's name
    checkIn = input.split(':')
    client = Client(checkIn[0])

    lakewood = Hotel('Lakewood', 3, 110, 80, 90, 80)
    bridgewood = Hotel('Bridgewood', 4, 160, 110, 60, 50)
    ridgewood = Hotel('Ridgewood', 5, 220, 100, 150, 40)
    hotels = [lakewood, bridgewood, ridgewood]

    hotelPrices = {
        hotels[0]:[],
        hotels[1]:[],
        hotels[2]:[],
    }

    daysOfWeek = checkIn[1].split(',')
    for unformatedDay in daysOfWeek:
        dayOfWeek = unformatedDay[unformatedDay.find("(")+1:unformatedDay.find(")")]
        for hotel in hotels:
            prices = hotelPrices[hotel]
            priceForDay = hotel.dailyValue(client, dayOfWeek)
            prices.append(priceForDay)
            hotelPrices[hotel] = prices
    
    bestPrice = math.inf
    bestHotel = hotels[0]

    for hotel in hotels:
        prices = hotelPrices[hotel]
        totalPrice = sum(prices)
        if totalPrice < bestPrice:
            bestPrice = totalPrice
            bestHotel = hotel
        elif totalPrice == bestPrice and hotel.getClassification() > bestHotel.getClassification():
            bestHotel = hotel
    
    return bestHotel.getName() 
