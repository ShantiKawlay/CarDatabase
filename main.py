# Assignment #3
# INF1340 Section 1
# Fall-2017
# Shanti Kawlay


def load_data(file, inventory, records):
    '''(file open for reading, dict of {str: list of str}, list) -> None
    
    Loads all the data from the input file into	the dictionary (inventory) and
    the	records	list (records)
    
    Example:
    file:-
    
    #This is the beginning of file
    Fog Lights,ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1
    #This is the end of file
    
    >>> load_data(file, {}, [])
    >>> inventory
    {'Fog Lights':[ZN3EU]}
    >>> records
    [[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1]]
    
    '''
    #loop through all the lines of file
    for line in file.readlines():
        
        if not line.startswith('#'): #ignore the lines starting with '#' char      
            
            car_record = line.strip('\n').split(',') #parse data
            accessory = car_record.pop(0)
            car_record[6] = int(car_record[6])
            records.append(car_record)
            
            if accessory in inventory: #add record
                
                inventory[accessory].append(car_record[0])
            
            else:
                
                inventory[accessory] = [car_record[0]]



def menu(inventory_size):
    '''(int) -> str
    
    This function takes one argument as car invenctory size as an int and returns a str representing the menu selection from the user.
    >>> menu(0)
    Car Inventory Menu
    ==================

    1- Add a Car
    Q- Quit

    Enter your selection: 
    
    >>> menu(1)
    Car Inventory Menu
    ==================

    1- Add a Car
    2- Remove a Car
    3- Find a Car
    4- Show Complete Inventory
    5- Output Inventory to File
    Q- Quit

    Enter your selection: 
    '''
    #Car Inventory menu to let user select actions  
    print("\nCar Inventory Menu")
    print("==================\n")
    print("1- Add a Car")
    
    if inventory_size != 0:
        
        print("2- Remove a Car")
        print("3- Find a Car")
        print("4- Show Complete Inventory")
        print("5- Output Inventory to File")
        
        allowed_options = ["1","2","3","4","5","Q","q"]
    
    else:
        
        allowed_options = ["1","Q","q"]
    
    print("Q- Quit\n")
    option = 0
    
    #loop till user inputs a valid command option
    while option not in allowed_options:
        
        option = str(input("Enter your selection: "))
        
        if option not in allowed_options:
            
            print("Wrong selection, try again!\n\n")
            print("Car Inventory Menu")
            print("==================\n")
            print("1- Add a Car")
            
            if inventory_size != 0:
                
                print("2- Remove a Car")
                print("3- Find a Car")
                print("4- Show Complete Inventory")
                print("5- Output Inventory to File")
            
            print("Q- Quit\n")
                
    return option    



def find_index(records, model_number):
    '''(list, str) -> int
    
    This function searches the car records and returns the index of the car with
    a matching model number, as an int. The function returns -1 if the model number
    is not found.
    
    Example:
    >>> find_index([[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1], [NDAD7,2017,Red,Mazda,MX-5,Sport,3]], "ZN3EU")
    0
    >>> find_index([[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1], [NDAD7,2017,Red,Mazda,MX-5,Sport,3]], "ABCDE")
    -1
    >>> 
    '''
    for i in range(len(records)):
        
        if records[i][0] == model_number:
            return i
    
    return -1    



