
# make a class object for the warehouse
#the attributes known is that is has a name and items paired with values, a dictionary would make the most sense since its easily accessible and mutable
class Inventory:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def setStock(self, item, n):
        self.stock[item] = n

    def isOutofStock(self, item):
        if(self.stock[item] == 0):
            return True
        else:
            return False

#function to make tuples to represent the input, I am assuming they're tuples since they're a pair of values.
def makeItem(item, amount):
    return((item,amount))

#PROVIDED TEST CASES   

#TEST CASE 1 -- Expected out: ['owd', ('apple', 1)]
items = ['apple']
amounts = [1]
obj1 = Inventory('owd', {'apple':1})
warehouses = [obj1]

#TEST CASE 2 -- Expected out: [] empty list
# items = ['apple']
# amounts = [1]
# obj1 = Inventory('owd', {'apple':0})
# warehouses = [obj1]

#TEST CASE 3 -- Expected out: [{'dm', {'apple':5}} {'owd'}]
# items = ['apple']
# amounts = [10]
# obj1 = Inventory('owd', {'apple' : 5})
# obj2 = Inventory('dm', {'apple' : 5})
# warehouses = [obj1, obj2]

#TEST CASE 4
# items = ['apple', 'banana', 'orange']
# amounts = [5,5,5]
# obj1 = Inventory('owd', {'apple' : 5, 'orange':10})
# obj2 = Inventory('dm', {'banana' : 5, 'orange' : 10})
# warehouses = [obj1, obj2]

#makes a map of items
request = map(makeItem, items, amounts)


# Here begins the actual problem
# the goal of this function is to take a request and a list of warehouse objects, check each warehouse to see if the warehouse has what the order wants
# and print out the name of the warehouse, and the contents being taken from each

# Input: map of tuples w/ string int pairs, and a list of warehouse objects
# Returns list of warehouse objects w/ number being removed from each warehouse, warehouse's inventory are updated upon request
def picker(input1, input2):
    #turn the map into a list so I can iterate through
    listOfItems = list(input1)

    #looks like the output is another list of objects with then number of items being taken from each warehouse
    output = []
    #iterate over the warehouses, then check each warehouse if it contains whats in the request
    for warehouse in input2:
        nameOfWarehouse = warehouse.name
        itemsGoingOut = []

        for item in listOfItems:
            # make a list of tuples of the items being taken out of the warehouse
            # check if the warehouse has that item, and if the warehouse is out of stock on it

            # item[0] represents the name of the item, item[1] represents the value associated
            if (item[0] in warehouse.stock):
                if(not warehouse.isOutofStock(item[0])):
                    # if so, then remove that number of items from the warehouse and the request
                    # print(warehouse.stock[item[0]] - item[1])
                    # update the warehouse amount
                    numberInStock = warehouse.stock[item[0]]
                    # check if the warehouse has enough
                    if(numberInStock >= item[1]):
                        
                        warehouse.setStock(item[0], numberInStock - item[1])
                        itemsGoingOut.append((item[0], item[1]))
                        #remove that item from the list since it has been fulfilled
                        listOfItems.remove(item)

                    else:
                        #say the requested number is greater than the number in the warehouse
                        #so i should probably set the warehouse stock to 0 and update the number in the request, and pop it back in the list?
                        warehouse.setStock(item[0], 0)
                        itemsGoingOut.append((item[0], item[1] - numberInStock))

                        # item[1] = item[1] - numberInStock, tuples are immutable, so this wont work, so make a new item and pop it on the list with the updated value
                        listOfItems.remove(item)
                        listOfItems.append(makeItem(item[0], item[1] - numberInStock))
        #end of item loop
        #return a list of objects
        print(nameOfWarehouse)
        print(itemsGoingOut)

        #turn list of tuples into a dictionary
        objDict = {}
        for i in itemsGoingOut:
            objDict.update({i[0] : i[1]})
        
        #create object to append to list
        outputObj = Inventory(nameOfWarehouse, objDict)
        output.append(outputObj)
    #end of warehouse loop
    return output

#call the function
picker(request, warehouses)

