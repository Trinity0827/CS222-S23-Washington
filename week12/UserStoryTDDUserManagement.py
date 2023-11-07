'''
User story 1: User Registration
as an new usser, I want to be able to register for a new account using email and password
'''


'''
User story 2: Login
as a regustered user, I want to be able to log in ti my account using email and password
'''

import unittest
from User import UserManagement 
class TestUserManagement(unittest.TestCase): 
    def test_registration(self): #user story 1 capture 
        userManager = UserManagement()
        result = userManager.registester("a@b.com", "password")
        self.assertTrue(result)  

    def test_login(self):#user story 2 capture
        userManager = UserManagement()
        userManager.register("a@b.com", "password")
        result = userManager.login("a@b.com", "password")
        self.assertTrue(result)






   
