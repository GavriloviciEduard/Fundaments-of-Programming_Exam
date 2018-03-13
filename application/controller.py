from domain.car import Car

class CarController():
    


    def __init__(self,r):
        '''
        Constructor
        '''
        
        self.__repo=r
        
        
    '''
    Create a car depending on type of fuel.
    '''   
        
    def create(self,i,y,p,f):
        
        if f=="Diesel":
            
            if p and len(i.strip())>0:
                c=Car(i,y,p)
                self.__repo.cr_ap_diesel(c)
                
            else:
                input("Invalid Data! Press any key...")
        
        elif f=="Gas":
            
            if p and len(i.strip())>0:
                c=Car(i,y,p)
                self.__repo.cr_ap_gas(c)
                
            else:
                input("Invalid Data!Press any key...")
                
                
        elif f=="Electric":
            
            if p and len(i.strip())>0:
                c=Car(i,y,p)
                self.__repo.cr_ap_electric(c)
                
            else:
                input("Invalid Data!Press any key...") 
                
                
        else:
            input("Invalid Type of Fuel!Press any key...")
            
    '''
    Get all diesel cars.
    '''           
    def get_all_d(self):
        
        return self.__repo.get_all_diesel()
    
    '''
    Get all gas cars.
    ''' 
    def get_all_g(self):
        
        return self.__repo.get_all_gas()
    
    '''
    Get all electric cars.
    ''' 
    
    def get_all_e(self):
        
        return self.__repo.get_all_electric()
    
    '''
    Delete cars by a given year. 
    ''' 
    
    def del_gy(self,y):
        self.__repo.del_given_year(y)
        
        
    '''
    Increase price of all cars.
    '''     
    def incr(self,f):
        self.__repo.increase(f)
        
    def start(self):
        c1=Car("C1",2007,700)
        c2=Car("C2",2011,900)
        c3=Car("C3",2000,9600)
        
        self.__repo.cr_ap_diesel(c1)
        self.__repo.cr_ap_gas(c2)
        self.__repo.cr_ap_electric(c3)       
        
        