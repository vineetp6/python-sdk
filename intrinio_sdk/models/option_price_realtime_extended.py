# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.53.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OptionPriceRealtimeExtended(object):
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
        'bid_open': 'float',
        'bid_high': 'float',
        'bid_low': 'float',
        'ask_open': 'float',
        'ask_high': 'float',
        'ask_low': 'float',
        'trade_open': 'float',
        'trade_high': 'float',
        'trade_low': 'float',
        'ask_close': 'float',
        'bid_close': 'float',
        'trade_close': 'float',
        'mark': 'float'
    }

    attribute_map = {
        'bid_open': 'bid_open',
        'bid_high': 'bid_high',
        'bid_low': 'bid_low',
        'ask_open': 'ask_open',
        'ask_high': 'ask_high',
        'ask_low': 'ask_low',
        'trade_open': 'trade_open',
        'trade_high': 'trade_high',
        'trade_low': 'trade_low',
        'ask_close': 'ask_close',
        'bid_close': 'bid_close',
        'trade_close': 'trade_close',
        'mark': 'mark'
    }

    def __init__(self, bid_open=None, bid_high=None, bid_low=None, ask_open=None, ask_high=None, ask_low=None, trade_open=None, trade_high=None, trade_low=None, ask_close=None, bid_close=None, trade_close=None, mark=None):  # noqa: E501
        """OptionPriceRealtimeExtended - a model defined in Swagger"""  # noqa: E501

        self._bid_open = None
        self._bid_high = None
        self._bid_low = None
        self._ask_open = None
        self._ask_high = None
        self._ask_low = None
        self._trade_open = None
        self._trade_high = None
        self._trade_low = None
        self._ask_close = None
        self._bid_close = None
        self._trade_close = None
        self._mark = None
        self.discriminator = None

        if bid_open is not None:
            self.bid_open = bid_open
        if bid_high is not None:
            self.bid_high = bid_high
        if bid_low is not None:
            self.bid_low = bid_low
        if ask_open is not None:
            self.ask_open = ask_open
        if ask_high is not None:
            self.ask_high = ask_high
        if ask_low is not None:
            self.ask_low = ask_low
        if trade_open is not None:
            self.trade_open = trade_open
        if trade_high is not None:
            self.trade_high = trade_high
        if trade_low is not None:
            self.trade_low = trade_low
        if ask_close is not None:
            self.ask_close = ask_close
        if bid_close is not None:
            self.bid_close = bid_close
        if trade_close is not None:
            self.trade_close = trade_close
        if mark is not None:
            self.mark = mark

    @property
    def bid_open(self):
        """Gets the bid_open of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the bid at open  # noqa: E501

        :return: The bid_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._bid_open
        
    @property
    def bid_open_dict(self):
        """Gets the bid_open of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the bid at open as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_open
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
            result = { 'bid_open': value }

        
        return result
        

    @bid_open.setter
    def bid_open(self, bid_open):
        """Sets the bid_open of this OptionPriceRealtimeExtended.

        The price of the bid at open  # noqa: E501

        :param bid_open: The bid_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._bid_open = bid_open

    @property
    def bid_high(self):
        """Gets the bid_high of this OptionPriceRealtimeExtended.  # noqa: E501

        The high bid so far today  # noqa: E501

        :return: The bid_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._bid_high
        
    @property
    def bid_high_dict(self):
        """Gets the bid_high of this OptionPriceRealtimeExtended.  # noqa: E501

        The high bid so far today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_high of this OptionPriceRealtimeExtended.  # noqa: E501
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
        """Sets the bid_high of this OptionPriceRealtimeExtended.

        The high bid so far today  # noqa: E501

        :param bid_high: The bid_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._bid_high = bid_high

    @property
    def bid_low(self):
        """Gets the bid_low of this OptionPriceRealtimeExtended.  # noqa: E501

        The low bid so far today  # noqa: E501

        :return: The bid_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._bid_low
        
    @property
    def bid_low_dict(self):
        """Gets the bid_low of this OptionPriceRealtimeExtended.  # noqa: E501

        The low bid so far today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
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
        """Sets the bid_low of this OptionPriceRealtimeExtended.

        The low bid so far today  # noqa: E501

        :param bid_low: The bid_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._bid_low = bid_low

    @property
    def ask_open(self):
        """Gets the ask_open of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the ask at open  # noqa: E501

        :return: The ask_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._ask_open
        
    @property
    def ask_open_dict(self):
        """Gets the ask_open of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the ask at open as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_open
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
            result = { 'ask_open': value }

        
        return result
        

    @ask_open.setter
    def ask_open(self, ask_open):
        """Sets the ask_open of this OptionPriceRealtimeExtended.

        The price of the ask at open  # noqa: E501

        :param ask_open: The ask_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._ask_open = ask_open

    @property
    def ask_high(self):
        """Gets the ask_high of this OptionPriceRealtimeExtended.  # noqa: E501

        The high ask so far today  # noqa: E501

        :return: The ask_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._ask_high
        
    @property
    def ask_high_dict(self):
        """Gets the ask_high of this OptionPriceRealtimeExtended.  # noqa: E501

        The high ask so far today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_high of this OptionPriceRealtimeExtended.  # noqa: E501
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
        """Sets the ask_high of this OptionPriceRealtimeExtended.

        The high ask so far today  # noqa: E501

        :param ask_high: The ask_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._ask_high = ask_high

    @property
    def ask_low(self):
        """Gets the ask_low of this OptionPriceRealtimeExtended.  # noqa: E501

        The low ask so far today  # noqa: E501

        :return: The ask_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._ask_low
        
    @property
    def ask_low_dict(self):
        """Gets the ask_low of this OptionPriceRealtimeExtended.  # noqa: E501

        The low ask so far today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_low of this OptionPriceRealtimeExtended.  # noqa: E501
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
        """Sets the ask_low of this OptionPriceRealtimeExtended.

        The low ask so far today  # noqa: E501

        :param ask_low: The ask_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._ask_low = ask_low

    @property
    def trade_open(self):
        """Gets the trade_open of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the trade at open  # noqa: E501

        :return: The trade_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._trade_open
        
    @property
    def trade_open_dict(self):
        """Gets the trade_open of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the trade at open as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trade_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.trade_open
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
            result = { 'trade_open': value }

        
        return result
        

    @trade_open.setter
    def trade_open(self, trade_open):
        """Sets the trade_open of this OptionPriceRealtimeExtended.

        The price of the trade at open  # noqa: E501

        :param trade_open: The trade_open of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._trade_open = trade_open

    @property
    def trade_high(self):
        """Gets the trade_high of this OptionPriceRealtimeExtended.  # noqa: E501

        The high trade so far today  # noqa: E501

        :return: The trade_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._trade_high
        
    @property
    def trade_high_dict(self):
        """Gets the trade_high of this OptionPriceRealtimeExtended.  # noqa: E501

        The high trade so far today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trade_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.trade_high
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
            result = { 'trade_high': value }

        
        return result
        

    @trade_high.setter
    def trade_high(self, trade_high):
        """Sets the trade_high of this OptionPriceRealtimeExtended.

        The high trade so far today  # noqa: E501

        :param trade_high: The trade_high of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._trade_high = trade_high

    @property
    def trade_low(self):
        """Gets the trade_low of this OptionPriceRealtimeExtended.  # noqa: E501

        The low trade so far today  # noqa: E501

        :return: The trade_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._trade_low
        
    @property
    def trade_low_dict(self):
        """Gets the trade_low of this OptionPriceRealtimeExtended.  # noqa: E501

        The low trade so far today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trade_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.trade_low
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
            result = { 'trade_low': value }

        
        return result
        

    @trade_low.setter
    def trade_low(self, trade_low):
        """Sets the trade_low of this OptionPriceRealtimeExtended.

        The low trade so far today  # noqa: E501

        :param trade_low: The trade_low of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._trade_low = trade_low

    @property
    def ask_close(self):
        """Gets the ask_close of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of ask at close today  # noqa: E501

        :return: The ask_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._ask_close
        
    @property
    def ask_close_dict(self):
        """Gets the ask_close of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of ask at close today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ask_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ask_close
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
            result = { 'ask_close': value }

        
        return result
        

    @ask_close.setter
    def ask_close(self, ask_close):
        """Sets the ask_close of this OptionPriceRealtimeExtended.

        The price of ask at close today  # noqa: E501

        :param ask_close: The ask_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._ask_close = ask_close

    @property
    def bid_close(self):
        """Gets the bid_close of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of bid at close today  # noqa: E501

        :return: The bid_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._bid_close
        
    @property
    def bid_close_dict(self):
        """Gets the bid_close of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of bid at close today as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bid_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.bid_close
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
            result = { 'bid_close': value }

        
        return result
        

    @bid_close.setter
    def bid_close(self, bid_close):
        """Sets the bid_close of this OptionPriceRealtimeExtended.

        The price of bid at close today  # noqa: E501

        :param bid_close: The bid_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._bid_close = bid_close

    @property
    def trade_close(self):
        """Gets the trade_close of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the last trade of the day  # noqa: E501

        :return: The trade_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._trade_close
        
    @property
    def trade_close_dict(self):
        """Gets the trade_close of this OptionPriceRealtimeExtended.  # noqa: E501

        The price of the last trade of the day as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trade_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.trade_close
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
            result = { 'trade_close': value }

        
        return result
        

    @trade_close.setter
    def trade_close(self, trade_close):
        """Sets the trade_close of this OptionPriceRealtimeExtended.

        The price of the last trade of the day  # noqa: E501

        :param trade_close: The trade_close of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._trade_close = trade_close

    @property
    def mark(self):
        """Gets the mark of this OptionPriceRealtimeExtended.  # noqa: E501

        The mark price  # noqa: E501

        :return: The mark of this OptionPriceRealtimeExtended.  # noqa: E501
        :rtype: float
        """
        return self._mark
        
    @property
    def mark_dict(self):
        """Gets the mark of this OptionPriceRealtimeExtended.  # noqa: E501

        The mark price as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mark of this OptionPriceRealtimeExtended.  # noqa: E501
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
        """Sets the mark of this OptionPriceRealtimeExtended.

        The mark price  # noqa: E501

        :param mark: The mark of this OptionPriceRealtimeExtended.  # noqa: E501
        :type: float
        """

        self._mark = mark

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
        if not isinstance(other, OptionPriceRealtimeExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
