"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import fingoti
from fingoti.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user_tokens_id(self):
        """Test case for delete_user_tokens_id

        Delete a Token. Token will no longer authenticate API requests. This is not recoverable.  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get your Fingoti user.  # noqa: E501
        """
        pass

    def test_get_user_organisations(self):
        """Test case for get_user_organisations

        Get all organisations you are a member of.  # noqa: E501
        """
        pass

    def test_get_user_sessions(self):
        """Test case for get_user_sessions

        Get all user sessions.  # noqa: E501
        """
        pass

    def test_get_user_tokens(self):
        """Test case for get_user_tokens

        Get all API tokens.  # noqa: E501
        """
        pass

    def test_get_user_tokens_id(self):
        """Test case for get_user_tokens_id

        Get specified token.  # noqa: E501
        """
        pass

    def test_patch_user(self):
        """Test case for patch_user

        Update Fingoti user.  # noqa: E501
        """
        pass

    def test_patch_user_tokens_id(self):
        """Test case for patch_user_tokens_id

        Update API token.  # noqa: E501
        """
        pass

    def test_post_user(self):
        """Test case for post_user

        Register a new Fingoti user.  # noqa: E501
        """
        pass

    def test_post_user_tokens(self):
        """Test case for post_user_tokens

        Generate new API token.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()