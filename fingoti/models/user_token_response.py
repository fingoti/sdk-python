# coding: utf-8

"""
    Fingoti API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from fingoti.configuration import Configuration


class UserTokenResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'success': 'bool',
        'page_number': 'int',
        'count': 'int',
        'tokens': 'list[UserTokenDto]'
    }

    attribute_map = {
        'success': 'success',
        'page_number': 'pageNumber',
        'count': 'count',
        'tokens': 'tokens'
    }

    def __init__(self, success=None, page_number=None, count=None, tokens=None, local_vars_configuration=None):  # noqa: E501
        """UserTokenResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._page_number = None
        self._count = None
        self._tokens = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if page_number is not None:
            self.page_number = page_number
        if count is not None:
            self.count = count
        self.tokens = tokens

    @property
    def success(self):
        """Gets the success of this UserTokenResponse.  # noqa: E501


        :return: The success of this UserTokenResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UserTokenResponse.


        :param success: The success of this UserTokenResponse.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def page_number(self):
        """Gets the page_number of this UserTokenResponse.  # noqa: E501


        :return: The page_number of this UserTokenResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this UserTokenResponse.


        :param page_number: The page_number of this UserTokenResponse.  # noqa: E501
        :type page_number: int
        """

        self._page_number = page_number

    @property
    def count(self):
        """Gets the count of this UserTokenResponse.  # noqa: E501


        :return: The count of this UserTokenResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this UserTokenResponse.


        :param count: The count of this UserTokenResponse.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def tokens(self):
        """Gets the tokens of this UserTokenResponse.  # noqa: E501


        :return: The tokens of this UserTokenResponse.  # noqa: E501
        :rtype: list[UserTokenDto]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this UserTokenResponse.


        :param tokens: The tokens of this UserTokenResponse.  # noqa: E501
        :type tokens: list[UserTokenDto]
        """

        self._tokens = tokens

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserTokenResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserTokenResponse):
            return True

        return self.to_dict() != other.to_dict()