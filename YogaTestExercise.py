
# coding: utf-8

# In[12]:
import os,sys, unittest

from yoga.patient import exercise

class TestExercise(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        print('setupClass')
        cls.e1=exercise.Exercise('Nadi Shuddhi', 6)                    
        cls.e1.display()
        cls.e2=exercise.Exercise('Bhramari', 3)                    
        cls.e2.display()
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        del cls.e1
        del cls.e2
    def setUp(self):
        self.e3=exercise.Exercise('Savasana', 4) 
        self.e4=exercise.Exercise('Surya Namaskar', 15)
        self.e5=exercise.Exercise('Halasana', 2)
        self.e6=exercise.Exercise('Pavanmuktasana', 3) 
        self.e7=exercise.Exercise('Tadasana', 2) 
        self.e3.display()
        print('Setup')
    def tearDown(self):
        print('Teardown')
        del self.e3
        del self.e4
        del self.e5
        del self.e6
        del self.e7
    def test_display(self):
        rtn1=self.e3.display()
        self.assertEqual(rtn1,0)
        rtn1=self.e4.display()
        self.assertEqual(rtn1,0)
        rtn1=self.e5.display()
        self.assertEqual(rtn1,0)
        rtn1=self.e6.display()
        self.assertEqual(rtn1,0)
        rtn1=self.e7.display()
        self.assertEqual(rtn1,0)
    def test_User1(self):
        e1 = exercise.Exercise('Nadi Shuddhi', '12e')  
        self.assertNotIsInstance(e1.time, int)
    def test_User2(self):
        e1 =exercise.Exercise( 'a', 250)  
        self.assertNotEqual(e1.name, 'a')

#unittest.main(argv=[''], verbosity=2, exit=False)

