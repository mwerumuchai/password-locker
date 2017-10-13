# Global variables
user_full_name = ' '
user_password = ' '

class User:
    '''
    Class that generates new instances of users
    '''
    user_list = []
    global user_full_name
    global user_password
    
    def __init__(self,user_full_name,user_favorite_color,user_email,user_password,):
        
        '''
        __init__method that helps us define propertis for our objects
        
        Args:
            full_name: New User full name.
            favorite_color: New user favorite color.
            email: New user email.
            password: New user password.
        '''
        
        self.user_full_name = user_full_name
        self.user_favorite_color = user_favorite_color
        self.user_email = user_email
        self.user_password = user_password
        
    def save_user(self):
        
        '''
        Save user method saves user objects
        '''
        
        User.user_list.append()

