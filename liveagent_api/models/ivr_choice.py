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


class IvrChoice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IvrChoice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dtmf': 'str',
            'play': 'str',
            'name': 'str',
            'ivr': 'str'
        }

        self.attribute_map = {
            'dtmf': 'dtmf',
            'play': 'play',
            'name': 'name',
            'ivr': 'ivr'
        }

        self._dtmf = None
        self._play = None
        self._name = None
        self._ivr = None

    @property
    def dtmf(self):
        """
        Gets the dtmf of this IvrChoice.
        DTMF symbol of choice

        :return: The dtmf of this IvrChoice.
        :rtype: str
        """
        return self._dtmf

    @dtmf.setter
    def dtmf(self, dtmf):
        """
        Sets the dtmf of this IvrChoice.
        DTMF symbol of choice

        :param dtmf: The dtmf of this IvrChoice.
        :type: str
        """
        allowed_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"]
        if dtmf not in allowed_values:
            raise ValueError(
                "Invalid value for `dtmf`, must be one of {0}"
                .format(allowed_values)
            )
        self._dtmf = dtmf

    @property
    def play(self):
        """
        Gets the play of this IvrChoice.
        URL of the sound to play

        :return: The play of this IvrChoice.
        :rtype: str
        """
        return self._play

    @play.setter
    def play(self, play):
        """
        Sets the play of this IvrChoice.
        URL of the sound to play

        :param play: The play of this IvrChoice.
        :type: str
        """
        self._play = play

    @property
    def name(self):
        """
        Gets the name of this IvrChoice.
        Readable name of choice

        :return: The name of this IvrChoice.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IvrChoice.
        Readable name of choice

        :param name: The name of this IvrChoice.
        :type: str
        """
        self._name = name

    @property
    def ivr(self):
        """
        Gets the ivr of this IvrChoice.
        Name of IVR to continue in

        :return: The ivr of this IvrChoice.
        :rtype: str
        """
        return self._ivr

    @ivr.setter
    def ivr(self, ivr):
        """
        Sets the ivr of this IvrChoice.
        Name of IVR to continue in

        :param ivr: The ivr of this IvrChoice.
        :type: str
        """
        self._ivr = ivr

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

