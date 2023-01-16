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


class NewOrganisationTokenDto(object):
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
        'expiry': 'datetime',
        'token_name': 'str',
        'role_id': 'str',
        'assigned_users': 'list[str]'
    }

    attribute_map = {
        'expiry': 'expiry',
        'token_name': 'tokenName',
        'role_id': 'roleId',
        'assigned_users': 'assignedUsers'
    }

    def __init__(self, expiry=None, token_name=None, role_id=None, assigned_users=None, local_vars_configuration=None):  # noqa: E501
        """NewOrganisationTokenDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._expiry = None
        self._token_name = None
        self._role_id = None
        self._assigned_users = None
        self.discriminator = None

        self.expiry = expiry
        self.token_name = token_name
        self.role_id = role_id
        self.assigned_users = assigned_users

    @property
    def expiry(self):
        """Gets the expiry of this NewOrganisationTokenDto.  # noqa: E501


        :return: The expiry of this NewOrganisationTokenDto.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this NewOrganisationTokenDto.


        :param expiry: The expiry of this NewOrganisationTokenDto.  # noqa: E501
        :type expiry: datetime
        """

        self._expiry = expiry

    @property
    def token_name(self):
        """Gets the token_name of this NewOrganisationTokenDto.  # noqa: E501


        :return: The token_name of this NewOrganisationTokenDto.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this NewOrganisationTokenDto.


        :param token_name: The token_name of this NewOrganisationTokenDto.  # noqa: E501
        :type token_name: str
        """
        if self.local_vars_configuration.client_side_validation and token_name is None:  # noqa: E501
            raise ValueError("Invalid value for `token_name`, must not be `None`")  # noqa: E501

        self._token_name = token_name

    @property
    def role_id(self):
        """Gets the role_id of this NewOrganisationTokenDto.  # noqa: E501


        :return: The role_id of this NewOrganisationTokenDto.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this NewOrganisationTokenDto.


        :param role_id: The role_id of this NewOrganisationTokenDto.  # noqa: E501
        :type role_id: str
        """
        if self.local_vars_configuration.client_side_validation and role_id is None:  # noqa: E501
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def assigned_users(self):
        """Gets the assigned_users of this NewOrganisationTokenDto.  # noqa: E501


        :return: The assigned_users of this NewOrganisationTokenDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._assigned_users

    @assigned_users.setter
    def assigned_users(self, assigned_users):
        """Sets the assigned_users of this NewOrganisationTokenDto.


        :param assigned_users: The assigned_users of this NewOrganisationTokenDto.  # noqa: E501
        :type assigned_users: list[str]
        """

        self._assigned_users = assigned_users

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
        if not isinstance(other, NewOrganisationTokenDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewOrganisationTokenDto):
            return True

        return self.to_dict() != other.to_dict()
