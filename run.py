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
    print("Welcome to password Locker. Kindly write your user name below")
    
    user_name = input()
    
    print(f"{user_name}, Would you like to create a credential account?")
    print('\n')
    

if __name__ == '__main__':
    main()
    