import os


class CarUI():
    


    def __init__(self,c):
        '''
        Constructor
        '''
        
        self.__controller=c
        
        
    @staticmethod
    def prin_menu():
        print("1.Add a new car.")
        print("2.Increse price by 10%.")
        print("3.Delete cars below given year.")
        print("4.Print cars.")
        print("0.Exit.")
        
    @staticmethod
    def read_nr():
        
        while True:
            
            try:
                nr=int(input())
                break
                
            except Exception as e:
                print("Error:",e)
                
                
        return nr
    
    
    @staticmethod
    def read_st():
        
        while True:
            
            try:
                st=input()
                break
                
            except Exception as e:
                print("Error:",e)
                
                
        return st
    
    
    def menu(self):
        
        self.__controller.start()
        
        while True:
            os.system("cls")
            d=self.__controller.get_all_d()
            g=self.__controller.get_all_g()
            e=self.__controller.get_all_e()
            
            print("Diesel cars:")
            for el in d:
                print(el)
                
            print("\nGas cars:")
            for el in g:
                print(el)
                
            print("\nElectric cars:")
            for el in e:
                print(el)
                
            print("\n\n")
            CarUI.prin_menu()
                
                
            print("Select an option:")
            opt=CarUI.read_st()
            
            if opt=='1':
                print("Give the type of diesel for the car:")
                f=CarUI.read_st()
                print("Give the id of the car:")
                i=CarUI.read_st()
                print("Give the year of the car:")
                y=CarUI.read_nr()
                print("Give the price of the car:")
                p=CarUI.read_nr()
                
                self.__controller.create(i,y,p,f)
                
            elif opt=='2':
                print("Give the type of diesel for the car:")
                f=CarUI.read_st()
                
                self.__controller.incr(f)
                
                
            elif opt=='3':
                print("Give a year:")
                y=CarUI.read_nr()
                
                if y>0:
                    self.__controller.del_gy(y)
                
            elif opt =='4':
                d=self.__controller.get_all_d()
                g=self.__controller.get_all_g()
                e=self.__controller.get_all_e()
            
                print("Diesel cars:")
                for el in d:
                    print(el)
                
                print("\nGas cars:")
                for el in g:
                    print(el)
                
                print("\nElectric cars:")
                for el in e:
                    print(el)
                    
                input("Press any key...")
                
            elif opt =='0':
                break
            
            else:
                input("The option does not exist!Press any key...")
        
        
                
        
        