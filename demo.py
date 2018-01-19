import unittest
import HTMLTestRunner
import time




class Test(unittest.TestCase):
    def setUp(self):
        self.number = 30

    def test_case1(self):
        self.assertEqual(self.number, 10, msg='num is not 30')

    def test_case2(self):
        self.assertEqual(self.number, 20, msg='num is not 30')

    # @unittest.skip('skip test_case3')
    def test_case3(self):
        self.assertEqual(self.number, 30, msg='num is not 30')

    def tearDown(self):
        print('Test Over')


'''
#Method 1
if __name__ == '__main__':
    unittest.main()

'''


#Method 2
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Test("test_case1"))
    suit.addTest(Test("test_case2"))
    suit.addTest(Test("test_case3"))

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = '/Users/chenqi1/Desktop/result_' + now + '_mac_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                    title='Test Report',
                                    description='Implementation Example with: ')
    runner.run(suit)
    fp.close


'''
#Method 3
if __name__=='__main__':
    test_dir='/Users/chenqi1/Pycharm/study/PracticeFile/'
    discover=unittest.defaultTestLoader.discover(test_dir, '*.py')
    runner=unittest.TextTestRunner()
    runner.run(discover)
'''



