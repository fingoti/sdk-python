"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fingoti
from fingoti.model.webhook_attempts import WebhookAttempts
from fingoti.model.webhook_headers import WebhookHeaders
from fingoti.model.webhook_status import WebhookStatus
globals()['WebhookAttempts'] = WebhookAttempts
globals()['WebhookHeaders'] = WebhookHeaders
globals()['WebhookStatus'] = WebhookStatus
from fingoti.model.call_log_dto import CallLogDto


class TestCallLogDto(unittest.TestCase):
    """CallLogDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCallLogDto(self):
        """Test CallLogDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CallLogDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
