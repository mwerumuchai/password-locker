import pyperclip

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
            user_name: New User user name.
            user_phone_number: New user phone number.
            user_email: New user email.
            user_password: New user password.
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
    
    
    def check_existing_user_account(user_name):
        
        '''
        Functions that checks if the user account exists and returns a boolean
        '''
        
        return User.user_exists(user_name)
    
    #Display all users
    @classmethod
    def display_users(cls):
        '''
        Methos that returns the user list
        '''
        
        return cls.user_list
    
    @classmethod
    def user_exists(cls, user_name):
        
        '''
        Method that is used to check if the account exists. User name.
        '''
        # will lopp through each account that is saved and it will check if the password matches. 
        for user in cls.user_list:
            if user.user_name == user_name:
                #return Credential.credential_account_list
                return True
            
        return False

        
# Create a class credential account
class Credential:
    '''
    class the generates new instances of credential users
    '''
    
    credential_account_list = []
    global user_list
    
    def __init__(self,account_name, account_password):
        
        '''
        __init__method that helps us define propertis for our objects
        
        Args:
            user_name: New user name
            password: New user password.
        '''
        
        self.account_name = account_name
        self.account_password = account_password
        
    # Save credential
    def save_credential(self):
        
        '''
        Save credential method saves user credential objects
        '''
        
        Credential.credential_account_list.append(self)
        
    # Delete account
    def delete_credential_account(self):
        
        '''
        delete_credential_account delete a saved account from the credential account list
        '''
        
        Credential.credential_account_list.remove(self)
        
        
    # Find by account name
    @classmethod
    def find_by_account_name(cls,account_name):
      '''
      Method that gets the account name and returns the credential that matches that number
       
      Args:
          account_name: Account name to search for
      Returns :
          The actual account name for that credential
      '''
      
      for credential in cls.credential_account_list:
          if credential.account_name == account_name:
              return credential
        
    @classmethod
    def display_all_credential_accounts(cls):
        '''
        method that returns the credential account list
        '''
        return cls.credential_account_list
    
    @classmethod
    def copy_account_name(cls, account_name):
        account_name_found = Credential.find_by_account_name(account_name)
        pyperclip.copy(account_name_found.account_name)
        
    


    
   
    
    
 
    
    
    


