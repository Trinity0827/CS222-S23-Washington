import unittest

#code
class Stack():
    def _init_(self):
        self.items = []
    def size(self):
        return len(self.items) 
    def push(self, arg):
        self.items.append(arg)
    def pop(self):
        if not self.is_empty():
            return self.items.pop
        return IndexError("Stack is Empty")
    
    def is_empty(self): # return the boolean 
        return (len(self.items) == 0)






# 3 test cases
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()


    def test_push_and_pop(self): #test push and pop at the same time
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    
    def test_is_empty(self): # test 
        self.assertTrue(self.stack.is_empty())
        self.stack.push(55)
        self.assertFalse(self.stack.is_empty())


    def test_size(self): # write an function that checking the size of the stack
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 2)


if __name__ == "__main__":
    unittest.main()
