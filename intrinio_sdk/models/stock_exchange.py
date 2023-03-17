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


class StockExchange(object):
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
        'mic': 'str',
        'acronym': 'str',
        'city': 'str',
        'country': 'str',
        'country_code': 'str',
        'website': 'str',
        'first_stock_price_date': 'date',
        'last_stock_price_date': 'date'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mic': 'mic',
        'acronym': 'acronym',
        'city': 'city',
        'country': 'country',
        'country_code': 'country_code',
        'website': 'website',
        'first_stock_price_date': 'first_stock_price_date',
        'last_stock_price_date': 'last_stock_price_date'
    }

    def __init__(self, id=None, name=None, mic=None, acronym=None, city=None, country=None, country_code=None, website=None, first_stock_price_date=None, last_stock_price_date=None):  # noqa: E501
        """StockExchange - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._mic = None
        self._acronym = None
        self._city = None
        self._country = None
        self._country_code = None
        self._website = None
        self._first_stock_price_date = None
        self._last_stock_price_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mic is not None:
            self.mic = mic
        if acronym is not None:
            self.acronym = acronym
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if website is not None:
            self.website = website
        if first_stock_price_date is not None:
            self.first_stock_price_date = first_stock_price_date
        if last_stock_price_date is not None:
            self.last_stock_price_date = last_stock_price_date

    @property
    def id(self):
        """Gets the id of this StockExchange.  # noqa: E501

        The Intrinio ID for the Stock Exchange  # noqa: E501

        :return: The id of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this StockExchange.  # noqa: E501

        The Intrinio ID for the Stock Exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this StockExchange.  # noqa: E501
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
        """Sets the id of this StockExchange.

        The Intrinio ID for the Stock Exchange  # noqa: E501

        :param id: The id of this StockExchange.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StockExchange.  # noqa: E501

        The name of the exchange  # noqa: E501

        :return: The name of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this StockExchange.  # noqa: E501

        The name of the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this StockExchange.  # noqa: E501
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
        """Sets the name of this StockExchange.

        The name of the exchange  # noqa: E501

        :param name: The name of this StockExchange.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mic(self):
        """Gets the mic of this StockExchange.  # noqa: E501

        The Market Identifier Code (MIC) of the exchange  # noqa: E501

        :return: The mic of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._mic
        
    @property
    def mic_dict(self):
        """Gets the mic of this StockExchange.  # noqa: E501

        The Market Identifier Code (MIC) of the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mic of this StockExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.mic
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
            result = { 'mic': value }

        
        return result
        

    @mic.setter
    def mic(self, mic):
        """Sets the mic of this StockExchange.

        The Market Identifier Code (MIC) of the exchange  # noqa: E501

        :param mic: The mic of this StockExchange.  # noqa: E501
        :type: str
        """

        self._mic = mic

    @property
    def acronym(self):
        """Gets the acronym of this StockExchange.  # noqa: E501

        The acronym of the exchange's name  # noqa: E501

        :return: The acronym of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._acronym
        
    @property
    def acronym_dict(self):
        """Gets the acronym of this StockExchange.  # noqa: E501

        The acronym of the exchange's name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The acronym of this StockExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.acronym
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
            result = { 'acronym': value }

        
        return result
        

    @acronym.setter
    def acronym(self, acronym):
        """Sets the acronym of this StockExchange.

        The acronym of the exchange's name  # noqa: E501

        :param acronym: The acronym of this StockExchange.  # noqa: E501
        :type: str
        """

        self._acronym = acronym

    @property
    def city(self):
        """Gets the city of this StockExchange.  # noqa: E501

        The city in which the exchange is located  # noqa: E501

        :return: The city of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._city
        
    @property
    def city_dict(self):
        """Gets the city of this StockExchange.  # noqa: E501

        The city in which the exchange is located as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The city of this StockExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.city
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
            result = { 'city': value }

        
        return result
        

    @city.setter
    def city(self, city):
        """Sets the city of this StockExchange.

        The city in which the exchange is located  # noqa: E501

        :param city: The city of this StockExchange.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this StockExchange.  # noqa: E501

        The country in which the exchange is located  # noqa: E501

        :return: The country of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._country
        
    @property
    def country_dict(self):
        """Gets the country of this StockExchange.  # noqa: E501

        The country in which the exchange is located as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The country of this StockExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.country
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
            result = { 'country': value }

        
        return result
        

    @country.setter
    def country(self, country):
        """Sets the country of this StockExchange.

        The country in which the exchange is located  # noqa: E501

        :param country: The country of this StockExchange.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this StockExchange.  # noqa: E501

        The 2-digit code of the exchange's country  # noqa: E501

        :return: The country_code of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._country_code
        
    @property
    def country_code_dict(self):
        """Gets the country_code of this StockExchange.  # noqa: E501

        The 2-digit code of the exchange's country as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The country_code of this StockExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.country_code
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
            result = { 'country_code': value }

        
        return result
        

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this StockExchange.

        The 2-digit code of the exchange's country  # noqa: E501

        :param country_code: The country_code of this StockExchange.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def website(self):
        """Gets the website of this StockExchange.  # noqa: E501

        The website of the exchange  # noqa: E501

        :return: The website of this StockExchange.  # noqa: E501
        :rtype: str
        """
        return self._website
        
    @property
    def website_dict(self):
        """Gets the website of this StockExchange.  # noqa: E501

        The website of the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The website of this StockExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.website
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
            result = { 'website': value }

        
        return result
        

    @website.setter
    def website(self, website):
        """Sets the website of this StockExchange.

        The website of the exchange  # noqa: E501

        :param website: The website of this StockExchange.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def first_stock_price_date(self):
        """Gets the first_stock_price_date of this StockExchange.  # noqa: E501

        The earliest date for which Intrinio has stock prices for the exchange  # noqa: E501

        :return: The first_stock_price_date of this StockExchange.  # noqa: E501
        :rtype: date
        """
        return self._first_stock_price_date
        
    @property
    def first_stock_price_date_dict(self):
        """Gets the first_stock_price_date of this StockExchange.  # noqa: E501

        The earliest date for which Intrinio has stock prices for the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The first_stock_price_date of this StockExchange.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.first_stock_price_date
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
            result = { 'first_stock_price_date': value }

        
        return result
        

    @first_stock_price_date.setter
    def first_stock_price_date(self, first_stock_price_date):
        """Sets the first_stock_price_date of this StockExchange.

        The earliest date for which Intrinio has stock prices for the exchange  # noqa: E501

        :param first_stock_price_date: The first_stock_price_date of this StockExchange.  # noqa: E501
        :type: date
        """

        self._first_stock_price_date = first_stock_price_date

    @property
    def last_stock_price_date(self):
        """Gets the last_stock_price_date of this StockExchange.  # noqa: E501

        The latest date for which Intrinio has stock prices for the exchange  # noqa: E501

        :return: The last_stock_price_date of this StockExchange.  # noqa: E501
        :rtype: date
        """
        return self._last_stock_price_date
        
    @property
    def last_stock_price_date_dict(self):
        """Gets the last_stock_price_date of this StockExchange.  # noqa: E501

        The latest date for which Intrinio has stock prices for the exchange as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_stock_price_date of this StockExchange.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_stock_price_date
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
            result = { 'last_stock_price_date': value }

        
        return result
        

    @last_stock_price_date.setter
    def last_stock_price_date(self, last_stock_price_date):
        """Sets the last_stock_price_date of this StockExchange.

        The latest date for which Intrinio has stock prices for the exchange  # noqa: E501

        :param last_stock_price_date: The last_stock_price_date of this StockExchange.  # noqa: E501
        :type: date
        """

        self._last_stock_price_date = last_stock_price_date

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
        if not isinstance(other, StockExchange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
