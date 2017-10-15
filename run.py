
#!/usr/bin/env python3.6

from password_locker import User 
from password_locker import Credential


#Start with Users information
def create_user(user_name,user_phone_number,user_email,user_password):
    '''
    Function that creates a new user information
    '''
    
    new_user = User(user_name,user_phone_number,user_email,user_password)
    return new_user

# save user information
def save_user(user):
    '''
    Function to save users information
    '''
    user.save_user()
    
# Delete User Information
def delete_user(user):
    '''
    Function to delete a user information
    '''
    user.delete_user()
    
# Check if user information exists
def check_existing_user(user_name):
    '''
    Function that checks whether the users information exists and returns a boolean
    '''
    return User.user_exists(user_name)

# Checks for all users
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

# Checks if user has logged in
def log_in_user(user_name,user_phone_number,user_email,user_password):
    '''
    Function that checks if the user has logged in
    '''
    login = User.login(user_name,user_phone_number,user_email,user_password)
    
    if login != False:
        return User.login(user_name,user_phone_number,user_email,user_password)
    

### CREDENTIAL INFORMATION
def create_credential(account_name, account_password):
    '''
    Function that creates login credentials
    '''
    
    new_credential = Credential(account_name, account_password)
    return new_credential

# save
def save_credentials(credential):
    '''
    Functions that save the users credentials
    '''
    credential.save_credentials()

# check existing credential account
def check_existing_credential_account(account_name):
    '''
    Function that checks whether the account exists
    '''
    return Credential.check_existing_credential_account(account_name)

# Dispalay all the accounts the user has
def display_all_credentials(account_password):
    '''
    Function that finds all the credentials saved
    '''
    return Credential.display_all_credentials(account_password)

#autogenerate password
def create_autogenerate_password(account_name):
    '''
    Function that autogenerates passwords for the user for specific accounts
    '''
    account_password = Credential.autogenerate_password()
    
    return account_password

    

def main():
    print("Welcome to password Locker. Create an account.")
    
# =============================================================================
#     user_name = input()
#     
#     print(f"{user_name}, Would you like to create a credential account?")
#     print('\n')
# =============================================================================
    while True:
        print("Use these short codes :\n cu - Create a new user account \n du - Display user information  \n lg - Log in \n ex - Exit Password Locker")
              
        short_code = input().lower()
          
        if short_code == 'cu':
            '''
            Create a new password locker account
            '''
            print("New Password Locker Account")
            print("-"*10)
              
            print ("User name: ....")
            user_name = input()

            print("Phone Number: ....")
            user_phone_number = input()
            
            print ("Email Address: ....")
            user_email = input()

            print("Password: ....")
            user_password = input()
            
            #Create and save new user
            save_user(create_user(user_name,user_phone_number,user_email,user_password))
            
            print('\n')
            print(f"{user_name} welcome! Continue to create you Credentials")
            
        elif short_code == 'du' :
            '''
            Display current user
            '''
            
            if display_users():
                print("Current Users")
                print("-"*10)
                
                for user in display_users():
                    print(f"{user.user_name}")
                    
                    print('\n')
                    print("-"*10)
            else:
                print('\n')
                print("You don't have an account. Please register to use Password Locker.")
                
                print('\n')
                    
        elif short_code == 'lg' :
            '''
            Logs the user in to view or create their accounts
            '''
            print("Please sign in")
            print('\n')
            
            print("Enter User Name:")
            user_name = input()
            
            print("Enter Password:")
            user_phone_number = input()
            
            print("Enter User Name:")
            user_email = input()
            
            print("Enter Password:")
            user_password = input()
            
            if  log_in_user(user_name,user_phone_number,user_email,user_password) == None:
                print("Forgot password or create new account")
                print('\n')
            
                
            else:
                log_in_user(user_name,user_phone_number,user_email,user_password)
                print(f"{user_name} Proceed to your credentials \n Use the short codes below")
                print('\n')
               
                
                while True:
                    '''
                    Loop through functions
                    '''
                    print("Use these short codes :\n cc - Create a New Credential account \n cg - Autogenerate password \n dc - Display credential information  \n lg - Log in \n ex - Log out")
                    
                    if short_code == 'cc':
                        '''
                        Create credential account
                        '''
                        
                        print("New Account")
                        print('\n')
                        print("-"*10)
                        
                        print(" Account Name: ....")
                        account_name = input()
                        
                        print(" Password: ....")
                        account_password = input() 
                        
                        save_credentials(create_credential(account_name, account_password))
                        
                        print(f"{account_name}, you have created a new account")
                        print('\n')
                        
                    elif short_code == 'cg':
                        '''
                        Autogenerate passowrd
                        '''
                        
                        print("New Account")
                        print('\n')
                        print("-"*10)
                        
                        print(" Account Name: ....")
                        account_name = input()
                       
                        #save new account/autogenrate password
                        save_credentials(Credential(account_name, (create_autogenerate_password(account_name))))
                        
                        print(f"{account_name}, you have created a new account")
                        print('\n')
                        
                    ##exit credential
                    elif short_code == 'ex' :
                        print(f"About to exit")
                        print('\n')
                        break
                    else:
                        print("Try again")
                        print('\n')
                        
                        
                
                
                                
                
         # Exit Password Locker  
        elif short_code == "ex":
            print("Exit Password Locker")
            break
        else:
            print("Please use the short codes to continue. Thank you.")
              

if __name__ == '__main__':
    main()
    