def add_car(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function adds the key/value pair (accessory and model number) to the inventory	
    and	the car to the list of records if and only if the car is not already part
    of the inventory. If the car is already part of the	inventory, the function	
    asks the user the quantity to be added and increases the current quantity accordingly.
    
    Example:
    >>> add_car({}, [])
    
    Enter the model number: EK13Z
    Enter the car accessory: Heated Seats
    Enter the year: 2003
    Enter the colour: Black
    Enter the make: Chevy
    Enter the model: Silverado
    Enter the body type: Truck
    Enter the quantity: 7

    New car successfully added
    
    >>> add_car({'Heated Seats':[EK13Z]}, [[EK13Z,2003,Black,Chevy,Silverado,Truck,7]])
    
    Enter the model number: EK13Z

    Car already exists in inventory.

    Enter the quantity to be added: 2
    Increased quantity by 2. New quantity is: 9

    >>> 
    '''
    print(" ")
    model_number = str(input("Enter the model number: "))
    index = find_index(records, model_number)
    
    #index is -1 if car not found in records
    if index == -1:
        
        accessory = str(input("Enter the car accessory: "))
        year = int(input("Enter the year: "))
        color = str(input("Enter the colour: "))        
        make = str(input("Enter the make: "))
        model = str(input("Enter the model: "))
        body_type = str(input("Enter the body type: "))
        quantity = int(input("Enter the quantity: "))
        
        row = [model_number, year, color, make, model, body_type, quantity] #created row for records
        records.append(row) #add row
        
        if accessory in inventory:
            
            inventory[accessory].append(model_number) #appends to existing list
        
        else:
            
            inventory[accessory] = [model_number] #creates a new list
        
        print("\nNew car successfully added\n")
        
    # OR car with model already present. Only increment quantity
    else:
        
        print("\nCar already exists in inventory.\n")
        quantity = int(input("Enter the quantity to be added: "))
        records[index][6] += quantity
        print("Increased quantity by "+str(quantity)+". New quantity is: "+str(records[index][6])+"\n")



def remove_car(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function removes a car from the inventory (i.e., removes the model number
    for	a given	accessory) and from the	list of	records if and only if the car quantity
    is 1. If the car quantity is greater than 1, it decreases the quantity of the
    car by one. The function will also remove a	key (accessory)	from the inventory
    if and only	if the list of values (model numbers) is empty.
    
    Example:
    >>> remove_car({'Heated Seats':[EK13Z]}, [[EK13Z,2003,Black,Chevy,Silverado,Truck,9]])
     
    Enter the car accessory: Heated Seats
    Enter the model number: EK13Z
    
    \Car quantity is greater than one.
    Decreased quantity by 1. New quantity is:8
    
    >>> remove_car({'Heated Seats':[EK13Z]}, [[EK13Z,2003,Black,Chevy,Silverado,Truck,8]])
    
    Enter the car accessory: Heated Seats
    Enter the model number: ABCDE
    No cars with model number ABCDE for accessory Heated Seats. Cannot remove car!
    
    >>> remove_car({'Heated Seats':[EK13Z]}, [[EK13Z,2003,Black,Chevy,Silverado,Truck,8]])
    
    Enter the car accessory: Fog Lights
    No cars for accessory Fog Lights. Cannot remove car!

    >>> remove_car({'Heated Seats':[EK13Z]}, [[EK13Z,2003,Black,Chevy,Silverado,Truck,1]])
    
    Enter the car accessory: Heated Seats
    Enter the model number: EK13Z

    Car removed from inventory.
    
    >>> 
    '''
    print(" ")
    accessory = str(input("Enter the car accessory: "))
    
    if accessory in inventory:
        
        model_number = str(input("Enter the model number: "))
        index = find_index(records, model_number)
    
        if (index == -1) or (model_number not in inventory[accessory]):
            print("No cars with model number "+str(model_number)+" for accessory "+str(accessory)+". Cannot remove car!\n")
        
            #removes car record if quantity is 1 otherwise decrease quantity
        else:
            
            if records[index][6] == 1: #quantity is one
                
                del records[index]
                inventory[accessory].remove(model_number)
                print("\nCar removed from inventory.\n")
                
                if not inventory[accessory]: #remove dictionary key if value list is empty
                    inventory.pop(accessory, None)
        
            else:
                
                records[index][6] -= 1
                print("\n\Car quantity is greater than one.\nDecreased quantity by 1. New quantity is:"+str(records[index][6])+"\n")
    
    else:
        
        print("No cars for accessory "+str(accessory)+". Cannot remove car!\n")



def find_car(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function searches for a car model number for a	given accessory. If the car
    is part of the inventory, the function prints the car data, tab-delimited on
    one line and the car accessory on the next line.

    Example:
    >>> find_car({'Fog Lights':[ZN3EU]}, [[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1]])
    
    Enter the accessory: Fog Lights
    Enter the model number: ZN3EU


    ZN3EU	2017	Red	Toyota	Prius V	Hatchback	1
    Accessory: Fog Lights


    >>> find_car({'Fog Lights':[ZN3EU]}, [[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1]])
    
    Enter the accessory: Fog Lights
    Enter the model number: ABCDE
    No cars with model number ABCDE for accessory Fog Lights.

    >>> 
    '''    
    accessory = str(input("\nEnter the accessory: "))
    
    if accessory in inventory:
        
        model_number = str(input("Enter the model number: "))
        index = find_index(records, model_number)
        
        if index == -1 or (model_number not in inventory[accessory]):
            
            print("No cars with model number "+str(model_number)+" for accessory "+str(accessory)+".\n")
        
        else:
            
            print("\n")
            print(str(records[index][0])+'\t'+str(records[index][1])+'\t'+str(records[index][2])+'\t'+str(records[index][3])+'\t'+str(records[index][4])+'\t'+str(records[index][5])+'\t'+str(records[index][6]))
            print("Accessory: "+str(accessory)+"\n")
    else:
        
        print("No cars for accessory "+str(accessory)+".\n")



def show_inventory(inventory, records):
    '''(dict of {str: list of str}, list) -> None
    
    This function prints all the cars for every	accessory, tabdelimited, one car per line.
    
    Example:
    >>> show_inventory({'Fog Lights':[ZN3EU], 'Heated Seats':[EK13Z, SU81X]} , [[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1], 
    [EK13Z,2003,Black,Chevy,Silverado,Truck,8], [SU81X,2013,White,Hyundai,Santa Fe,SUV,10]])
    
    Complete Inventory:
    ==================
    
    Fog Lights:
    ----------
    ZN3EU	2017	Red	Toyota	Prius V	Hatchback	1
    
    Heated Seats:
    ------------
    EK13Z	2003	Black	Chevy	Silverado	Truck	8
    SU81X	2013	White	Hyundai	Santa Fe	SUV	10
    
    >>> 
    '''
    print("\nComplete Inventory:")
    print("==================\n")
    
    #loop through all accessories
    for key in inventory:
        
        print(str(key)+":")
        
        #underline should fit the accessory word length 
        for x in range(len(key)):
            print('-', end='')
        
        print("")
        
        #print car records per accessory
        for model_no in inventory[key]:
            index = find_index(records, model_no)
            print(str(records[index][0])+'\t'+str(records[index][1])+'\t'+str(records[index][2])+'\t'+str(records[index][3])+'\t'+str(records[index][4])+'\t'+str(records[index][5])+'\t'+str(records[index][6]))
        
        print("")



def output_inventory(file, inventory, records):
    '''(file open for writing, dict of {str: list of str}, list) -> None
    
    This function outputs all the cars for every accessory, tab-delimited, one 
    car per line to the	output file.
    
    Example:
    >>> output_inventory(file, {'Fog Lights':[ZN3EU], 'Heated Seats':[EK13Z, SU81X]} , [[ZN3EU,2017,Red,Toyota,Prius V,Hatchback,1], 
    [EK13Z,2003,Black,Chevy,Silverado,Truck,8], [SU81X,2013,White,Hyundai,Santa Fe,SUV,10]])
    
    >>> 
    
    output.txt : 
    Complete Inventory: 
    ==================

    Fog Lights:
    ----------
    ZN3EU	2017	Red	Toyota	Prius V	Hatchback	1
    
    Heated Seats:
    ------------
    EK13Z	2003	Black	Chevy	Silverado	Truck	8
    SU81X	2013	White	Hyundai	Santa Fe	SUV	10
    
    
    '''
    #write to file
    file.write("Complete Inventory: \n")
    file.write("==================\n\n")
    
    for key in inventory:
        file.write(str(key)+":")
        
        file.write('\n')
        #underline should fit the accessory word length
        for x in range(len(key)):
            file.write('-')
            
        file.write('\n')
        
        for model_no in inventory[key]:
            index = find_index(records, model_no)
            file.write(str(records[index][0])+'\t'+str(records[index][1])+'\t'+str(records[index][2])+'\t'+str(records[index][3])+'\t'+str(records[index][4])+'\t'+str(records[index][5])+'\t'+str(records[index][6]))
            file.write('\n')
            
        file.write("\n")



#Starter main Program

car_inventory = {} #initialize empty dictionary for car_inventory 
records = [] #initialize empty list for records 

file = open('a3.csv','r')
load_data(file, car_inventory, records)
file.close()

option = 0

#loop till user enters Q or q
while option not in ['Q','q']:
    
    #menu takes user command and returns as option
    option = menu(len(car_inventory))
    
    if option == "1":
        add_car(car_inventory, records)
        
    elif option == "2":
        remove_car(car_inventory, records)
        
    elif option == "3":
        find_car(car_inventory, records)
        
    elif option == "4":
        show_inventory(car_inventory, records)
        
    elif option == "5":
        file = open('output.txt','w')
        output_inventory(file, car_inventory, records)
        file.close()
        
print("Goodbye!")

#End of Program    
