

class CarRepo():
    


    def __init__(self):
        '''
        Constructor
        '''
        
        self.__diesel=[]
        self.__gas=[]
        self.__electric=[]
        
        
        
    '''
    Create diesel car.
    '''   
    def cr_ap_diesel(self,obj):
        
        if len(obj.get_fuel().strip())>0 and obj.get_price()>0:
            self.__diesel.append(obj)
            
        else:
            input("Invalid Data!Press any key...")
    
    '''
    Create electric car.
    '''   
        
    def cr_ap_electric(self,obj):
        if len(obj.get_fuel().strip())>0 and obj.get_price()>0:
            self.__electric.append(obj)
            
        else:
            input("Invalid Data!Press any key...")
    '''
    Create gas car.
    '''      
    def cr_ap_gas(self,obj):
        if len(obj.get_fuel().strip())>0 and obj.get_price()>0:
            self.__gas.append(obj)
            
            
        else:
            input("Invalid Data!Press any key...")
    '''
    Get all diesel cars.
    '''     
    def get_all_diesel(self):
        
        s=[]
        
        for el in self.__diesel:
            s.append(str(el))
            
        return s
    
    '''
    Get all electric cars.
    '''
    
    def get_all_electric(self):
        
        s=[]
        
        for el in self.__electric:
            s.append(str(el))
            
        return s
    
    
    '''
    Get all gas cars.
    '''
    
    
    def get_all_gas(self):
        
        s=[]
        
        for el in self.__gas:
            s.append(str(el))
            
        return s
    
    
    '''
    Delete cars by a given year. 
    ''' 
    
    def del_given_year(self,y):
        
        global i
        
        for i in range(len(self.__diesel)-1,0,-1):
                    if self.__diesel[i].get_year()<y:
                        del(self.__diesel[i])
                        
                    
                    
        for i in range(len(self.__electric)-1,0,-1):
                if self.__electric[i].get_year()<y:
                    del(self.__electric[i])
                    
                
        for i in range(len(self.__gas)-1,0,-1):
                if self.__gas[i].get_year()<y:
                    del(self.__gas[i])
                    
        if len(self.__diesel):            
            if self.__diesel[0].get_year()<y:
                del(self.__diesel[0])
        if len(self.__electric):                
            if self.__electric[0].get_year()<y:
                del(self.__electric[0])
        
        if len(self.__gas):                
            if self.__gas[0].get_year()<y:
                        del(self.__gas[0])
                    
            
    
    '''
    Increase price of all cars.
    '''                
    def increase(self,f):
        
        if f=="Diesel":
            
            for el in self.__diesel:
                nr=(el.get_price()*10)//100
                nr=el.get_price()+nr
                
                el.set_price(nr)
            
        elif f =="Gas":
            
            for el in self.__gas:
                nr=(el.get_price()*10)//100
                nr=el.get_price()+nr
                
                el.set_price(nr)
            
        elif f =="Electric":
            
            for el in self.__electric:
                nr=(el.get_price()*10)//100
                nr=el.get_price()+nr
                
                el.set_price(nr)
                
    
    
    
        