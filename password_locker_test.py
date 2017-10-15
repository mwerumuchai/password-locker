#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:59:06 2017

@author: muchai
"""

import unittest
from password_locker import User 
from password_locker import Credential
import pyperclip

class TestUser(unittest.TestCase): # TestUser is a subclass
    
    '''
    Test class that defines test cases for the user class behaviours
    '''
    
    def setUp(self):
        '''
        Set up method runs before each test case
        '''
        
        self.new_user = User("mwerumuchai", "0725336159","mwerumuchai@gmail.com", "mweru90")
        
    def test_init(self):
        
        '''
        Test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"mwerumuchai")
        self.assertEqual(self.new_user.user_phone_number,"0725336159")
        self.assertEqual(self.new_user.user_email,"mwerumuchai@gmail.com")
        self.assertEqual(self.new_user.user_password,"mweru90")
        
                  
    
    # Check if user information is saved
    def test_save_user(self):
        
         '''
         Tests save user test case to see if the user object is saved into the user_list
         '''
         self.new_user.save_user() #saving new user
         self.assertEqual(len(User.user_list), 1)
         
         
     # this method executes a set of instructions after every test    
    def tearDown(self):
        '''
        This cleans up after each test case has run
        '''
        User.user_list = []
        
    
    # Check if user can save multiple user accounts
    def test_save_multiple_user(self):
        
        '''
        Test save multiple user test case to see whether we can save multiple user accounts to our user list
        '''
        
        self.new_user.save_user() 
        test_user = User("marymukami", "0714253689", "marymukami@gmail.com", "mary90")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        
        
       # Use assertTrue method to check if the user account exists 
    def test_user_exists(self):
        '''
        Test to check if we can return a Boolean if account isn't found
        '''
        
        self.new_user.save_user()
        test_user =  User("marymukami", "0714253689", "marymukami@gmail.com", "mary90")
        test_user.save_user()
        
        user_exists = User.user_exists("marymukami")
        
        self.assertTrue(user_exists)
        
    # Log into Credentials
    def test_login(self):
        '''
        Test to check if user can log into their credentials
        '''
        self.new_user.save_user() #saving new user
        
        test_user = User("mwerumuchai", "0725336159","mwerumuchai@gmail.com", "mweru90")
        test_user.save_user()
        
        # Connect with credential account
        found_credential = User.login("mwerumuchai", "0725336159","mwerumuchai@gmail.com", "mweru90")
        self.assertEqual(found_credential, Credential.credential_account_list )
                      
        
     # Display all users
    def test_display_users(self):
        
        '''
        test_display_users to test that it returns a list of all users saved
        '''
        
        self.assertEqual(User.display_users(), User.user_list)
        
        
# Credential Account
        
class TestCredential(unittest.TestCase): # TestUser is a subclass
    
    '''
    Test class that defines test cases for the credential class behaviours
    '''
    
    def setUp(self):
        '''
        Set up method runs before each test case
        '''
        
        self.new_credential = Credential("Instagram", "muchai90")
        
    def test_init(self):
        
        '''
        Test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.account_password,"muchai90")
        
     # Check if account information is saved
    def test_save_credential_account(self):
        
         '''
         Tests save credential account test case to see if the credential object is saved into the credentail_list
         '''
         self.new_credential.save_credential() #saving new credential account
         self.assertEqual(len(Credential.credential_account_list), 1)
         
    # Check if user can save multiple credential accounts
    def test_save_multiple_credential_account(self):
        
        '''
        Test save multiple user test case to see whether we can save multiple user accounts to our user list
        '''
        
        self.new_credential.save_credential() 
        test_credential = Credential("Facebook", "facebook90")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_account_list), 2)
    
     # this method executes a set of instructions after every test    
    def tearDown(self):
        '''
        This cleans up after each test case has run
        '''
        Credential.credential_account_list = []
        
    # Deletes the credential account
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential account
        '''
        
        self.new_credential.save_credential()
        test_credential = Credential("Instagram", "muchai90")
        test_credential.save_credential()
        
        # deleting the credential account
        self.new_credential.delete_credential_account()
        self.assertEqual(len(Credential.credential_account_list), 1)
        
    #D isplay all credential account
    def test_display_all_credential_accounts(self):
        
        '''
        test_display_all_credential_accounts to test that it returns a list of all credential accounts saved
        '''
        
        self.assertEqual(Credential.display_all_credential_accounts(), Credential.credential_account_list)
        
        
    # Use find_by_account_name
    def test_find_credential_by_account_name(self):
        '''
       Test to get the account name and returns the credential that matches that number
        '''
        
        self.new_credential.save_credential()
        
        test_credential = Credential("Instagram", "muchai90")
        
        test_credential.save_credential()
        
        found_credential = Credential.find_by_account_name(test_credential.account_name)
        
        self.assertEqual(found_credential.account_password,test_credential.account_password)
        
      
    # Check if credential account exists
    def test_existing_credential_account(self):
        '''
        Test if the credential account exists
        '''
        self.new_credential.save_credential()
        
        test_credential = Credential("Instagram", "muchai90")
        
        test_credential.save_credential()
        
        check_existing_credential_account = Credential.check_existing_credential_account("Instagram")
        
        self.assertTrue(check_existing_credential_account)
        
    # Copy details in credentials account
    def test_copy_account_name(self):
        
        '''
        Test to confirm that the copied account name  if from the credential list
        '''
        
        self.new_credential.save_credential()
        Credential.copy_account_name("Instagram")
        
        self.assertEqual(self.new_credential.account_name,pyperclip.paste())
        
        
    # Autogenerate new password
    def test_autogenerate_password(self):
        '''
        Test if user can get autogenerated passwords
        '''
        autogenerate_password = self.new_credential.autogenerate_password()
        self.assertEqual(len(autogenerate_password),8)
        
    
        
          
          
if __name__ == '__main__':
		unittest.main(verbosity=2)