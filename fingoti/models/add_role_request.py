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


class AddRoleRequest(object):
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
        'role_name': 'str',
        'device': 'int',
        'organisation': 'int',
        'follow': 'int',
        'rule': 'int',
        'schedule': 'int',
        'user': 'int',
        'webhook': 'int',
        'partner': 'int',
        'billing': 'int'
    }

    attribute_map = {
        'role_name': 'roleName',
        'device': 'device',
        'organisation': 'organisation',
        'follow': 'follow',
        'rule': 'rule',
        'schedule': 'schedule',
        'user': 'user',
        'webhook': 'webhook',
        'partner': 'partner',
        'billing': 'billing'
    }

    def __init__(self, role_name=None, device=None, organisation=None, follow=None, rule=None, schedule=None, user=None, webhook=None, partner=None, billing=None, local_vars_configuration=None):  # noqa: E501
        """AddRoleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._role_name = None
        self._device = None
        self._organisation = None
        self._follow = None
        self._rule = None
        self._schedule = None
        self._user = None
        self._webhook = None
        self._partner = None
        self._billing = None
        self.discriminator = None

        self.role_name = role_name
        if device is not None:
            self.device = device
        if organisation is not None:
            self.organisation = organisation
        if follow is not None:
            self.follow = follow
        if rule is not None:
            self.rule = rule
        if schedule is not None:
            self.schedule = schedule
        if user is not None:
            self.user = user
        if webhook is not None:
            self.webhook = webhook
        if partner is not None:
            self.partner = partner
        if billing is not None:
            self.billing = billing

    @property
    def role_name(self):
        """Gets the role_name of this AddRoleRequest.  # noqa: E501


        :return: The role_name of this AddRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this AddRoleRequest.


        :param role_name: The role_name of this AddRoleRequest.  # noqa: E501
        :type role_name: str
        """
        if self.local_vars_configuration.client_side_validation and role_name is None:  # noqa: E501
            raise ValueError("Invalid value for `role_name`, must not be `None`")  # noqa: E501

        self._role_name = role_name

    @property
    def device(self):
        """Gets the device of this AddRoleRequest.  # noqa: E501


        :return: The device of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this AddRoleRequest.


        :param device: The device of this AddRoleRequest.  # noqa: E501
        :type device: int
        """

        self._device = device

    @property
    def organisation(self):
        """Gets the organisation of this AddRoleRequest.  # noqa: E501


        :return: The organisation of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this AddRoleRequest.


        :param organisation: The organisation of this AddRoleRequest.  # noqa: E501
        :type organisation: int
        """

        self._organisation = organisation

    @property
    def follow(self):
        """Gets the follow of this AddRoleRequest.  # noqa: E501


        :return: The follow of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._follow

    @follow.setter
    def follow(self, follow):
        """Sets the follow of this AddRoleRequest.


        :param follow: The follow of this AddRoleRequest.  # noqa: E501
        :type follow: int
        """

        self._follow = follow

    @property
    def rule(self):
        """Gets the rule of this AddRoleRequest.  # noqa: E501


        :return: The rule of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this AddRoleRequest.


        :param rule: The rule of this AddRoleRequest.  # noqa: E501
        :type rule: int
        """

        self._rule = rule

    @property
    def schedule(self):
        """Gets the schedule of this AddRoleRequest.  # noqa: E501


        :return: The schedule of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AddRoleRequest.


        :param schedule: The schedule of this AddRoleRequest.  # noqa: E501
        :type schedule: int
        """

        self._schedule = schedule

    @property
    def user(self):
        """Gets the user of this AddRoleRequest.  # noqa: E501


        :return: The user of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AddRoleRequest.


        :param user: The user of this AddRoleRequest.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def webhook(self):
        """Gets the webhook of this AddRoleRequest.  # noqa: E501


        :return: The webhook of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this AddRoleRequest.


        :param webhook: The webhook of this AddRoleRequest.  # noqa: E501
        :type webhook: int
        """

        self._webhook = webhook

    @property
    def partner(self):
        """Gets the partner of this AddRoleRequest.  # noqa: E501


        :return: The partner of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this AddRoleRequest.


        :param partner: The partner of this AddRoleRequest.  # noqa: E501
        :type partner: int
        """

        self._partner = partner

    @property
    def billing(self):
        """Gets the billing of this AddRoleRequest.  # noqa: E501


        :return: The billing of this AddRoleRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this AddRoleRequest.


        :param billing: The billing of this AddRoleRequest.  # noqa: E501
        :type billing: int
        """

        self._billing = billing

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
        if not isinstance(other, AddRoleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddRoleRequest):
            return True

        return self.to_dict() != other.to_dict()
