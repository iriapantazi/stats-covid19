#! /usr/bin/env python 

import unittest
from unittest.mock import Mock, patch
import sys
import covid
import requests


class Testing(unittest.TestCase):


    def test_detect_python_version(self):
        """
        test_detect_python_version:
        Test if python version is supported.
        """
        self.assertEqual(sys.version_info.major, 3)

        patcher = patch('sys.version_info', major=2, minor=7)
        patcher.start()
        with self.assertRaises(SystemExit): 
            covid.detect_python_version()


    def test_parse_arguments(self):
        """
        test_parse_arguments:
        Will be concluded in due time.
        """


    def test_choose_title(self):
        """
        test_choose_title:
        """
        expected = f'Plot of number of cumulative deaths'
        returned = covid.choose_title('deaths')
        self.assertEqual(expected, returned)

        expected = f'Plot of number of cumulative recovered cases'
        returned = covid.choose_title('recovered')
        self.assertEqual(expected, returned)

        expected = f'Plot of number of cumulative confirmed cases'
        returned = covid.choose_title('confirmed')
        self.assertEqual(expected, returned)


    def test_request_data(self):
        """
        test_request_data:
        """
        mock = Mock()
        requests.get = mock


    def test_main(self):
        """
        test_main:
        """


if __name__=='__main__':
    unittest.main()
