"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import fingoti
from fingoti.api.webhook_api import WebhookApi  # noqa: E501


class TestWebhookApi(unittest.TestCase):
    """WebhookApi unit test stubs"""

    def setUp(self):
        self.api = WebhookApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_webhook_id(self):
        """Test case for delete_webhook_id

        Delete a Webhook. This is not recoverable.  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Get all registered webhooks.  # noqa: E501
        """
        pass

    def test_get_webhook_id(self):
        """Test case for get_webhook_id

        Get specified webhook.  # noqa: E501
        """
        pass

    def test_get_webhook_logs(self):
        """Test case for get_webhook_logs

        Get all registered webhooks with call logs.  # noqa: E501
        """
        pass

    def test_patch_webhook_id(self):
        """Test case for patch_webhook_id

        Update Fingoti webhook.  # noqa: E501
        """
        pass

    def test_post_webhook(self):
        """Test case for post_webhook

        Register a new webhook.  # noqa: E501
        """
        pass

    def test_post_webhook_retry(self):
        """Test case for post_webhook_retry

        Retry a webhook.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()