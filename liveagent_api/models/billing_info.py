# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class BillingInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BillingInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'force': 'bool',
            'name': 'str',
            'email': 'str',
            'company': 'str',
            'phone': 'str',
            'address1': 'str',
            'address2': 'str',
            'city': 'str',
            'state': 'str',
            'country': 'str',
            'zip': 'str',
            'vat_id': 'str',
            'ico_sk': 'str',
            'dic_sk': 'str'
        }

        self.attribute_map = {
            'force': 'force',
            'name': 'name',
            'email': 'email',
            'company': 'company',
            'phone': 'phone',
            'address1': 'address1',
            'address2': 'address2',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'zip': 'zip',
            'vat_id': 'vat_id',
            'ico_sk': 'ico_sk',
            'dic_sk': 'dic_sk'
        }

        self._force = False
        self._name = None
        self._email = None
        self._company = None
        self._phone = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._country = None
        self._zip = None
        self._vat_id = None
        self._ico_sk = None
        self._dic_sk = None

    @property
    def force(self):
        """
        Gets the force of this BillingInfo.


        :return: The force of this BillingInfo.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """
        Sets the force of this BillingInfo.


        :param force: The force of this BillingInfo.
        :type: bool
        """
        self._force = force

    @property
    def name(self):
        """
        Gets the name of this BillingInfo.


        :return: The name of this BillingInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BillingInfo.


        :param name: The name of this BillingInfo.
        :type: str
        """
        self._name = name

    @property
    def email(self):
        """
        Gets the email of this BillingInfo.


        :return: The email of this BillingInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this BillingInfo.


        :param email: The email of this BillingInfo.
        :type: str
        """
        self._email = email

    @property
    def company(self):
        """
        Gets the company of this BillingInfo.


        :return: The company of this BillingInfo.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this BillingInfo.


        :param company: The company of this BillingInfo.
        :type: str
        """
        self._company = company

    @property
    def phone(self):
        """
        Gets the phone of this BillingInfo.


        :return: The phone of this BillingInfo.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this BillingInfo.


        :param phone: The phone of this BillingInfo.
        :type: str
        """
        self._phone = phone

    @property
    def address1(self):
        """
        Gets the address1 of this BillingInfo.


        :return: The address1 of this BillingInfo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this BillingInfo.


        :param address1: The address1 of this BillingInfo.
        :type: str
        """
        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this BillingInfo.


        :return: The address2 of this BillingInfo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this BillingInfo.


        :param address2: The address2 of this BillingInfo.
        :type: str
        """
        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this BillingInfo.


        :return: The city of this BillingInfo.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this BillingInfo.


        :param city: The city of this BillingInfo.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this BillingInfo.


        :return: The state of this BillingInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this BillingInfo.


        :param state: The state of this BillingInfo.
        :type: str
        """
        self._state = state

    @property
    def country(self):
        """
        Gets the country of this BillingInfo.


        :return: The country of this BillingInfo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingInfo.


        :param country: The country of this BillingInfo.
        :type: str
        """
        self._country = country

    @property
    def zip(self):
        """
        Gets the zip of this BillingInfo.


        :return: The zip of this BillingInfo.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this BillingInfo.


        :param zip: The zip of this BillingInfo.
        :type: str
        """
        self._zip = zip

    @property
    def vat_id(self):
        """
        Gets the vat_id of this BillingInfo.


        :return: The vat_id of this BillingInfo.
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """
        Sets the vat_id of this BillingInfo.


        :param vat_id: The vat_id of this BillingInfo.
        :type: str
        """
        self._vat_id = vat_id

    @property
    def ico_sk(self):
        """
        Gets the ico_sk of this BillingInfo.


        :return: The ico_sk of this BillingInfo.
        :rtype: str
        """
        return self._ico_sk

    @ico_sk.setter
    def ico_sk(self, ico_sk):
        """
        Sets the ico_sk of this BillingInfo.


        :param ico_sk: The ico_sk of this BillingInfo.
        :type: str
        """
        self._ico_sk = ico_sk

    @property
    def dic_sk(self):
        """
        Gets the dic_sk of this BillingInfo.


        :return: The dic_sk of this BillingInfo.
        :rtype: str
        """
        return self._dic_sk

    @dic_sk.setter
    def dic_sk(self, dic_sk):
        """
        Sets the dic_sk of this BillingInfo.


        :param dic_sk: The dic_sk of this BillingInfo.
        :type: str
        """
        self._dic_sk = dic_sk

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

