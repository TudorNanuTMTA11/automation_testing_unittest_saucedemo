import unittest

import HtmlTestRunner

from inventory import Test_Inventory
from login import Test_Login


class TestSuite(unittest.TestCase):

        def test_suite(self):
            teste_de_rulat = unittest.TestSuite()
            teste_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test_Inventory),
                                            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Login)])


            runner = HtmlTestRunner.HTMLTestRunner\
                                (
                combine_reports=True, # daca rulam mai multe clase, ne va genera raport
                report_title = "Test execution report",
                report_name = "Test results"
        )

            runner.run(teste_de_rulat)