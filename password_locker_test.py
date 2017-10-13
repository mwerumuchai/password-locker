#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:59:06 2017

@author: muchai
"""

import unittest
from user import User

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours
    '''
    
    # Check if user information is saved
    def test_save_user(self):
        
         '''
         Tests save user test case to see if the user object is saved into the user_list
         '''
          self.new_user.save_user() #saving new user
         