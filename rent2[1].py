from datetime import datetime
a=[]
def rent():
    rentdic = {}
    print("----------------------------lets rent a coustume-----------------------------------------")
    count = 0
    print("_________________________________________________________________________________________")
    print("ID \t Name \t Brand \t Price \t quantity")
    print("_________________________________________________________________________________________")
    
    file = open("costume.txt","r")
    rentdata = file.read()
    rentdata = rentdata.split("\n")

    while "" in rentdata:
        rentdata.remove("")

    for i in range(len(rentdata)):
        count = count + 1
        rentdic[count] = rentdata[i].split(",")

    for key, value in rentdic.items():
        print(key,end = "\t")
        for i in value:
            print(i,end = "\t")
        print("\n")

    
    try:
        done = False
        while done == False:
            option = int(input("enter ID to choose the costume: "))
            if option>0 and option<=count:
                print("cloth is ready to rent")
                qty = int(input("enter the amount of quantity you want to rent: "))
                validation(count,rentdic,qty,option)
                done ==True
                
            else:
                print("PLEASE ENTER A VALID VALUE")
                rent()
    except:
        print("enter correct value")
        rent()

def validation(count,rentdic,qty,option): 
    selected_item = rentdic[option]

    if int(selected_item[3]) >= qty:
        print("cloth is avialable")
        update_qty = str(int(selected_item[3])-qty)
        selected_item[3] = update_qty
        a.append([selected_item[0],selected_item[1],selected_item[2], str(qty),str(int(selected_item[2].strip().strip("$"))*qty)])
        print(rentdic)
        update(rentdic)

        loop = False
        while loop == False:
            reask = input("Do you want to rent another costume (y/n): ")
            if reask.upper() == "Y":
                loop = True
                rent()
            elif reask.upper() == "N":
                    name = input("enter your user id")
                    billrent(name)
                    loop = True
                    print("thanks")
##                    again = input("do you want to exit")
##                    if again.upper() == "Y":
##                        quit()
                        
##                    elif again.upper() == "N":
                    import main
                    main.firstview()
##                    else:
##                        print("enter right value")


                    

            else:
                print("invalid input")
                
            
    else:
        print("the enter amount is greater then in the stock")

def update(rentdic):
    f = open("costume.txt","w")
    for value in rentdic.values():
        f.write(",".join(value))
        f.write("\n")
    f.close()


def billrent(name):
    print("===========================================================================================================")
    print("Name: ", name,"\t\t\t\t\t\t\t",datetime.now())
    print("===========================================================================================================")
    print("Costumes  \t\t  brand \t\t  Quantity  \t\t  price \t\t  Amount")
    print("===========================================================================================================")
    for i in a:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[3],"\t\t\t",i[2],"\t\t\t",i[4])                     
        print("==========================================================================================================")
        total = 0

    for i in a:
        total = total + int(i[4])
    
        bill(name)
        loop = True
    print("total = ", total)
    return print("Bill has been printed")

    


        
def bill(name):
    loop = open(name,"w")
    loop.write(str("--------------------------------------------------------------------"))
    loop.write("\n")
    loop.write("name:" + name )
    loop.write("\n")
    loop.write("--------------------------------------------------------------------")
    loop.write("\n")
    loop.write("Costumes  \t\t  brand \t\t  Quantity  \t\t  price \t\t Amount")
    loop.write("\n")
    loop.write("--------------------------------------------------------------------")
    loop.write("\n")
    for i in a:
        loop.write(i[0]+"\t\t"+  i[1]+"\t\t"+ i[3]+"\t\t\t"+ i[2]+"\t\t\t"+ i[4])
        loop.write("\n")
    total = 0
    for i in a:
        total = total + int(i[-1])
    loop.write("\n--------------------------------------------------------------------\n")
    loop.write("total = " + str(total))




    




