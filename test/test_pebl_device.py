"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fingoti
from fingoti.model.device_blink import DeviceBlink
from fingoti.model.device_bus import DeviceBus
from fingoti.model.device_cloud import DeviceCloud
from fingoti.model.device_location import DeviceLocation
from fingoti.model.device_power import DevicePower
from fingoti.model.device_session import DeviceSession
from fingoti.model.device_support import DeviceSupport
from fingoti.model.device_uptime import DeviceUptime
from fingoti.model.device_version import DeviceVersion
globals()['DeviceBlink'] = DeviceBlink
globals()['DeviceBus'] = DeviceBus
globals()['DeviceCloud'] = DeviceCloud
globals()['DeviceLocation'] = DeviceLocation
globals()['DevicePower'] = DevicePower
globals()['DeviceSession'] = DeviceSession
globals()['DeviceSupport'] = DeviceSupport
globals()['DeviceUptime'] = DeviceUptime
globals()['DeviceVersion'] = DeviceVersion
from fingoti.model.pebl_device import PeblDevice


class TestPeblDevice(unittest.TestCase):
    """PeblDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPeblDevice(self):
        """Test PeblDevice"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PeblDevice()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
