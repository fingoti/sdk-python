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


class PatchUserRequest(object):
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
        'forename': 'str',
        'surname': 'str',
        'mobile': 'str',
        'telephone': 'str',
        'marketing': 'bool',
        'default_organisation': 'str'
    }

    attribute_map = {
        'forename': 'forename',
        'surname': 'surname',
        'mobile': 'mobile',
        'telephone': 'telephone',
        'marketing': 'marketing',
        'default_organisation': 'defaultOrganisation'
    }

    def __init__(self, forename=None, surname=None, mobile=None, telephone=None, marketing=None, default_organisation=None, local_vars_configuration=None):  # noqa: E501
        """PatchUserRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._forename = None
        self._surname = None
        self._mobile = None
        self._telephone = None
        self._marketing = None
        self._default_organisation = None
        self.discriminator = None

        self.forename = forename
        self.surname = surname
        self.mobile = mobile
        self.telephone = telephone
        self.marketing = marketing
        self.default_organisation = default_organisation

    @property
    def forename(self):
        """Gets the forename of this PatchUserRequest.  # noqa: E501


        :return: The forename of this PatchUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._forename

    @forename.setter
    def forename(self, forename):
        """Sets the forename of this PatchUserRequest.


        :param forename: The forename of this PatchUserRequest.  # noqa: E501
        :type forename: str
        """

        self._forename = forename

    @property
    def surname(self):
        """Gets the surname of this PatchUserRequest.  # noqa: E501


        :return: The surname of this PatchUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this PatchUserRequest.


        :param surname: The surname of this PatchUserRequest.  # noqa: E501
        :type surname: str
        """

        self._surname = surname

    @property
    def mobile(self):
        """Gets the mobile of this PatchUserRequest.  # noqa: E501


        :return: The mobile of this PatchUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this PatchUserRequest.


        :param mobile: The mobile of this PatchUserRequest.  # noqa: E501
        :type mobile: str
        """

        self._mobile = mobile

    @property
    def telephone(self):
        """Gets the telephone of this PatchUserRequest.  # noqa: E501


        :return: The telephone of this PatchUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PatchUserRequest.


        :param telephone: The telephone of this PatchUserRequest.  # noqa: E501
        :type telephone: str
        """

        self._telephone = telephone

    @property
    def marketing(self):
        """Gets the marketing of this PatchUserRequest.  # noqa: E501


        :return: The marketing of this PatchUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._marketing

    @marketing.setter
    def marketing(self, marketing):
        """Sets the marketing of this PatchUserRequest.


        :param marketing: The marketing of this PatchUserRequest.  # noqa: E501
        :type marketing: bool
        """

        self._marketing = marketing

    @property
    def default_organisation(self):
        """Gets the default_organisation of this PatchUserRequest.  # noqa: E501


        :return: The default_organisation of this PatchUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_organisation

    @default_organisation.setter
    def default_organisation(self, default_organisation):
        """Sets the default_organisation of this PatchUserRequest.


        :param default_organisation: The default_organisation of this PatchUserRequest.  # noqa: E501
        :type default_organisation: str
        """

        self._default_organisation = default_organisation

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
        if not isinstance(other, PatchUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchUserRequest):
            return True

        return self.to_dict() != other.to_dict()
