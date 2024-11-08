import Return
import rent2


def firstview():
    A = False
    while A == False:
        print("------------------------------SELECT A DESIRABLE OPTION TO RENT OR RETURN A CLOTH----------------------------- \n\n (1) Press 1 to rent a costume \n (2) Press 2 to return a costume \n (3) Press 3 to exit" ) 
        first =(input("\n\n     enter an option: ")) 
        if first == "1":
            A = True
            dic0=rent2.rent()
            rent2.validation(len(dic0),dic0)
            print("lets rent")

        elif first == "2":
            print("lets return")
            dic=Return.display()
            
            Return.validation(len(dic),dic)
        elif first == "3":
            print(" Thank you for using my application")
            exit()
            A = False
 
                     
        else:
            print("\n\n Please enter a valid option")

firstview()








    
    
