#!/usr/bin/env python3.6

from password_locker import User 
#from password_locker import Credential


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

def main():
    print("Welcome to password Locker. Create an account.")
    
# =============================================================================
#     user_name = input()
#     
#     print(f"{user_name}, Would you like to create a credential account?")
#     print('\n')
# =============================================================================
    while True:
        print("Use these short codes :\n cu - Create a new user account \n du - Display user information \n ex - Exit Password Locker")
              
        short_code = input().lower()
          
        if short_code == 'cu':
            '''
            Create a new password locker account
            '''
            print("New Password Locker Account")
            print("-"*10)
              
            print ("User name ....")
            user_name = input()

            print("Password ....")
            user_password = input()
            
        elif short_code == "ex":
            print("Exit Password Locker")
            break
        else:
            print("Please use the short codes to continue. Thank you.")
              

if __name__ == '__main__':
    main()
    