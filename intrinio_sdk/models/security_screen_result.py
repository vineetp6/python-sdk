# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.26.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.security_screen_result_data import SecurityScreenResultData  # noqa: F401,E501
from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501


class SecurityScreenResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'security': 'SecuritySummary',
        'data': 'list[SecurityScreenResultData]'
    }

    attribute_map = {
        'security': 'security',
        'data': 'data'
    }

    def __init__(self, security=None, data=None):  # noqa: E501
        """SecurityScreenResult - a model defined in Swagger"""  # noqa: E501

        self._security = None
        self._data = None
        self.discriminator = None

        if security is not None:
            self.security = security
        if data is not None:
            self.data = data

    @property
    def security(self):
        """Gets the security of this SecurityScreenResult.  # noqa: E501


        :return: The security of this SecurityScreenResult.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security
        
    @property
    def security_dict(self):
        """Gets the security of this SecurityScreenResult.  # noqa: E501


        :return: The security of this SecurityScreenResult.  # noqa: E501
        :rtype: SecuritySummary
        """

        result = None

        value = self.security
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'security': value }

        
        return result
        

    @security.setter
    def security(self, security):
        """Sets the security of this SecurityScreenResult.


        :param security: The security of this SecurityScreenResult.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

    @property
    def data(self):
        """Gets the data of this SecurityScreenResult.  # noqa: E501


        :return: The data of this SecurityScreenResult.  # noqa: E501
        :rtype: list[SecurityScreenResultData]
        """
        return self._data
        
    @property
    def data_dict(self):
        """Gets the data of this SecurityScreenResult.  # noqa: E501


        :return: The data of this SecurityScreenResult.  # noqa: E501
        :rtype: list[SecurityScreenResultData]
        """

        result = None

        value = self.data
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'data': value }

        
        return result
        

    @data.setter
    def data(self, data):
        """Sets the data of this SecurityScreenResult.


        :param data: The data of this SecurityScreenResult.  # noqa: E501
        :type: list[SecurityScreenResultData]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityScreenResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
