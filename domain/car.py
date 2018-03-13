

class Car():
    

    '''
        Constructor
    '''
    def __init__(self,f='',y=0,p=0):
        
        self.__fuel=f
        self.__year=y
        self.__price=p
        
    def set_fuel(self,f):
        '''
        Seter
        '''
        self.__fuel=f
        
        
    def set_year(self,y):
        '''
        Seter
        '''
        self.__year=y
        
        
    def set_price(self,p):
        '''
        Seter
        '''
        self.__price=p
        
        
    def get_fuel(self):
        
        '''
        Geter
        '''
        
        return self.__fuel
    
    
    def get_year(self):
        
        '''
        Geter
        '''
        
        return self.__year
    
    
    def get_price(self):
        
        '''
        Geter
        '''
        
        return self.__price
    
    
    
    def __str__(self):
        
        return "ID:"+self.__fuel+"//--//"+"Year:"+str(self.__year)+"//--//"+"Price:"+str(self.__price)
        
        
        
        