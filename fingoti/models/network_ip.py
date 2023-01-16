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


class NetworkIp(object):
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
        'public': 'str',
        'local': 'str',
        'mask': 'str',
        'gateway': 'str',
        'dns': 'str',
        'dhcp': 'bool'
    }

    attribute_map = {
        'public': 'public',
        'local': 'local',
        'mask': 'mask',
        'gateway': 'gateway',
        'dns': 'dns',
        'dhcp': 'dhcp'
    }

    def __init__(self, public=None, local=None, mask=None, gateway=None, dns=None, dhcp=None, local_vars_configuration=None):  # noqa: E501
        """NetworkIp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._public = None
        self._local = None
        self._mask = None
        self._gateway = None
        self._dns = None
        self._dhcp = None
        self.discriminator = None

        self.public = public
        self.local = local
        self.mask = mask
        self.gateway = gateway
        self.dns = dns
        if dhcp is not None:
            self.dhcp = dhcp

    @property
    def public(self):
        """Gets the public of this NetworkIp.  # noqa: E501


        :return: The public of this NetworkIp.  # noqa: E501
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NetworkIp.


        :param public: The public of this NetworkIp.  # noqa: E501
        :type public: str
        """

        self._public = public

    @property
    def local(self):
        """Gets the local of this NetworkIp.  # noqa: E501


        :return: The local of this NetworkIp.  # noqa: E501
        :rtype: str
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this NetworkIp.


        :param local: The local of this NetworkIp.  # noqa: E501
        :type local: str
        """

        self._local = local

    @property
    def mask(self):
        """Gets the mask of this NetworkIp.  # noqa: E501


        :return: The mask of this NetworkIp.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this NetworkIp.


        :param mask: The mask of this NetworkIp.  # noqa: E501
        :type mask: str
        """

        self._mask = mask

    @property
    def gateway(self):
        """Gets the gateway of this NetworkIp.  # noqa: E501


        :return: The gateway of this NetworkIp.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NetworkIp.


        :param gateway: The gateway of this NetworkIp.  # noqa: E501
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def dns(self):
        """Gets the dns of this NetworkIp.  # noqa: E501


        :return: The dns of this NetworkIp.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this NetworkIp.


        :param dns: The dns of this NetworkIp.  # noqa: E501
        :type dns: str
        """

        self._dns = dns

    @property
    def dhcp(self):
        """Gets the dhcp of this NetworkIp.  # noqa: E501


        :return: The dhcp of this NetworkIp.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this NetworkIp.


        :param dhcp: The dhcp of this NetworkIp.  # noqa: E501
        :type dhcp: bool
        """

        self._dhcp = dhcp

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
        if not isinstance(other, NetworkIp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkIp):
            return True

        return self.to_dict() != other.to_dict()