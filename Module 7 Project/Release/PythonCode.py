import re
import string


def ItemsPurchased():
    f = open('GroceryItems.txt') #Opens grocery items list

    contents = f.read() #Reads GroceryItems, and sets it to "contents"

    items = contents.split()

    itemsBought = [] #List that stores the items bought from the file

    for item in items: #for loop that puts each item in the itemsBought list
        if item not in itemsBought:
            itemsBought.append(item)

    itemsBought.sort() #sorts itemsBought

    for items in itemsBought:
        print(contents.count(items), items) #prints a list with a numerical value for ItemsBought
    

    return 0

def ItemsList():
    f = open('GroceryItems.txt')

    contents = f.read()

    items = contents.split()

    itemsBought = []

    for item in items:
        if item not in itemsBought:
            itemsBought.append(item)

    itemsBought.sort()

    listToStr = '\n'.join(map(str, itemsBought)) #Joins the itemsBought list into a more legible list for the user to see and read

    print(listToStr)

def CertainItem(k):

    f = open('GroceryItems.txt') 
    
    contents = f.read()

    items = contents.split()

    itemsBought = []

    for item in items:
        if item not in itemsBought:
            itemsBought.append(item)

    itemsBought.sort()

    if k in itemsBought:
        print("There were", contents.count(k), k, "purchased today") #Gets the user input from C++ and tells the user how many of that item was purchased on the given day

    if k not in itemsBought:
        print("Invalid Input! That item does not exist or was not purchased today") #User input was not found on list, so returns an error.

    return 0

def Histogram():
    f = open('GroceryItems.txt')
    
    contents = f.read()

    items = contents.split()

    itemsBought = []

    for item in items:
        if item not in itemsBought:
            itemsBought.append(item)

    itemsBought.sort()

    for items in itemsBought: #For loop that displays the items as a histogram, with the "bars" of the histogram represented by an asterisk.
        itemCount = contents.count(items)
        output = ''
        while(itemCount > 0):
            output += '*'
            itemCount -= 1
        print(items.ljust(13), output)





    
