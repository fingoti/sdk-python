"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fingoti
from fingoti.model.network_ip import NetworkIp
from fingoti.model.network_mac import NetworkMac
globals()['NetworkIp'] = NetworkIp
globals()['NetworkMac'] = NetworkMac
from fingoti.model.gateway_network import GatewayNetwork


class TestGatewayNetwork(unittest.TestCase):
    """GatewayNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGatewayNetwork(self):
        """Test GatewayNetwork"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GatewayNetwork()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
