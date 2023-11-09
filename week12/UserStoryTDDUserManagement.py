'''
User story 1: User Registration
as an new usser, I want to be able to register for a new account using email and password
'''


'''
User story 2: Login
as a regustered user, I want to be able to log in ti my account using email and password
'''



'''
User story 3: Password Reset
as a user who forgot password, I want to be able to request an password reset 
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

    def test_password_reset_request(self):#user story 3 capture, checking to see if the request can be sent
        userManager = UserManagement()
        result = userManager.request_password_reset("a@b.com")
        self.assertTrue(result)
    def test_password_reset(self): # Testung the reset password funcition
        userManager = UserManagement()
        userManager.register("a@b.com", "password")
        reset_token = userManager.request_password_reset("a@b.com")
        result = userManager.resetpassword("a@b.com", reset_token, "newPassword")
        self.assertTrue(result)








   
