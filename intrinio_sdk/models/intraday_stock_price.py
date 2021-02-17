# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.19.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IntradayStockPrice(object):
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
        'time': 'datetime',
        'last_price': 'float',
        'ask_price': 'float',
        'ask_size': 'float',
        'bid_price': 'float',
        'bid_size': 'float',
        'volume': 'float',
        'source': 'str'
    }

    attribute_map = {
        'time': 'time',
        'last_price': 'last_price',
        'ask_price': 'ask_price',
        'ask_size': 'ask_size',
        'bid_price': 'bid_price',
        'bid_size': 'bid_size',
        'volume': 'volume',
        'source': 'source'
    }

    def __init__(self, time=None, last_price=None, ask_price=None, ask_size=None, bid_price=None, bid_size=None, volume=None, source=None):  # noqa: E501
        """IntradayStockPrice - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._last_price = None
        self._ask_price = None
        self._ask_size = None
        self._bid_price = None
        self._bid_size = None
        self._volume = None
        self._source = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if last_price is not None:
            self.last_price = last_price
        if ask_price is not None:
            self.ask_price = ask_price
        if ask_size is not None:
            self.ask_size = ask_size
        if bid_price is not None:
            self.bid_price = bid_price
        if bid_size is not None:
            self.bid_size = bid_size
        if volume is not None:
            self.volume = volume
        if source is not None:
            self.source = source

    @property
    def time(self):
        """Gets the time of this IntradayStockPrice.  # noqa: E501

        The timestamp that the `last_price` represents.  # noqa: E501

        :return: The time of this IntradayStockPrice.  # noqa: E501
        :rtype: datetime
        """
        return self._time
        
    @property
    def time_dict(self):
        """Gets the time of this IntradayStockPrice.  # noqa: E501

        The timestamp that the `last_price` represents. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The time of this IntradayStockPrice.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.time
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
            result = { 'time': value }

        
        return result
        

    @time.setter
    def time(self, time):
        """Sets the time of this IntradayStockPrice.

        The timestamp that the `last_price` represents.  # noqa: E501

        :param time: The time of this IntradayStockPrice.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def last_price(self):
        """Gets the last_price of this IntradayStockPrice.  # noqa: E501

        The price of the last trade.  # noqa: E501

        :return: The last_price of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._last_price
        
    @property
    def last_price_dict(self):
        """Gets the last_price of this IntradayStockPrice.  # noqa: E501

        The price of the last trade. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_price of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.last_price
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
            result = { 'last_price': value }

        
        return result
        

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this IntradayStockPrice.

        The price of the last trade.  # noqa: E501

        :param last_price: The last_price of this IntradayStockPrice.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def ask_price(self):
        """Gets the ask_price of this IntradayStockPrice.  # noqa: E501

        The price of the top ask order.  # noqa: E501

        :return: The ask_price of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._ask_price
        
    @property
    def ask_price_dict(self):
        """Gets the ask_price of this IntradayStockPrice.  # noqa: E501

        The price of the top ask order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_price of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_price
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
            result = { 'ask_price': value }

        
        return result
        

    @ask_price.setter
    def ask_price(self, ask_price):
        """Sets the ask_price of this IntradayStockPrice.

        The price of the top ask order.  # noqa: E501

        :param ask_price: The ask_price of this IntradayStockPrice.  # noqa: E501
        :type: float
        """

        self._ask_price = ask_price

    @property
    def ask_size(self):
        """Gets the ask_size of this IntradayStockPrice.  # noqa: E501

        The size of the top ask order.  # noqa: E501

        :return: The ask_size of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._ask_size
        
    @property
    def ask_size_dict(self):
        """Gets the ask_size of this IntradayStockPrice.  # noqa: E501

        The size of the top ask order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_size of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_size
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
            result = { 'ask_size': value }

        
        return result
        

    @ask_size.setter
    def ask_size(self, ask_size):
        """Sets the ask_size of this IntradayStockPrice.

        The size of the top ask order.  # noqa: E501

        :param ask_size: The ask_size of this IntradayStockPrice.  # noqa: E501
        :type: float
        """

        self._ask_size = ask_size

    @property
    def bid_price(self):
        """Gets the bid_price of this IntradayStockPrice.  # noqa: E501

        The price of the top bid order.  # noqa: E501

        :return: The bid_price of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._bid_price
        
    @property
    def bid_price_dict(self):
        """Gets the bid_price of this IntradayStockPrice.  # noqa: E501

        The price of the top bid order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_price of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_price
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
            result = { 'bid_price': value }

        
        return result
        

    @bid_price.setter
    def bid_price(self, bid_price):
        """Sets the bid_price of this IntradayStockPrice.

        The price of the top bid order.  # noqa: E501

        :param bid_price: The bid_price of this IntradayStockPrice.  # noqa: E501
        :type: float
        """

        self._bid_price = bid_price

    @property
    def bid_size(self):
        """Gets the bid_size of this IntradayStockPrice.  # noqa: E501

        The size of the top bid order.  # noqa: E501

        :return: The bid_size of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._bid_size
        
    @property
    def bid_size_dict(self):
        """Gets the bid_size of this IntradayStockPrice.  # noqa: E501

        The size of the top bid order. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_size of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_size
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
            result = { 'bid_size': value }

        
        return result
        

    @bid_size.setter
    def bid_size(self, bid_size):
        """Sets the bid_size of this IntradayStockPrice.

        The size of the top bid order.  # noqa: E501

        :param bid_size: The bid_size of this IntradayStockPrice.  # noqa: E501
        :type: float
        """

        self._bid_size = bid_size

    @property
    def volume(self):
        """Gets the volume of this IntradayStockPrice.  # noqa: E501

        The number of shares exchanged during the trading day on the exchange.  # noqa: E501

        :return: The volume of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """
        return self._volume
        
    @property
    def volume_dict(self):
        """Gets the volume of this IntradayStockPrice.  # noqa: E501

        The number of shares exchanged during the trading day on the exchange. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume of this IntradayStockPrice.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.volume
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
            result = { 'volume': value }

        
        return result
        

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this IntradayStockPrice.

        The number of shares exchanged during the trading day on the exchange.  # noqa: E501

        :param volume: The volume of this IntradayStockPrice.  # noqa: E501
        :type: float
        """

        self._volume = volume

    @property
    def source(self):
        """Gets the source of this IntradayStockPrice.  # noqa: E501

        The source of the data.  # noqa: E501

        :return: The source of this IntradayStockPrice.  # noqa: E501
        :rtype: str
        """
        return self._source
        
    @property
    def source_dict(self):
        """Gets the source of this IntradayStockPrice.  # noqa: E501

        The source of the data. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source of this IntradayStockPrice.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.source
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
            result = { 'source': value }

        
        return result
        

    @source.setter
    def source(self, source):
        """Sets the source of this IntradayStockPrice.

        The source of the data.  # noqa: E501

        :param source: The source of this IntradayStockPrice.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if not isinstance(other, IntradayStockPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
