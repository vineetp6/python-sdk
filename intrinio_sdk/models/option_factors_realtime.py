# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.39.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionFactorsRealtime(object):
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
        'market_price': 'float',
        'underlying_price': 'float',
        'strike_price': 'float',
        'days_to_expiration': 'float',
        'risk_free_interest_rate': 'float',
        'dividend_yield': 'float'
    }

    attribute_map = {
        'market_price': 'market_price',
        'underlying_price': 'underlying_price',
        'strike_price': 'strike_price',
        'days_to_expiration': 'days_to_expiration',
        'risk_free_interest_rate': 'risk_free_interest_rate',
        'dividend_yield': 'dividend_yield'
    }

    def __init__(self, market_price=None, underlying_price=None, strike_price=None, days_to_expiration=None, risk_free_interest_rate=None, dividend_yield=None):  # noqa: E501
        """OptionFactorsRealtime - a model defined in Swagger"""  # noqa: E501

        self._market_price = None
        self._underlying_price = None
        self._strike_price = None
        self._days_to_expiration = None
        self._risk_free_interest_rate = None
        self._dividend_yield = None
        self.discriminator = None

        if market_price is not None:
            self.market_price = market_price
        if underlying_price is not None:
            self.underlying_price = underlying_price
        if strike_price is not None:
            self.strike_price = strike_price
        if days_to_expiration is not None:
            self.days_to_expiration = days_to_expiration
        if risk_free_interest_rate is not None:
            self.risk_free_interest_rate = risk_free_interest_rate
        if dividend_yield is not None:
            self.dividend_yield = dividend_yield

    @property
    def market_price(self):
        """Gets the market_price of this OptionFactorsRealtime.  # noqa: E501

        The market price of the options contract  # noqa: E501

        :return: The market_price of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._market_price
        
    @property
    def market_price_dict(self):
        """Gets the market_price of this OptionFactorsRealtime.  # noqa: E501

        The market price of the options contract as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_price of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.market_price
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
            result = { 'market_price': value }

        
        return result
        

    @market_price.setter
    def market_price(self, market_price):
        """Sets the market_price of this OptionFactorsRealtime.

        The market price of the options contract  # noqa: E501

        :param market_price: The market_price of this OptionFactorsRealtime.  # noqa: E501
        :type: float
        """

        self._market_price = market_price

    @property
    def underlying_price(self):
        """Gets the underlying_price of this OptionFactorsRealtime.  # noqa: E501

        The market price of the underlying asset  # noqa: E501

        :return: The underlying_price of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._underlying_price
        
    @property
    def underlying_price_dict(self):
        """Gets the underlying_price of this OptionFactorsRealtime.  # noqa: E501

        The market price of the underlying asset as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The underlying_price of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.underlying_price
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
            result = { 'underlying_price': value }

        
        return result
        

    @underlying_price.setter
    def underlying_price(self, underlying_price):
        """Sets the underlying_price of this OptionFactorsRealtime.

        The market price of the underlying asset  # noqa: E501

        :param underlying_price: The underlying_price of this OptionFactorsRealtime.  # noqa: E501
        :type: float
        """

        self._underlying_price = underlying_price

    @property
    def strike_price(self):
        """Gets the strike_price of this OptionFactorsRealtime.  # noqa: E501

        The strike price of the options contract  # noqa: E501

        :return: The strike_price of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._strike_price
        
    @property
    def strike_price_dict(self):
        """Gets the strike_price of this OptionFactorsRealtime.  # noqa: E501

        The strike price of the options contract as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The strike_price of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.strike_price
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
            result = { 'strike_price': value }

        
        return result
        

    @strike_price.setter
    def strike_price(self, strike_price):
        """Sets the strike_price of this OptionFactorsRealtime.

        The strike price of the options contract  # noqa: E501

        :param strike_price: The strike_price of this OptionFactorsRealtime.  # noqa: E501
        :type: float
        """

        self._strike_price = strike_price

    @property
    def days_to_expiration(self):
        """Gets the days_to_expiration of this OptionFactorsRealtime.  # noqa: E501

        The number of days to expiration  # noqa: E501

        :return: The days_to_expiration of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._days_to_expiration
        
    @property
    def days_to_expiration_dict(self):
        """Gets the days_to_expiration of this OptionFactorsRealtime.  # noqa: E501

        The number of days to expiration as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The days_to_expiration of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.days_to_expiration
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
            result = { 'days_to_expiration': value }

        
        return result
        

    @days_to_expiration.setter
    def days_to_expiration(self, days_to_expiration):
        """Sets the days_to_expiration of this OptionFactorsRealtime.

        The number of days to expiration  # noqa: E501

        :param days_to_expiration: The days_to_expiration of this OptionFactorsRealtime.  # noqa: E501
        :type: float
        """

        self._days_to_expiration = days_to_expiration

    @property
    def risk_free_interest_rate(self):
        """Gets the risk_free_interest_rate of this OptionFactorsRealtime.  # noqa: E501

        The current risk-free interest rate, as measured by the 3-month Treasury Bill rate  # noqa: E501

        :return: The risk_free_interest_rate of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._risk_free_interest_rate
        
    @property
    def risk_free_interest_rate_dict(self):
        """Gets the risk_free_interest_rate of this OptionFactorsRealtime.  # noqa: E501

        The current risk-free interest rate, as measured by the 3-month Treasury Bill rate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The risk_free_interest_rate of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.risk_free_interest_rate
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
            result = { 'risk_free_interest_rate': value }

        
        return result
        

    @risk_free_interest_rate.setter
    def risk_free_interest_rate(self, risk_free_interest_rate):
        """Sets the risk_free_interest_rate of this OptionFactorsRealtime.

        The current risk-free interest rate, as measured by the 3-month Treasury Bill rate  # noqa: E501

        :param risk_free_interest_rate: The risk_free_interest_rate of this OptionFactorsRealtime.  # noqa: E501
        :type: float
        """

        self._risk_free_interest_rate = risk_free_interest_rate

    @property
    def dividend_yield(self):
        """Gets the dividend_yield of this OptionFactorsRealtime.  # noqa: E501

        The divident yield of the underlying asset (if applicable)  # noqa: E501

        :return: The dividend_yield of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """
        return self._dividend_yield
        
    @property
    def dividend_yield_dict(self):
        """Gets the dividend_yield of this OptionFactorsRealtime.  # noqa: E501

        The divident yield of the underlying asset (if applicable) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The dividend_yield of this OptionFactorsRealtime.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.dividend_yield
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
            result = { 'dividend_yield': value }

        
        return result
        

    @dividend_yield.setter
    def dividend_yield(self, dividend_yield):
        """Sets the dividend_yield of this OptionFactorsRealtime.

        The divident yield of the underlying asset (if applicable)  # noqa: E501

        :param dividend_yield: The dividend_yield of this OptionFactorsRealtime.  # noqa: E501
        :type: float
        """

        self._dividend_yield = dividend_yield

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
        if not isinstance(other, OptionFactorsRealtime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
