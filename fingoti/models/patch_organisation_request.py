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


class PatchOrganisationRequest(object):
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
        'organisation_name': 'str',
        'vat_number': 'str',
        'main_contact': 'str',
        'main_address': 'str',
        'billing_contact': 'str',
        'billing_address': 'str',
        'delivery_contact': 'str',
        'delivery_address': 'str'
    }

    attribute_map = {
        'organisation_name': 'organisationName',
        'vat_number': 'vatNumber',
        'main_contact': 'mainContact',
        'main_address': 'mainAddress',
        'billing_contact': 'billingContact',
        'billing_address': 'billingAddress',
        'delivery_contact': 'deliveryContact',
        'delivery_address': 'deliveryAddress'
    }

    def __init__(self, organisation_name=None, vat_number=None, main_contact=None, main_address=None, billing_contact=None, billing_address=None, delivery_contact=None, delivery_address=None, local_vars_configuration=None):  # noqa: E501
        """PatchOrganisationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._organisation_name = None
        self._vat_number = None
        self._main_contact = None
        self._main_address = None
        self._billing_contact = None
        self._billing_address = None
        self._delivery_contact = None
        self._delivery_address = None
        self.discriminator = None

        self.organisation_name = organisation_name
        self.vat_number = vat_number
        self.main_contact = main_contact
        self.main_address = main_address
        self.billing_contact = billing_contact
        self.billing_address = billing_address
        self.delivery_contact = delivery_contact
        self.delivery_address = delivery_address

    @property
    def organisation_name(self):
        """Gets the organisation_name of this PatchOrganisationRequest.  # noqa: E501


        :return: The organisation_name of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this PatchOrganisationRequest.


        :param organisation_name: The organisation_name of this PatchOrganisationRequest.  # noqa: E501
        :type organisation_name: str
        """

        self._organisation_name = organisation_name

    @property
    def vat_number(self):
        """Gets the vat_number of this PatchOrganisationRequest.  # noqa: E501


        :return: The vat_number of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """Sets the vat_number of this PatchOrganisationRequest.


        :param vat_number: The vat_number of this PatchOrganisationRequest.  # noqa: E501
        :type vat_number: str
        """

        self._vat_number = vat_number

    @property
    def main_contact(self):
        """Gets the main_contact of this PatchOrganisationRequest.  # noqa: E501


        :return: The main_contact of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._main_contact

    @main_contact.setter
    def main_contact(self, main_contact):
        """Sets the main_contact of this PatchOrganisationRequest.


        :param main_contact: The main_contact of this PatchOrganisationRequest.  # noqa: E501
        :type main_contact: str
        """

        self._main_contact = main_contact

    @property
    def main_address(self):
        """Gets the main_address of this PatchOrganisationRequest.  # noqa: E501


        :return: The main_address of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        """Sets the main_address of this PatchOrganisationRequest.


        :param main_address: The main_address of this PatchOrganisationRequest.  # noqa: E501
        :type main_address: str
        """

        self._main_address = main_address

    @property
    def billing_contact(self):
        """Gets the billing_contact of this PatchOrganisationRequest.  # noqa: E501


        :return: The billing_contact of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._billing_contact

    @billing_contact.setter
    def billing_contact(self, billing_contact):
        """Sets the billing_contact of this PatchOrganisationRequest.


        :param billing_contact: The billing_contact of this PatchOrganisationRequest.  # noqa: E501
        :type billing_contact: str
        """

        self._billing_contact = billing_contact

    @property
    def billing_address(self):
        """Gets the billing_address of this PatchOrganisationRequest.  # noqa: E501


        :return: The billing_address of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this PatchOrganisationRequest.


        :param billing_address: The billing_address of this PatchOrganisationRequest.  # noqa: E501
        :type billing_address: str
        """

        self._billing_address = billing_address

    @property
    def delivery_contact(self):
        """Gets the delivery_contact of this PatchOrganisationRequest.  # noqa: E501


        :return: The delivery_contact of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._delivery_contact

    @delivery_contact.setter
    def delivery_contact(self, delivery_contact):
        """Sets the delivery_contact of this PatchOrganisationRequest.


        :param delivery_contact: The delivery_contact of this PatchOrganisationRequest.  # noqa: E501
        :type delivery_contact: str
        """

        self._delivery_contact = delivery_contact

    @property
    def delivery_address(self):
        """Gets the delivery_address of this PatchOrganisationRequest.  # noqa: E501


        :return: The delivery_address of this PatchOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this PatchOrganisationRequest.


        :param delivery_address: The delivery_address of this PatchOrganisationRequest.  # noqa: E501
        :type delivery_address: str
        """

        self._delivery_address = delivery_address

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
        if not isinstance(other, PatchOrganisationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchOrganisationRequest):
            return True

        return self.to_dict() != other.to_dict()
