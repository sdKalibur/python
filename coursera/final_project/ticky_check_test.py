#! /usr/bin/env python3

import unittest
from ticky_check import *

from final_project.ticky_check import get_tick_events


class Test_ticky_check(unittest.TestCase):

    def test_get_ticky_events(self):
        """test getting a ticky event from syslog"""
        testcase = "Jan 31 18:43:01 ubuntu.local ticky: ERROR Ticket doesn't exist (nonummy"
        expected = "ERROR Ticket doesn't exist"
        self.assertEqual(get_tick_events(testcase), expected)

    def Test_get_tick_stats(self):
        # """create per user stats dict from of dict lists count per user"""
        # userlist = {'Kiara','Andy','Grace'}
        # # 'britanni', 'blossom', 'montanap', 'flavia', 'kirknixon', 'x
        # # testcase = {'success': ['Kiara','Andy','Grace','Grace','Andy','Grace'], \
        # #             'error': ['Kiara','Andy','Grace','Kiara','Andy','Grace']}
        # testcase = sys.argv[1]
        # expected = [
        #     {'name': 'bree', 'success': 1, 'error': 2 },
        #     {'name': 'blossom', 'success':3 , 'error': 2 },
        #     {'name': 'mdouglas', 'success':2 , 'error': 2 }
        #     ]
        # self.assertEqual(get_tick_stats(testcase), expected)
        pass

unittest.main()
