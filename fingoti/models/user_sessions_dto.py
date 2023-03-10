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


class UserSessionsDto(object):
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
        'id': 'str',
        'user_agent': 'str',
        'platform': 'str',
        'client': 'str',
        'login_time': 'datetime',
        'last_active': 'datetime',
        'location': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_agent': 'userAgent',
        'platform': 'platform',
        'client': 'client',
        'login_time': 'loginTime',
        'last_active': 'lastActive',
        'location': 'location',
        'ip_address': 'ipAddress'
    }

    def __init__(self, id=None, user_agent=None, platform=None, client=None, login_time=None, last_active=None, location=None, ip_address=None, local_vars_configuration=None):  # noqa: E501
        """UserSessionsDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_agent = None
        self._platform = None
        self._client = None
        self._login_time = None
        self._last_active = None
        self._location = None
        self._ip_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.user_agent = user_agent
        self.platform = platform
        self.client = client
        self.login_time = login_time
        self.last_active = last_active
        self.location = location
        self.ip_address = ip_address

    @property
    def id(self):
        """Gets the id of this UserSessionsDto.  # noqa: E501


        :return: The id of this UserSessionsDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSessionsDto.


        :param id: The id of this UserSessionsDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def user_agent(self):
        """Gets the user_agent of this UserSessionsDto.  # noqa: E501


        :return: The user_agent of this UserSessionsDto.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this UserSessionsDto.


        :param user_agent: The user_agent of this UserSessionsDto.  # noqa: E501
        :type user_agent: str
        """

        self._user_agent = user_agent

    @property
    def platform(self):
        """Gets the platform of this UserSessionsDto.  # noqa: E501


        :return: The platform of this UserSessionsDto.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UserSessionsDto.


        :param platform: The platform of this UserSessionsDto.  # noqa: E501
        :type platform: str
        """

        self._platform = platform

    @property
    def client(self):
        """Gets the client of this UserSessionsDto.  # noqa: E501


        :return: The client of this UserSessionsDto.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this UserSessionsDto.


        :param client: The client of this UserSessionsDto.  # noqa: E501
        :type client: str
        """

        self._client = client

    @property
    def login_time(self):
        """Gets the login_time of this UserSessionsDto.  # noqa: E501


        :return: The login_time of this UserSessionsDto.  # noqa: E501
        :rtype: datetime
        """
        return self._login_time

    @login_time.setter
    def login_time(self, login_time):
        """Sets the login_time of this UserSessionsDto.


        :param login_time: The login_time of this UserSessionsDto.  # noqa: E501
        :type login_time: datetime
        """

        self._login_time = login_time

    @property
    def last_active(self):
        """Gets the last_active of this UserSessionsDto.  # noqa: E501


        :return: The last_active of this UserSessionsDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_active

    @last_active.setter
    def last_active(self, last_active):
        """Sets the last_active of this UserSessionsDto.


        :param last_active: The last_active of this UserSessionsDto.  # noqa: E501
        :type last_active: datetime
        """

        self._last_active = last_active

    @property
    def location(self):
        """Gets the location of this UserSessionsDto.  # noqa: E501


        :return: The location of this UserSessionsDto.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UserSessionsDto.


        :param location: The location of this UserSessionsDto.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def ip_address(self):
        """Gets the ip_address of this UserSessionsDto.  # noqa: E501


        :return: The ip_address of this UserSessionsDto.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this UserSessionsDto.


        :param ip_address: The ip_address of this UserSessionsDto.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

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
        if not isinstance(other, UserSessionsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSessionsDto):
            return True

        return self.to_dict() != other.to_dict()
