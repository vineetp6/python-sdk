# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.21.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ForexPair(object):
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
        'code': 'str',
        'base_currency': 'str',
        'quote_currency': 'str'
    }

    attribute_map = {
        'code': 'code',
        'base_currency': 'base_currency',
        'quote_currency': 'quote_currency'
    }

    def __init__(self, code=None, base_currency=None, quote_currency=None):  # noqa: E501
        """ForexPair - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._base_currency = None
        self._quote_currency = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if base_currency is not None:
            self.base_currency = base_currency
        if quote_currency is not None:
            self.quote_currency = quote_currency

    @property
    def code(self):
        """Gets the code of this ForexPair.  # noqa: E501

        The common code of the currency pair  # noqa: E501

        :return: The code of this ForexPair.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this ForexPair.  # noqa: E501

        The common code of the currency pair as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this ForexPair.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.code
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
            result = { 'code': value }

        
        return result
        

    @code.setter
    def code(self, code):
        """Sets the code of this ForexPair.

        The common code of the currency pair  # noqa: E501

        :param code: The code of this ForexPair.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def base_currency(self):
        """Gets the base_currency of this ForexPair.  # noqa: E501

        The ISO 4217 currency code of the base currency  # noqa: E501

        :return: The base_currency of this ForexPair.  # noqa: E501
        :rtype: str
        """
        return self._base_currency
        
    @property
    def base_currency_dict(self):
        """Gets the base_currency of this ForexPair.  # noqa: E501

        The ISO 4217 currency code of the base currency as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The base_currency of this ForexPair.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.base_currency
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
            result = { 'base_currency': value }

        
        return result
        

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this ForexPair.

        The ISO 4217 currency code of the base currency  # noqa: E501

        :param base_currency: The base_currency of this ForexPair.  # noqa: E501
        :type: str
        """

        self._base_currency = base_currency

    @property
    def quote_currency(self):
        """Gets the quote_currency of this ForexPair.  # noqa: E501

        The ISO 4217 currency code of the quote currency  # noqa: E501

        :return: The quote_currency of this ForexPair.  # noqa: E501
        :rtype: str
        """
        return self._quote_currency
        
    @property
    def quote_currency_dict(self):
        """Gets the quote_currency of this ForexPair.  # noqa: E501

        The ISO 4217 currency code of the quote currency as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The quote_currency of this ForexPair.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.quote_currency
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
            result = { 'quote_currency': value }

        
        return result
        

    @quote_currency.setter
    def quote_currency(self, quote_currency):
        """Sets the quote_currency of this ForexPair.

        The ISO 4217 currency code of the quote currency  # noqa: E501

        :param quote_currency: The quote_currency of this ForexPair.  # noqa: E501
        :type: str
        """

        self._quote_currency = quote_currency

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
        if not isinstance(other, ForexPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
