import unittest,os

    
from yoga.output import fileio
from yoga.patient import patient
from yoga.patient import exercise



class TestFileio(unittest.TestCase): # test class
    print("testing enviroment")
    @classmethod
    def setUpClass(cls):
        print('Test File IO setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self): 
        print('setup...')
        self.p1=patient.Patient("rroy","pass","Mr.","Rajeev","","Roy")
        self.p2=patient.Patient("mzardadi", "pass", "Mr.", "Mohsen", "","Zardadi")
        self.p3=patient.Patient("mroberto", "pass", "Mr.", "Maziar", "","Roberto")
        self.p1.addRev(100)
        self.p2.addRev(200)
        self.p3.addRev(300)
        self.ex1 = exercise.Exercise("Surya Namaskar", 30)
        self.ex2 = exercise.Exercise("Savasana", 10)
        
        
    def tearDown(self):
        print('tear down ...')
        del self.p1
        del self.p2
        del self.p3
        del self.ex1
        del self.ex2
        os.remove("test1.csv")
        os.remove("test2.csv")
        os.remove("test3.csv")
        os.remove("test4.csv")
        os.remove("test5.csv")
            
    
    def test_pcsv(self):
        a=True
        fileio.ExportUsers.pcsv(patient.Patient._registery,"test1.csv")
        state = os.path.isfile('./test1.csv')      
        self.assertTrue(state)
        
        a=fileio.ExportUsers.pcsv("Error","test2.csv")
        self.assertFalse(a)
        
        fileio.ExportUsers.pcsv(patient.Patient._registery,"test3.csv")
        state = os.path.isfile('./test3.csv')      
        self.assertTrue(state)
                
        fileio.ExportUsers.pcsv(patient.Patient._registery,"test4.csv")
        state = os.path.isfile('./test3.csv')      
        self.assertTrue(state)
        
        fileio.ExportUsers.pcsv(patient.Patient._registery,"test5.csv")
        state = os.path.isfile('./test5.csv')      
        self.assertTrue(state)

    def test_ecsv(self):
        a=True
        fileio.ExportUsers.ecsv(exercise.Exercise._registery,"test1.csv")
        state = os.path.isfile('./test1.csv')      
        self.assertTrue(state)
        
        a=fileio.ExportUsers.ecsv("Error File","test2.csv")   
        self.assertFalse(a)
        
        fileio.ExportUsers.ecsv(exercise.Exercise._registery,"test3.csv")
        state = os.path.isfile('./test3.csv')      
        self.assertTrue(state)
        
        fileio.ExportUsers.ecsv(exercise.Exercise._registery,"test4.csv")
        state = os.path.isfile('./test4.csv')      
        self.assertTrue(state)
        
        fileio.ExportUsers.ecsv(exercise.Exercise._registery,"test5.csv")
        state = os.path.isfile('./test5.csv')      
        self.assertTrue(state)
        a=fileio.ExportUsers()
        
    
    
    

#unittest.main()

