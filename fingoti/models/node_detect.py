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


class NodeDetect(object):
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
        'serial': 'str',
        'address': 'int'
    }

    attribute_map = {
        'serial': 'serial',
        'address': 'address'
    }

    def __init__(self, serial=None, address=None, local_vars_configuration=None):  # noqa: E501
        """NodeDetect - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._serial = None
        self._address = None
        self.discriminator = None

        self.serial = serial
        if address is not None:
            self.address = address

    @property
    def serial(self):
        """Gets the serial of this NodeDetect.  # noqa: E501


        :return: The serial of this NodeDetect.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this NodeDetect.


        :param serial: The serial of this NodeDetect.  # noqa: E501
        :type serial: str
        """

        self._serial = serial

    @property
    def address(self):
        """Gets the address of this NodeDetect.  # noqa: E501


        :return: The address of this NodeDetect.  # noqa: E501
        :rtype: int
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NodeDetect.


        :param address: The address of this NodeDetect.  # noqa: E501
        :type address: int
        """

        self._address = address

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
        if not isinstance(other, NodeDetect):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeDetect):
            return True

        return self.to_dict() != other.to_dict()
