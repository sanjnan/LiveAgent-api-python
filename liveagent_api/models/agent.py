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


class Agent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Agent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'email': 'str',
            'role': 'str',
            'avatar_url': 'str',
            'online_status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'role': 'role',
            'avatar_url': 'avatar_url',
            'online_status': 'online_status'
        }

        self._id = None
        self._name = None
        self._email = None
        self._role = None
        self._avatar_url = None
        self._online_status = None

    @property
    def id(self):
        """
        Gets the id of this Agent.


        :return: The id of this Agent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Agent.


        :param id: The id of this Agent.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Agent.


        :return: The name of this Agent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Agent.


        :param name: The name of this Agent.
        :type: str
        """
        self._name = name

    @property
    def email(self):
        """
        Gets the email of this Agent.


        :return: The email of this Agent.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Agent.


        :param email: The email of this Agent.
        :type: str
        """
        self._email = email

    @property
    def role(self):
        """
        Gets the role of this Agent.


        :return: The role of this Agent.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Agent.


        :param role: The role of this Agent.
        :type: str
        """
        allowed_values = ["owner", "admin", "agent"]
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role`, must be one of {0}"
                .format(allowed_values)
            )
        self._role = role

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this Agent.


        :return: The avatar_url of this Agent.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this Agent.


        :param avatar_url: The avatar_url of this Agent.
        :type: str
        """
        self._avatar_url = avatar_url

    @property
    def online_status(self):
        """
        Gets the online_status of this Agent.


        :return: The online_status of this Agent.
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """
        Sets the online_status of this Agent.


        :param online_status: The online_status of this Agent.
        :type: str
        """
        self._online_status = online_status

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

