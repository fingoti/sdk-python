"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fingoti
from fingoti.model.device_power import DevicePower
from fingoti.model.device_version import DeviceVersion
from fingoti.model.node_address import NodeAddress
from fingoti.model.node_data import NodeData
from fingoti.model.node_location import NodeLocation
globals()['DevicePower'] = DevicePower
globals()['DeviceVersion'] = DeviceVersion
globals()['NodeAddress'] = NodeAddress
globals()['NodeData'] = NodeData
globals()['NodeLocation'] = NodeLocation
from fingoti.model.vyne_node import VyneNode


class TestVyneNode(unittest.TestCase):
    """VyneNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVyneNode(self):
        """Test VyneNode"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VyneNode()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
