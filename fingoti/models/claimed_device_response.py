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


class ClaimedDeviceResponse(object):
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
        'pebl': 'DevicePeblDto',
        'vyne': 'DeviceVyneDto'
    }

    attribute_map = {
        'success': 'success',
        'pebl': 'pebl',
        'vyne': 'vyne'
    }

    def __init__(self, success=None, pebl=None, vyne=None, local_vars_configuration=None):  # noqa: E501
        """ClaimedDeviceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._pebl = None
        self._vyne = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if pebl is not None:
            self.pebl = pebl
        if vyne is not None:
            self.vyne = vyne

    @property
    def success(self):
        """Gets the success of this ClaimedDeviceResponse.  # noqa: E501


        :return: The success of this ClaimedDeviceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ClaimedDeviceResponse.


        :param success: The success of this ClaimedDeviceResponse.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def pebl(self):
        """Gets the pebl of this ClaimedDeviceResponse.  # noqa: E501


        :return: The pebl of this ClaimedDeviceResponse.  # noqa: E501
        :rtype: DevicePeblDto
        """
        return self._pebl

    @pebl.setter
    def pebl(self, pebl):
        """Sets the pebl of this ClaimedDeviceResponse.


        :param pebl: The pebl of this ClaimedDeviceResponse.  # noqa: E501
        :type pebl: DevicePeblDto
        """

        self._pebl = pebl

    @property
    def vyne(self):
        """Gets the vyne of this ClaimedDeviceResponse.  # noqa: E501


        :return: The vyne of this ClaimedDeviceResponse.  # noqa: E501
        :rtype: DeviceVyneDto
        """
        return self._vyne

    @vyne.setter
    def vyne(self, vyne):
        """Sets the vyne of this ClaimedDeviceResponse.


        :param vyne: The vyne of this ClaimedDeviceResponse.  # noqa: E501
        :type vyne: DeviceVyneDto
        """

        self._vyne = vyne

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
        if not isinstance(other, ClaimedDeviceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClaimedDeviceResponse):
            return True

        return self.to_dict() != other.to_dict()
