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


class OptionPriceEod(object):
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
        'date': 'str',
        'close': 'float',
        'close_bid': 'float',
        'close_ask': 'float',
        'volume': 'int',
        'open': 'float',
        'open_ask': 'float',
        'open_bid': 'float',
        'open_interest': 'int',
        'high': 'float',
        'low': 'float',
        'mark': 'float',
        'ask_high': 'float',
        'ask_low': 'float',
        'bid_high': 'float',
        'bid_low': 'object'
    }

    attribute_map = {
        'date': 'date',
        'close': 'close',
        'close_bid': 'close_bid',
        'close_ask': 'close_ask',
        'volume': 'volume',
        'open': 'open',
        'open_ask': 'open_ask',
        'open_bid': 'open_bid',
        'open_interest': 'open_interest',
        'high': 'high',
        'low': 'low',
        'mark': 'mark',
        'ask_high': 'ask_high',
        'ask_low': 'ask_low',
        'bid_high': 'bid_high',
        'bid_low': 'bid_low'
    }

    def __init__(self, date=None, close=None, close_bid=None, close_ask=None, volume=None, open=None, open_ask=None, open_bid=None, open_interest=None, high=None, low=None, mark=None, ask_high=None, ask_low=None, bid_high=None, bid_low=None):  # noqa: E501
        """OptionPriceEod - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._close = None
        self._close_bid = None
        self._close_ask = None
        self._volume = None
        self._open = None
        self._open_ask = None
        self._open_bid = None
        self._open_interest = None
        self._high = None
        self._low = None
        self._mark = None
        self._ask_high = None
        self._ask_low = None
        self._bid_high = None
        self._bid_low = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if close is not None:
            self.close = close
        if close_bid is not None:
            self.close_bid = close_bid
        if close_ask is not None:
            self.close_ask = close_ask
        if volume is not None:
            self.volume = volume
        if open is not None:
            self.open = open
        if open_ask is not None:
            self.open_ask = open_ask
        if open_bid is not None:
            self.open_bid = open_bid
        if open_interest is not None:
            self.open_interest = open_interest
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if mark is not None:
            self.mark = mark
        if ask_high is not None:
            self.ask_high = ask_high
        if ask_low is not None:
            self.ask_low = ask_low
        if bid_high is not None:
            self.bid_high = bid_high
        if bid_low is not None:
            self.bid_low = bid_low

    @property
    def date(self):
        """Gets the date of this OptionPriceEod.  # noqa: E501

        The date of the price, in the format YYYY-MM-DD  # noqa: E501

        :return: The date of this OptionPriceEod.  # noqa: E501
        :rtype: str
        """
        return self._date
        
    @property
    def date_dict(self):
        """Gets the date of this OptionPriceEod.  # noqa: E501

        The date of the price, in the format YYYY-MM-DD as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date of this OptionPriceEod.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.date
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
            result = { 'date': value }

        
        return result
        

    @date.setter
    def date(self, date):
        """Sets the date of this OptionPriceEod.

        The date of the price, in the format YYYY-MM-DD  # noqa: E501

        :param date: The date of this OptionPriceEod.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def close(self):
        """Gets the close of this OptionPriceEod.  # noqa: E501

        The closing price of the options contract.  # noqa: E501

        :return: The close of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._close
        
    @property
    def close_dict(self):
        """Gets the close of this OptionPriceEod.  # noqa: E501

        The closing price of the options contract. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close
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
            result = { 'close': value }

        
        return result
        

    @close.setter
    def close(self, close):
        """Sets the close of this OptionPriceEod.

        The closing price of the options contract.  # noqa: E501

        :param close: The close of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def close_bid(self):
        """Gets the close_bid of this OptionPriceEod.  # noqa: E501

        The closing bid price of the options contract.  # noqa: E501

        :return: The close_bid of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._close_bid
        
    @property
    def close_bid_dict(self):
        """Gets the close_bid of this OptionPriceEod.  # noqa: E501

        The closing bid price of the options contract. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_bid of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close_bid
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
            result = { 'close_bid': value }

        
        return result
        

    @close_bid.setter
    def close_bid(self, close_bid):
        """Sets the close_bid of this OptionPriceEod.

        The closing bid price of the options contract.  # noqa: E501

        :param close_bid: The close_bid of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._close_bid = close_bid

    @property
    def close_ask(self):
        """Gets the close_ask of this OptionPriceEod.  # noqa: E501

        The closing ask price of the options contract.  # noqa: E501

        :return: The close_ask of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._close_ask
        
    @property
    def close_ask_dict(self):
        """Gets the close_ask of this OptionPriceEod.  # noqa: E501

        The closing ask price of the options contract. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The close_ask of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.close_ask
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
            result = { 'close_ask': value }

        
        return result
        

    @close_ask.setter
    def close_ask(self, close_ask):
        """Sets the close_ask of this OptionPriceEod.

        The closing ask price of the options contract.  # noqa: E501

        :param close_ask: The close_ask of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._close_ask = close_ask

    @property
    def volume(self):
        """Gets the volume of this OptionPriceEod.  # noqa: E501

        The cumulative volume of this options contract that traded that day.  # noqa: E501

        :return: The volume of this OptionPriceEod.  # noqa: E501
        :rtype: int
        """
        return self._volume
        
    @property
    def volume_dict(self):
        """Gets the volume of this OptionPriceEod.  # noqa: E501

        The cumulative volume of this options contract that traded that day. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The volume of this OptionPriceEod.  # noqa: E501
        :rtype: int
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
        """Sets the volume of this OptionPriceEod.

        The cumulative volume of this options contract that traded that day.  # noqa: E501

        :param volume: The volume of this OptionPriceEod.  # noqa: E501
        :type: int
        """

        self._volume = volume

    @property
    def open(self):
        """Gets the open of this OptionPriceEod.  # noqa: E501

        The price at the beginning of the period  # noqa: E501

        :return: The open of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._open
        
    @property
    def open_dict(self):
        """Gets the open of this OptionPriceEod.  # noqa: E501

        The price at the beginning of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open
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
            result = { 'open': value }

        
        return result
        

    @open.setter
    def open(self, open):
        """Sets the open of this OptionPriceEod.

        The price at the beginning of the period  # noqa: E501

        :param open: The open of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def open_ask(self):
        """Gets the open_ask of this OptionPriceEod.  # noqa: E501

        The ask at the beginning of the period  # noqa: E501

        :return: The open_ask of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._open_ask
        
    @property
    def open_ask_dict(self):
        """Gets the open_ask of this OptionPriceEod.  # noqa: E501

        The ask at the beginning of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_ask of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open_ask
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
            result = { 'open_ask': value }

        
        return result
        

    @open_ask.setter
    def open_ask(self, open_ask):
        """Sets the open_ask of this OptionPriceEod.

        The ask at the beginning of the period  # noqa: E501

        :param open_ask: The open_ask of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._open_ask = open_ask

    @property
    def open_bid(self):
        """Gets the open_bid of this OptionPriceEod.  # noqa: E501

        The bid at the beginning of the period  # noqa: E501

        :return: The open_bid of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._open_bid
        
    @property
    def open_bid_dict(self):
        """Gets the open_bid of this OptionPriceEod.  # noqa: E501

        The bid at the beginning of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_bid of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.open_bid
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
            result = { 'open_bid': value }

        
        return result
        

    @open_bid.setter
    def open_bid(self, open_bid):
        """Sets the open_bid of this OptionPriceEod.

        The bid at the beginning of the period  # noqa: E501

        :param open_bid: The open_bid of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._open_bid = open_bid

    @property
    def open_interest(self):
        """Gets the open_interest of this OptionPriceEod.  # noqa: E501

        The total number of this options contract that are still open.  # noqa: E501

        :return: The open_interest of this OptionPriceEod.  # noqa: E501
        :rtype: int
        """
        return self._open_interest
        
    @property
    def open_interest_dict(self):
        """Gets the open_interest of this OptionPriceEod.  # noqa: E501

        The total number of this options contract that are still open. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The open_interest of this OptionPriceEod.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.open_interest
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
            result = { 'open_interest': value }

        
        return result
        

    @open_interest.setter
    def open_interest(self, open_interest):
        """Sets the open_interest of this OptionPriceEod.

        The total number of this options contract that are still open.  # noqa: E501

        :param open_interest: The open_interest of this OptionPriceEod.  # noqa: E501
        :type: int
        """

        self._open_interest = open_interest

    @property
    def high(self):
        """Gets the high of this OptionPriceEod.  # noqa: E501

        The highest price over the span of the period  # noqa: E501

        :return: The high of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this OptionPriceEod.  # noqa: E501

        The highest price over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high
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
            result = { 'high': value }

        
        return result
        

    @high.setter
    def high(self, high):
        """Sets the high of this OptionPriceEod.

        The highest price over the span of the period  # noqa: E501

        :param high: The high of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this OptionPriceEod.  # noqa: E501

        The highest price over the span of the period  # noqa: E501

        :return: The low of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this OptionPriceEod.  # noqa: E501

        The highest price over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low
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
            result = { 'low': value }

        
        return result
        

    @low.setter
    def low(self, low):
        """Sets the low of this OptionPriceEod.

        The highest price over the span of the period  # noqa: E501

        :param low: The low of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def mark(self):
        """Gets the mark of this OptionPriceEod.  # noqa: E501

        The mid price between the latest bid and ask spread  # noqa: E501

        :return: The mark of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._mark
        
    @property
    def mark_dict(self):
        """Gets the mark of this OptionPriceEod.  # noqa: E501

        The mid price between the latest bid and ask spread as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mark of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mark
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
            result = { 'mark': value }

        
        return result
        

    @mark.setter
    def mark(self, mark):
        """Sets the mark of this OptionPriceEod.

        The mid price between the latest bid and ask spread  # noqa: E501

        :param mark: The mark of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._mark = mark

    @property
    def ask_high(self):
        """Gets the ask_high of this OptionPriceEod.  # noqa: E501

        The highest ask over the span of the period  # noqa: E501

        :return: The ask_high of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._ask_high
        
    @property
    def ask_high_dict(self):
        """Gets the ask_high of this OptionPriceEod.  # noqa: E501

        The highest ask over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_high of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_high
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
            result = { 'ask_high': value }

        
        return result
        

    @ask_high.setter
    def ask_high(self, ask_high):
        """Sets the ask_high of this OptionPriceEod.

        The highest ask over the span of the period  # noqa: E501

        :param ask_high: The ask_high of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._ask_high = ask_high

    @property
    def ask_low(self):
        """Gets the ask_low of this OptionPriceEod.  # noqa: E501

        The lowest ask over the span of the period  # noqa: E501

        :return: The ask_low of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._ask_low
        
    @property
    def ask_low_dict(self):
        """Gets the ask_low of this OptionPriceEod.  # noqa: E501

        The lowest ask over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_low of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_low
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
            result = { 'ask_low': value }

        
        return result
        

    @ask_low.setter
    def ask_low(self, ask_low):
        """Sets the ask_low of this OptionPriceEod.

        The lowest ask over the span of the period  # noqa: E501

        :param ask_low: The ask_low of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._ask_low = ask_low

    @property
    def bid_high(self):
        """Gets the bid_high of this OptionPriceEod.  # noqa: E501

        The highest bid over the span of the period  # noqa: E501

        :return: The bid_high of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """
        return self._bid_high
        
    @property
    def bid_high_dict(self):
        """Gets the bid_high of this OptionPriceEod.  # noqa: E501

        The highest bid over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_high of this OptionPriceEod.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_high
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
            result = { 'bid_high': value }

        
        return result
        

    @bid_high.setter
    def bid_high(self, bid_high):
        """Sets the bid_high of this OptionPriceEod.

        The highest bid over the span of the period  # noqa: E501

        :param bid_high: The bid_high of this OptionPriceEod.  # noqa: E501
        :type: float
        """

        self._bid_high = bid_high

    @property
    def bid_low(self):
        """Gets the bid_low of this OptionPriceEod.  # noqa: E501

        The lowest bid over the span of the period  # noqa: E501

        :return: The bid_low of this OptionPriceEod.  # noqa: E501
        :rtype: object
        """
        return self._bid_low
        
    @property
    def bid_low_dict(self):
        """Gets the bid_low of this OptionPriceEod.  # noqa: E501

        The lowest bid over the span of the period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_low of this OptionPriceEod.  # noqa: E501
        :rtype: object
        """

        result = None

        value = self.bid_low
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
            result = { 'bid_low': value }

        
        return result
        

    @bid_low.setter
    def bid_low(self, bid_low):
        """Sets the bid_low of this OptionPriceEod.

        The lowest bid over the span of the period  # noqa: E501

        :param bid_low: The bid_low of this OptionPriceEod.  # noqa: E501
        :type: object
        """

        self._bid_low = bid_low

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
        if not isinstance(other, OptionPriceEod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
