"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fingoti
from fingoti.model.timer_request import TimerRequest
from fingoti.model.timer_status import TimerStatus
globals()['TimerRequest'] = TimerRequest
globals()['TimerStatus'] = TimerStatus
from fingoti.model.gateway_timer import GatewayTimer


class TestGatewayTimer(unittest.TestCase):
    """GatewayTimer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGatewayTimer(self):
        """Test GatewayTimer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GatewayTimer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()