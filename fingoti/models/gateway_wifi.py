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


class GatewayWifi(object):
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
        'credentials': 'list[str]',
        'status': 'WifiStatus',
        'detect': 'list[WifiDetect]'
    }

    attribute_map = {
        'credentials': 'credentials',
        'status': 'status',
        'detect': 'detect'
    }

    def __init__(self, credentials=None, status=None, detect=None, local_vars_configuration=None):  # noqa: E501
        """GatewayWifi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._credentials = None
        self._status = None
        self._detect = None
        self.discriminator = None

        self.credentials = credentials
        if status is not None:
            self.status = status
        self.detect = detect

    @property
    def credentials(self):
        """Gets the credentials of this GatewayWifi.  # noqa: E501


        :return: The credentials of this GatewayWifi.  # noqa: E501
        :rtype: list[str]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this GatewayWifi.


        :param credentials: The credentials of this GatewayWifi.  # noqa: E501
        :type credentials: list[str]
        """

        self._credentials = credentials

    @property
    def status(self):
        """Gets the status of this GatewayWifi.  # noqa: E501


        :return: The status of this GatewayWifi.  # noqa: E501
        :rtype: WifiStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GatewayWifi.


        :param status: The status of this GatewayWifi.  # noqa: E501
        :type status: WifiStatus
        """

        self._status = status

    @property
    def detect(self):
        """Gets the detect of this GatewayWifi.  # noqa: E501


        :return: The detect of this GatewayWifi.  # noqa: E501
        :rtype: list[WifiDetect]
        """
        return self._detect

    @detect.setter
    def detect(self, detect):
        """Sets the detect of this GatewayWifi.


        :param detect: The detect of this GatewayWifi.  # noqa: E501
        :type detect: list[WifiDetect]
        """

        self._detect = detect

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
        if not isinstance(other, GatewayWifi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayWifi):
            return True

        return self.to_dict() != other.to_dict()