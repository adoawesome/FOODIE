import random #to choose random values
import math #for calculations
import csv #to read and write data

#the csv file where the data is stored
path="C:\Users\Van-Ado Jean-Noel\Desktop\FoodData.csv"


food_list=[] #has the location on the memory of all the foods, (unintelligible)
name_list=[] #has the list of foods in english

#lists for reference, no real use in the code
dining_hall_list=["lower","mac","rat","eagles nest","stuart","chocolate bar","hillside","addies"]
meal_list=["breakfast","lunch","dinner","late night"]
fooddescription=["name_of_food","dining_hall","meal","liquid_or_solid","elo"]

#defines the class "food"
#every food has the properties
#name - the name of the food
#dining hall - the dining hall the food is served in
#meal - the meal it's offered during 
#foodstate - whether it's a solid or a liquid
#elo - the elo rating of the food
class food:
    def __init__(self,name,dining_hall,meal,foodstate,elo):
        self.name=name
        self.dining_hall=dining_hall
        self.meal=meal
        self.foodstate=foodstate
        self.elo=elo
        food_list.append(self)
        name_list.append(self.name)
        
#defining some foods - all start with an elo of 1000
#regular_mac_pizza=food("regular_mac_pizza","mac","lunch","solid",1000)
sicilian_mac_pizza=food("sicilian_mac_pizza","mac","lunch","solid",1000)
flatbread_pizza=food("flatbread_pizza","addies","late night","solid",1000)

#reads the foods from the CSV file
file=open(path)
for line in file:
    print(line)

dataset=[line.strip().split(",") for line in open(path)]
del(dataset[0])
print dataset
print dataset[1][0]

for item in dataset:
    newfood=food(item[0],item[1],item[2],item[3],int(item[4]))



#some commands for testing
#print regular_mac_pizza.name
#print food_list
#print name_list

#asks the user what food they prefer
def promptuser():
    random2=random.sample(food_list, 2)
    randoma=random2[0]
    randomb=random2[1]
    
    print "Which food is better?"
    
    print randoma.name

    print "or"
    
    print randomb.name

    "enter a or b please"
    userchoice=raw_input("")

    userchoice=int(userchoice)
    
    if userchoice == 1:
        elodecision(randoma,randomb)
        
    elif userchoice == 2:
        elodecision(randomb,randoma)

    else:
        print "that is not a valid option"


#calculates how the points will change after a preference is selected
def elodecision(winningfood,losingfood):

    transformedratingr1=10.0**(winningfood.elo/400.0)
    transformedratingr2=10.0**(losingfood.elo/400.0)
    
    expectedscoree1=(transformedratingr1)/(transformedratingr1+transformedratingr2)
    expectedscoree2=(transformedratingr2)/(transformedratingr1+transformedratingr2)

    winningfood.elo=winningfood.elo+(420*(1.0-expectedscoree1))
    losingfood.elo=losingfood.elo-(420*(0.0+expectedscoree2))

    winningfood.elo=int(winningfood.elo)
    losingfood.elo=int(losingfood.elo)
    print winningfood.name,winningfood.elo,losingfood.name,losingfood.elo


promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()
promptuser()



