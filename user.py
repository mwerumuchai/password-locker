from user import User

class user:
    '''
    Class that generates new instances of users
    '''
    
    def __init__(self,full_name,favorite_color,email,password,):
        '''
        __init__method that helps us define propertis for our objects
        
        Args:
            full_name: New User full name.
            favorite_color: New user favorite color.
            email: New user email.
            password: New user password.
        '''
        self.full_name = full_name
        self.favorite_color = favorite_color
        self.email = email
        self.password = password