# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.39.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionUnusualTrade(object):
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
        'symbol': 'str',
        'timestamp': 'date',
        'type': 'str',
        'total_value': 'float',
        'total_size': 'float',
        'average_price': 'float',
        'contract': 'str',
        'ask_at_execution': 'float',
        'bid_at_execution': 'float',
        'sentiment': 'str',
        'underlying_price_at_execution': 'float'
    }

    attribute_map = {
        'symbol': 'symbol',
        'timestamp': 'timestamp',
        'type': 'type',
        'total_value': 'total_value',
        'total_size': 'total_size',
        'average_price': 'average_price',
        'contract': 'contract',
        'ask_at_execution': 'ask_at_execution',
        'bid_at_execution': 'bid_at_execution',
        'sentiment': 'sentiment',
        'underlying_price_at_execution': 'underlying_price_at_execution'
    }

    def __init__(self, symbol=None, timestamp=None, type=None, total_value=None, total_size=None, average_price=None, contract=None, ask_at_execution=None, bid_at_execution=None, sentiment=None, underlying_price_at_execution=None):  # noqa: E501
        """OptionUnusualTrade - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._timestamp = None
        self._type = None
        self._total_value = None
        self._total_size = None
        self._average_price = None
        self._contract = None
        self._ask_at_execution = None
        self._bid_at_execution = None
        self._sentiment = None
        self._underlying_price_at_execution = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type
        if total_value is not None:
            self.total_value = total_value
        if total_size is not None:
            self.total_size = total_size
        if average_price is not None:
            self.average_price = average_price
        if contract is not None:
            self.contract = contract
        if ask_at_execution is not None:
            self.ask_at_execution = ask_at_execution
        if bid_at_execution is not None:
            self.bid_at_execution = bid_at_execution
        if sentiment is not None:
            self.sentiment = sentiment
        if underlying_price_at_execution is not None:
            self.underlying_price_at_execution = underlying_price_at_execution

    @property
    def symbol(self):
        """Gets the symbol of this OptionUnusualTrade.  # noqa: E501

        The underlying option security symbol for the trade  # noqa: E501

        :return: The symbol of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this OptionUnusualTrade.  # noqa: E501

        The underlying option security symbol for the trade as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
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
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this OptionUnusualTrade.

        The underlying option security symbol for the trade  # noqa: E501

        :param symbol: The symbol of this OptionUnusualTrade.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def timestamp(self):
        """Gets the timestamp of this OptionUnusualTrade.  # noqa: E501

        The UTC timestamp of order placement  # noqa: E501

        :return: The timestamp of this OptionUnusualTrade.  # noqa: E501
        :rtype: date
        """
        return self._timestamp
        
    @property
    def timestamp_dict(self):
        """Gets the timestamp of this OptionUnusualTrade.  # noqa: E501

        The UTC timestamp of order placement as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The timestamp of this OptionUnusualTrade.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.timestamp
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
            result = { 'timestamp': value }

        
        return result
        

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this OptionUnusualTrade.

        The UTC timestamp of order placement  # noqa: E501

        :param timestamp: The timestamp of this OptionUnusualTrade.  # noqa: E501
        :type: date
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this OptionUnusualTrade.  # noqa: E501

        The type of unusual trade  # noqa: E501

        :return: The type of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """
        return self._type
        
    @property
    def type_dict(self):
        """Gets the type of this OptionUnusualTrade.  # noqa: E501

        The type of unusual trade as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The type of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.type
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
            result = { 'type': value }

        
        return result
        

    @type.setter
    def type(self, type):
        """Sets the type of this OptionUnusualTrade.

        The type of unusual trade  # noqa: E501

        :param type: The type of this OptionUnusualTrade.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def total_value(self):
        """Gets the total_value of this OptionUnusualTrade.  # noqa: E501

        The aggregated value of all option contract premiums included in the trade  # noqa: E501

        :return: The total_value of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """
        return self._total_value
        
    @property
    def total_value_dict(self):
        """Gets the total_value of this OptionUnusualTrade.  # noqa: E501

        The aggregated value of all option contract premiums included in the trade as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_value of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.total_value
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
            result = { 'total_value': value }

        
        return result
        

    @total_value.setter
    def total_value(self, total_value):
        """Sets the total_value of this OptionUnusualTrade.

        The aggregated value of all option contract premiums included in the trade  # noqa: E501

        :param total_value: The total_value of this OptionUnusualTrade.  # noqa: E501
        :type: float
        """

        self._total_value = total_value

    @property
    def total_size(self):
        """Gets the total_size of this OptionUnusualTrade.  # noqa: E501

        The total number of contracts involved in a single transaction  # noqa: E501

        :return: The total_size of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """
        return self._total_size
        
    @property
    def total_size_dict(self):
        """Gets the total_size of this OptionUnusualTrade.  # noqa: E501

        The total number of contracts involved in a single transaction as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_size of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.total_size
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
            result = { 'total_size': value }

        
        return result
        

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this OptionUnusualTrade.

        The total number of contracts involved in a single transaction  # noqa: E501

        :param total_size: The total_size of this OptionUnusualTrade.  # noqa: E501
        :type: float
        """

        self._total_size = total_size

    @property
    def average_price(self):
        """Gets the average_price of this OptionUnusualTrade.  # noqa: E501

        The average premium paid per option contract  # noqa: E501

        :return: The average_price of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """
        return self._average_price
        
    @property
    def average_price_dict(self):
        """Gets the average_price of this OptionUnusualTrade.  # noqa: E501

        The average premium paid per option contract as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The average_price of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.average_price
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
            result = { 'average_price': value }

        
        return result
        

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this OptionUnusualTrade.

        The average premium paid per option contract  # noqa: E501

        :param average_price: The average_price of this OptionUnusualTrade.  # noqa: E501
        :type: float
        """

        self._average_price = average_price

    @property
    def contract(self):
        """Gets the contract of this OptionUnusualTrade.  # noqa: E501

        The option contract symbol  # noqa: E501

        :return: The contract of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """
        return self._contract
        
    @property
    def contract_dict(self):
        """Gets the contract of this OptionUnusualTrade.  # noqa: E501

        The option contract symbol as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The contract of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.contract
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
            result = { 'contract': value }

        
        return result
        

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this OptionUnusualTrade.

        The option contract symbol  # noqa: E501

        :param contract: The contract of this OptionUnusualTrade.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def ask_at_execution(self):
        """Gets the ask_at_execution of this OptionUnusualTrade.  # noqa: E501

        Ask price at execution  # noqa: E501

        :return: The ask_at_execution of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """
        return self._ask_at_execution
        
    @property
    def ask_at_execution_dict(self):
        """Gets the ask_at_execution of this OptionUnusualTrade.  # noqa: E501

        Ask price at execution as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_at_execution of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_at_execution
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
            result = { 'ask_at_execution': value }

        
        return result
        

    @ask_at_execution.setter
    def ask_at_execution(self, ask_at_execution):
        """Sets the ask_at_execution of this OptionUnusualTrade.

        Ask price at execution  # noqa: E501

        :param ask_at_execution: The ask_at_execution of this OptionUnusualTrade.  # noqa: E501
        :type: float
        """

        self._ask_at_execution = ask_at_execution

    @property
    def bid_at_execution(self):
        """Gets the bid_at_execution of this OptionUnusualTrade.  # noqa: E501

        Bid price at execution  # noqa: E501

        :return: The bid_at_execution of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """
        return self._bid_at_execution
        
    @property
    def bid_at_execution_dict(self):
        """Gets the bid_at_execution of this OptionUnusualTrade.  # noqa: E501

        Bid price at execution as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_at_execution of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_at_execution
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
            result = { 'bid_at_execution': value }

        
        return result
        

    @bid_at_execution.setter
    def bid_at_execution(self, bid_at_execution):
        """Sets the bid_at_execution of this OptionUnusualTrade.

        Bid price at execution  # noqa: E501

        :param bid_at_execution: The bid_at_execution of this OptionUnusualTrade.  # noqa: E501
        :type: float
        """

        self._bid_at_execution = bid_at_execution

    @property
    def sentiment(self):
        """Gets the sentiment of this OptionUnusualTrade.  # noqa: E501

        Bullish, Bearish, or Neutral Sentiment is estimated based on whether the trade was executed at the bid, ask, or mark price.  # noqa: E501

        :return: The sentiment of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """
        return self._sentiment
        
    @property
    def sentiment_dict(self):
        """Gets the sentiment of this OptionUnusualTrade.  # noqa: E501

        Bullish, Bearish, or Neutral Sentiment is estimated based on whether the trade was executed at the bid, ask, or mark price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sentiment of this OptionUnusualTrade.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.sentiment
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
            result = { 'sentiment': value }

        
        return result
        

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this OptionUnusualTrade.

        Bullish, Bearish, or Neutral Sentiment is estimated based on whether the trade was executed at the bid, ask, or mark price.  # noqa: E501

        :param sentiment: The sentiment of this OptionUnusualTrade.  # noqa: E501
        :type: str
        """
        allowed_values = ["bullish", "bearish", "neutral"]  # noqa: E501
        if sentiment not in allowed_values:
            raise ValueError(
                "Invalid value for `sentiment` ({0}), must be one of {1}"  # noqa: E501
                .format(sentiment, allowed_values)
            )

        self._sentiment = sentiment

    @property
    def underlying_price_at_execution(self):
        """Gets the underlying_price_at_execution of this OptionUnusualTrade.  # noqa: E501

        Price of the underlying security at execution of trade  # noqa: E501

        :return: The underlying_price_at_execution of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """
        return self._underlying_price_at_execution
        
    @property
    def underlying_price_at_execution_dict(self):
        """Gets the underlying_price_at_execution of this OptionUnusualTrade.  # noqa: E501

        Price of the underlying security at execution of trade as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The underlying_price_at_execution of this OptionUnusualTrade.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.underlying_price_at_execution
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
            result = { 'underlying_price_at_execution': value }

        
        return result
        

    @underlying_price_at_execution.setter
    def underlying_price_at_execution(self, underlying_price_at_execution):
        """Sets the underlying_price_at_execution of this OptionUnusualTrade.

        Price of the underlying security at execution of trade  # noqa: E501

        :param underlying_price_at_execution: The underlying_price_at_execution of this OptionUnusualTrade.  # noqa: E501
        :type: float
        """

        self._underlying_price_at_execution = underlying_price_at_execution

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
        if not isinstance(other, OptionUnusualTrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
