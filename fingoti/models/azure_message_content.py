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


class AzureMessageContent(object):
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
        'serial': 'str',
        '_property': 'str',
        'result': 'object',
        'error': 'object'
    }

    attribute_map = {
        'success': 'success',
        'serial': 'serial',
        '_property': 'property',
        'result': 'result',
        'error': 'error'
    }

    def __init__(self, success=None, serial=None, _property=None, result=None, error=None, local_vars_configuration=None):  # noqa: E501
        """AzureMessageContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._serial = None
        self.__property = None
        self._result = None
        self._error = None
        self.discriminator = None

        self.success = success
        self.serial = serial
        self._property = _property
        self.result = result
        self.error = error

    @property
    def success(self):
        """Gets the success of this AzureMessageContent.  # noqa: E501


        :return: The success of this AzureMessageContent.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this AzureMessageContent.


        :param success: The success of this AzureMessageContent.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def serial(self):
        """Gets the serial of this AzureMessageContent.  # noqa: E501


        :return: The serial of this AzureMessageContent.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this AzureMessageContent.


        :param serial: The serial of this AzureMessageContent.  # noqa: E501
        :type serial: str
        """

        self._serial = serial

    @property
    def _property(self):
        """Gets the _property of this AzureMessageContent.  # noqa: E501


        :return: The _property of this AzureMessageContent.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this AzureMessageContent.


        :param _property: The _property of this AzureMessageContent.  # noqa: E501
        :type _property: str
        """

        self.__property = _property

    @property
    def result(self):
        """Gets the result of this AzureMessageContent.  # noqa: E501


        :return: The result of this AzureMessageContent.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AzureMessageContent.


        :param result: The result of this AzureMessageContent.  # noqa: E501
        :type result: object
        """

        self._result = result

    @property
    def error(self):
        """Gets the error of this AzureMessageContent.  # noqa: E501


        :return: The error of this AzureMessageContent.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AzureMessageContent.


        :param error: The error of this AzureMessageContent.  # noqa: E501
        :type error: object
        """

        self._error = error

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
        if not isinstance(other, AzureMessageContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureMessageContent):
            return True

        return self.to_dict() != other.to_dict()
