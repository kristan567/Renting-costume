from datetime import datetime


returndic = {}
b=[]
def display():

    print("----------------------------lets return a coustume-----------------------------------------")
    count = 0
    print("_________________________________________________________________________________________")
    print("ID \t Name \t Brand \t Price \t quantity")
    print("_________________________________________________________________________________________")
    
    file = open("costume.txt","r")
    returndata = file.read()
    returndata = returndata.split("\n")

    while "" in returndata:
        returndata.remove("")

    for i in range(len(returndata)):
        count = count + 1
        #print(returndata[i].split(","))
        returndic[count] = returndata[i].split(",")


    for key, value in returndic.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")


    return returndic


def validation(count,returndic):
    
    try:
        option = int(input("enter ID to choose the costume: "))
        if option>0 and option<=count:
            print("costume can be returned")
            qty = int(input("enter the amount of quantity you want to return: "))
            selected_item = returndic[option]

            update_qty = str(int(selected_item[3])+qty)    
            selected_item[3] = update_qty
            print("thanks")
                
            print(returndic)
            b.append([selected_item[0],selected_item[1],selected_item[2],str(qty)])          
            print(selected_item)
            
            update_stock()
            returnbill(b,count,returndic)
           
            
        else:
            print("Please enter a valid input")
            display()
    except:
        print("enter coorect value")
        display()


def returnbill(b,count,returndic):
    check = False
    while check == False:
        reask = input("Any other costumes you want to return ?(Y/N): ")
        if reask.upper() == "Y":
            check = True
            display()
            validation(count,returndic)
        elif reask.upper() == "N":
            name = input("enter your name")
            print("---------------------------------------------------------------------------------")
            print("Name: ", name,"\t\t\t\t\t\t\t",datetime.now())
            print("---------------------------------------------------------------------------------")
            print("Costumes  \t\t  Quantity  \t\t  price \t\t" )
            print("---------------------------------------------------------------------------------")
            for i in b:
                print(i[0],"\t\t\t", i[3],"\t\t\t",i[2],"\t\t")
            print("---------------------------------------------------------------------------------")

            notepad(b,name,count)
            check = True
        else:
            print("Invalid input")
            
    
 
    #payamount = latec()
    #print(payamount)
    

def update_stock():
    R= open("costume.txt","w")
    for value in returndic.values():
        R.write(",".join(value))
        R.write("\n")
    R.close()

def late():
    l = False
    while l == False:
        later = str(input("are you late for the return: "))
        if later.upper() == "Y":
            l = True
            latec()
            
        elif later.upper() == "N":
            l = True
            print("thanks for returnig in the time")
            
        else:
            print("invalid input")
            break       
            
        


def notepad(b,name,count):
    ret = open(name,"w")
    ret.write(str("--------------------------------------------------------------------"))
    ret.write("\n")
    ret.write("name: " + name)
    ret.write("\n")
    ret.write("--------------------------------------------------------------------")
    ret.write("\n")
    ret.write("Costumes  \t\t  brand \t\t  Quantity  \t\t  price")
    ret.write("\n")
    ret.write("--------------------------------------------------------------------")
    ret.write("\n")
    for i in b:
        ret.write(i[0] + "\t\t" + i[1] + "\t\t" + i[3] + "\t\t" + i[2] + "\t\t")
        ret.write("\n")
    late()
    payamount = latec()
    ret.write("penalty: "+ str(payamount))

def latec():
    try:
        days = int(input("enter the days you are late"))
        if days >=5:
            payamount = 100
            payamount=payamount +((days-5)*5)


        elif days >= 10:
            payamount = payamount + ((days - 5)* 10)
        else:
            payamount = 0
    except:
        print("enter correct value")
    print("charge amount for late payment: ",payamount)
    print("a bill has been printed")
    import main
    main.firstview()
    return payamount













    
