#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:59:06 2017

@author: muchai
"""

import unittest
from password_locker import User 

class TestUser(unittest.TestCase): # TestUser is a subclass
    
    '''
    Test class that defines test cases for the user class behaviours
    '''
    
    def setUp(self):
        '''
        Set up method runs before each test case
        '''
        
        self.new_user = User("Mweru Muchai", "0725336159","mwerumuchai@gmail.com", "mweru90")
        
    def test_init(self):
        
        '''
        Test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_full_name,"Mweru Muchai")
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
        test_user = User("Mary Mukami", "0714253689", "marymukami@gmail.com", "mary90")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        
        
       # Use assertTrue method to check if the user account exists 
    def test_user_exists(self):
        '''
        Test to check if we can return a Boolean if account isn't found
        '''
        
        self.new_user.save_user()
        test_user =  User("Mary Mukami", "0714253689", "marymukami@gmail.com", "mary90")
        test_user.save_user()
        
        user_exists = User.user_exists("mary90")
        
        self.assertTrue(user_exists)
        
          
          
if __name__ == '__main__':
		unittest.main(verbosity=2)