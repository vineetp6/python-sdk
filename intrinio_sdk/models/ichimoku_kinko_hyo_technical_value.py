# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.20.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IchimokuKinkoHyoTechnicalValue(object):
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
        'date_time': 'datetime',
        'chikou_span': 'float',
        'kijun_sen': 'float',
        'senkou_span_a': 'float',
        'senkou_span_b': 'float',
        'tenkan_sen': 'float'
    }

    attribute_map = {
        'date_time': 'date_time',
        'chikou_span': 'chikou_span',
        'kijun_sen': 'kijun_sen',
        'senkou_span_a': 'senkou_span_a',
        'senkou_span_b': 'senkou_span_b',
        'tenkan_sen': 'tenkan_sen'
    }

    def __init__(self, date_time=None, chikou_span=None, kijun_sen=None, senkou_span_a=None, senkou_span_b=None, tenkan_sen=None):  # noqa: E501
        """IchimokuKinkoHyoTechnicalValue - a model defined in Swagger"""  # noqa: E501

        self._date_time = None
        self._chikou_span = None
        self._kijun_sen = None
        self._senkou_span_a = None
        self._senkou_span_b = None
        self._tenkan_sen = None
        self.discriminator = None

        if date_time is not None:
            self.date_time = date_time
        if chikou_span is not None:
            self.chikou_span = chikou_span
        if kijun_sen is not None:
            self.kijun_sen = kijun_sen
        if senkou_span_a is not None:
            self.senkou_span_a = senkou_span_a
        if senkou_span_b is not None:
            self.senkou_span_b = senkou_span_b
        if tenkan_sen is not None:
            self.tenkan_sen = tenkan_sen

    @property
    def date_time(self):
        """Gets the date_time of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The date_time of the observation  # noqa: E501

        :return: The date_time of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time
        
    @property
    def date_time_dict(self):
        """Gets the date_time of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The date_time of the observation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date_time of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.date_time
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
            result = { 'date_time': value }

        
        return result
        

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this IchimokuKinkoHyoTechnicalValue.

        The date_time of the observation  # noqa: E501

        :param date_time: The date_time of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def chikou_span(self):
        """Gets the chikou_span of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Chikou Span (Lagging Span) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :return: The chikou_span of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._chikou_span
        
    @property
    def chikou_span_dict(self):
        """Gets the chikou_span of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Chikou Span (Lagging Span) value of the Ichimoku Kinko Hyo calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The chikou_span of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.chikou_span
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
            result = { 'chikou_span': value }

        
        return result
        

    @chikou_span.setter
    def chikou_span(self, chikou_span):
        """Sets the chikou_span of this IchimokuKinkoHyoTechnicalValue.

        The Chikou Span (Lagging Span) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :param chikou_span: The chikou_span of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :type: float
        """

        self._chikou_span = chikou_span

    @property
    def kijun_sen(self):
        """Gets the kijun_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Kijun-sen (Base Line) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :return: The kijun_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._kijun_sen
        
    @property
    def kijun_sen_dict(self):
        """Gets the kijun_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Kijun-sen (Base Line) value of the Ichimoku Kinko Hyo calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The kijun_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.kijun_sen
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
            result = { 'kijun_sen': value }

        
        return result
        

    @kijun_sen.setter
    def kijun_sen(self, kijun_sen):
        """Sets the kijun_sen of this IchimokuKinkoHyoTechnicalValue.

        The Kijun-sen (Base Line) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :param kijun_sen: The kijun_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :type: float
        """

        self._kijun_sen = kijun_sen

    @property
    def senkou_span_a(self):
        """Gets the senkou_span_a of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Senkou Span A (Leading Span A) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :return: The senkou_span_a of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._senkou_span_a
        
    @property
    def senkou_span_a_dict(self):
        """Gets the senkou_span_a of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Senkou Span A (Leading Span A) value of the Ichimoku Kinko Hyo calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The senkou_span_a of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.senkou_span_a
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
            result = { 'senkou_span_a': value }

        
        return result
        

    @senkou_span_a.setter
    def senkou_span_a(self, senkou_span_a):
        """Sets the senkou_span_a of this IchimokuKinkoHyoTechnicalValue.

        The Senkou Span A (Leading Span A) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :param senkou_span_a: The senkou_span_a of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :type: float
        """

        self._senkou_span_a = senkou_span_a

    @property
    def senkou_span_b(self):
        """Gets the senkou_span_b of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Senkou Span B (Leading Span B) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :return: The senkou_span_b of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._senkou_span_b
        
    @property
    def senkou_span_b_dict(self):
        """Gets the senkou_span_b of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Senkou Span B (Leading Span B) value of the Ichimoku Kinko Hyo calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The senkou_span_b of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.senkou_span_b
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
            result = { 'senkou_span_b': value }

        
        return result
        

    @senkou_span_b.setter
    def senkou_span_b(self, senkou_span_b):
        """Sets the senkou_span_b of this IchimokuKinkoHyoTechnicalValue.

        The Senkou Span B (Leading Span B) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :param senkou_span_b: The senkou_span_b of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :type: float
        """

        self._senkou_span_b = senkou_span_b

    @property
    def tenkan_sen(self):
        """Gets the tenkan_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Tenskan-sen (Conversion Line) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :return: The tenkan_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._tenkan_sen
        
    @property
    def tenkan_sen_dict(self):
        """Gets the tenkan_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501

        The Tenskan-sen (Conversion Line) value of the Ichimoku Kinko Hyo calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The tenkan_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.tenkan_sen
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
            result = { 'tenkan_sen': value }

        
        return result
        

    @tenkan_sen.setter
    def tenkan_sen(self, tenkan_sen):
        """Sets the tenkan_sen of this IchimokuKinkoHyoTechnicalValue.

        The Tenskan-sen (Conversion Line) value of the Ichimoku Kinko Hyo calculation  # noqa: E501

        :param tenkan_sen: The tenkan_sen of this IchimokuKinkoHyoTechnicalValue.  # noqa: E501
        :type: float
        """

        self._tenkan_sen = tenkan_sen

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
        if not isinstance(other, IchimokuKinkoHyoTechnicalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
