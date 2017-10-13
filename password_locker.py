# Global variables
user_name = ' '
user_password = ' '


#The below class user 
class User:
    '''
    Class that generates new instances of users
    '''
    user_list = []
    
    # Using global variables in functions
    global user_name
    global user_password
    
    def __init__(self,user_name,user_phone_number,user_email,user_password):
        
        '''
        __init__method that helps us define propertis for our objects
        
        Args:
            full_name: New User full name.
            favorite_color: New user favorite color.
            email: New user email.
            password: New user password.
        '''
        
        self.user_name = user_name
        self.user_phone_number = user_phone_number
        self.user_email = user_email
        self.user_password = user_password
        
    def save_user(self):
        
        '''
        Save user method saves user objects
        '''
        
        User.user_list.append(self)
    
    
    def check_existing_user_account(user_password):
        
        '''
        Functions that checks if the user account exists and returns a boolean
        '''
        
        return User.user_exists(user_password)
    
    @classmethod
    def user_exists(cls, user_password):
        
        '''
        Method that is used to check if the account exists. Use phone number.
        '''
        # will lopp through each account that is saved and it will check if the number matches. 
        for user in cls.user_list:
            if user.user_password == user_password:
                return True
            
        return False
        
        
# Create a class credential account
class Credential:
    '''
    class the generates new instances of credential users
    '''
    
    credential_account_list = []
    global user_list
    


    
   
    
    
 
    
    
    


