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
        
        self.new_user = User("Esther Muchai", "mwerumuchai@gmail.com","0725336159", "mweru90")
    
    # Check if user information is saved
    def test_save_user(self):
        
         '''
         Tests save user test case to see if the user object is saved into the user_list
         '''
         self.new_user.save_user() #saving new user
         self.assertEqual(len(User.user_list), 1)
          
          
if __name__ == '__main__':
		unittest.main(verbosity=2)