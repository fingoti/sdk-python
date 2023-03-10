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


class OrganisationUsersDto(object):
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
        'forename': 'str',
        'surname': 'str',
        'user_handle': 'str',
        'email': 'str',
        'email_verified': 'bool',
        'role_id': 'str',
        'disabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'forename': 'forename',
        'surname': 'surname',
        'user_handle': 'userHandle',
        'email': 'email',
        'email_verified': 'emailVerified',
        'role_id': 'roleId',
        'disabled': 'disabled'
    }

    def __init__(self, id=None, forename=None, surname=None, user_handle=None, email=None, email_verified=None, role_id=None, disabled=None, local_vars_configuration=None):  # noqa: E501
        """OrganisationUsersDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._forename = None
        self._surname = None
        self._user_handle = None
        self._email = None
        self._email_verified = None
        self._role_id = None
        self._disabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.forename = forename
        self.surname = surname
        self.user_handle = user_handle
        self.email = email
        if email_verified is not None:
            self.email_verified = email_verified
        self.role_id = role_id
        if disabled is not None:
            self.disabled = disabled

    @property
    def id(self):
        """Gets the id of this OrganisationUsersDto.  # noqa: E501


        :return: The id of this OrganisationUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganisationUsersDto.


        :param id: The id of this OrganisationUsersDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def forename(self):
        """Gets the forename of this OrganisationUsersDto.  # noqa: E501


        :return: The forename of this OrganisationUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._forename

    @forename.setter
    def forename(self, forename):
        """Sets the forename of this OrganisationUsersDto.


        :param forename: The forename of this OrganisationUsersDto.  # noqa: E501
        :type forename: str
        """

        self._forename = forename

    @property
    def surname(self):
        """Gets the surname of this OrganisationUsersDto.  # noqa: E501


        :return: The surname of this OrganisationUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this OrganisationUsersDto.


        :param surname: The surname of this OrganisationUsersDto.  # noqa: E501
        :type surname: str
        """

        self._surname = surname

    @property
    def user_handle(self):
        """Gets the user_handle of this OrganisationUsersDto.  # noqa: E501


        :return: The user_handle of this OrganisationUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._user_handle

    @user_handle.setter
    def user_handle(self, user_handle):
        """Sets the user_handle of this OrganisationUsersDto.


        :param user_handle: The user_handle of this OrganisationUsersDto.  # noqa: E501
        :type user_handle: str
        """

        self._user_handle = user_handle

    @property
    def email(self):
        """Gets the email of this OrganisationUsersDto.  # noqa: E501


        :return: The email of this OrganisationUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrganisationUsersDto.


        :param email: The email of this OrganisationUsersDto.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def email_verified(self):
        """Gets the email_verified of this OrganisationUsersDto.  # noqa: E501


        :return: The email_verified of this OrganisationUsersDto.  # noqa: E501
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this OrganisationUsersDto.


        :param email_verified: The email_verified of this OrganisationUsersDto.  # noqa: E501
        :type email_verified: bool
        """

        self._email_verified = email_verified

    @property
    def role_id(self):
        """Gets the role_id of this OrganisationUsersDto.  # noqa: E501


        :return: The role_id of this OrganisationUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this OrganisationUsersDto.


        :param role_id: The role_id of this OrganisationUsersDto.  # noqa: E501
        :type role_id: str
        """

        self._role_id = role_id

    @property
    def disabled(self):
        """Gets the disabled of this OrganisationUsersDto.  # noqa: E501


        :return: The disabled of this OrganisationUsersDto.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this OrganisationUsersDto.


        :param disabled: The disabled of this OrganisationUsersDto.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

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
        if not isinstance(other, OrganisationUsersDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganisationUsersDto):
            return True

        return self.to_dict() != other.to_dict()
