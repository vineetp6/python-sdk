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


class ETFSummary(object):
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
        'id': 'str',
        'name': 'str',
        'ticker': 'str',
        'figi_ticker': 'str',
        'ric': 'str',
        'isin': 'str',
        'sedol': 'str',
        'exchange_mic': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ticker': 'ticker',
        'figi_ticker': 'figi_ticker',
        'ric': 'ric',
        'isin': 'isin',
        'sedol': 'sedol',
        'exchange_mic': 'exchange_mic'
    }

    def __init__(self, id=None, name=None, ticker=None, figi_ticker=None, ric=None, isin=None, sedol=None, exchange_mic=None):  # noqa: E501
        """ETFSummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._ticker = None
        self._figi_ticker = None
        self._ric = None
        self._isin = None
        self._sedol = None
        self._exchange_mic = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ticker is not None:
            self.ticker = ticker
        if figi_ticker is not None:
            self.figi_ticker = figi_ticker
        if ric is not None:
            self.ric = ric
        if isin is not None:
            self.isin = isin
        if sedol is not None:
            self.sedol = sedol
        if exchange_mic is not None:
            self.exchange_mic = exchange_mic

    @property
    def id(self):
        """Gets the id of this ETFSummary.  # noqa: E501

        The Intrinio ID of the ETF  # noqa: E501

        :return: The id of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this ETFSummary.  # noqa: E501

        The Intrinio ID of the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
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
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this ETFSummary.

        The Intrinio ID of the ETF  # noqa: E501

        :param id: The id of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ETFSummary.  # noqa: E501

        The common name of the ETF  # noqa: E501

        :return: The name of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this ETFSummary.  # noqa: E501

        The common name of the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
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
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this ETFSummary.

        The common name of the ETF  # noqa: E501

        :param name: The name of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this ETFSummary.  # noqa: E501

        The common ticker symbol for the ETF  # noqa: E501

        :return: The ticker of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this ETFSummary.  # noqa: E501

        The common ticker symbol for the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.ticker
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
            result = { 'ticker': value }

        
        return result
        

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this ETFSummary.

        The common ticker symbol for the ETF  # noqa: E501

        :param ticker: The ticker of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def figi_ticker(self):
        """Gets the figi_ticker of this ETFSummary.  # noqa: E501

        The OpenFIGI ticker for the ETF  # noqa: E501

        :return: The figi_ticker of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._figi_ticker
        
    @property
    def figi_ticker_dict(self):
        """Gets the figi_ticker of this ETFSummary.  # noqa: E501

        The OpenFIGI ticker for the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The figi_ticker of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.figi_ticker
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
            result = { 'figi_ticker': value }

        
        return result
        

    @figi_ticker.setter
    def figi_ticker(self, figi_ticker):
        """Sets the figi_ticker of this ETFSummary.

        The OpenFIGI ticker for the ETF  # noqa: E501

        :param figi_ticker: The figi_ticker of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._figi_ticker = figi_ticker

    @property
    def ric(self):
        """Gets the ric of this ETFSummary.  # noqa: E501

        Reuters Instrument Code (RIC) for the ETF  # noqa: E501

        :return: The ric of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._ric
        
    @property
    def ric_dict(self):
        """Gets the ric of this ETFSummary.  # noqa: E501

        Reuters Instrument Code (RIC) for the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ric of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.ric
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
            result = { 'ric': value }

        
        return result
        

    @ric.setter
    def ric(self, ric):
        """Sets the ric of this ETFSummary.

        Reuters Instrument Code (RIC) for the ETF  # noqa: E501

        :param ric: The ric of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._ric = ric

    @property
    def isin(self):
        """Gets the isin of this ETFSummary.  # noqa: E501

        International Securities Identification Number (ISIN) for the ETF  # noqa: E501

        :return: The isin of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._isin
        
    @property
    def isin_dict(self):
        """Gets the isin of this ETFSummary.  # noqa: E501

        International Securities Identification Number (ISIN) for the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The isin of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.isin
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
            result = { 'isin': value }

        
        return result
        

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this ETFSummary.

        International Securities Identification Number (ISIN) for the ETF  # noqa: E501

        :param isin: The isin of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def sedol(self):
        """Gets the sedol of this ETFSummary.  # noqa: E501

        Stock Exchange Daily Official List (SEDOL) for the ETF  # noqa: E501

        :return: The sedol of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._sedol
        
    @property
    def sedol_dict(self):
        """Gets the sedol of this ETFSummary.  # noqa: E501

        Stock Exchange Daily Official List (SEDOL) for the ETF as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sedol of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.sedol
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
            result = { 'sedol': value }

        
        return result
        

    @sedol.setter
    def sedol(self, sedol):
        """Sets the sedol of this ETFSummary.

        Stock Exchange Daily Official List (SEDOL) for the ETF  # noqa: E501

        :param sedol: The sedol of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._sedol = sedol

    @property
    def exchange_mic(self):
        """Gets the exchange_mic of this ETFSummary.  # noqa: E501

        The exchange Market Identifier Code (MIC) from the International Standards Organization (ISO)  # noqa: E501

        :return: The exchange_mic of this ETFSummary.  # noqa: E501
        :rtype: str
        """
        return self._exchange_mic
        
    @property
    def exchange_mic_dict(self):
        """Gets the exchange_mic of this ETFSummary.  # noqa: E501

        The exchange Market Identifier Code (MIC) from the International Standards Organization (ISO) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The exchange_mic of this ETFSummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.exchange_mic
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
            result = { 'exchange_mic': value }

        
        return result
        

    @exchange_mic.setter
    def exchange_mic(self, exchange_mic):
        """Sets the exchange_mic of this ETFSummary.

        The exchange Market Identifier Code (MIC) from the International Standards Organization (ISO)  # noqa: E501

        :param exchange_mic: The exchange_mic of this ETFSummary.  # noqa: E501
        :type: str
        """

        self._exchange_mic = exchange_mic

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
        if not isinstance(other, ETFSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
