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


class BulkDownloadLinks(object):
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
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, name=None, url=None):  # noqa: E501
        """BulkDownloadLinks - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this BulkDownloadLinks.  # noqa: E501

        The name of the file  # noqa: E501

        :return: The name of this BulkDownloadLinks.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this BulkDownloadLinks.  # noqa: E501

        The name of the file as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this BulkDownloadLinks.  # noqa: E501
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
        """Sets the name of this BulkDownloadLinks.

        The name of the file  # noqa: E501

        :param name: The name of this BulkDownloadLinks.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this BulkDownloadLinks.  # noqa: E501

        Link for accessing the bulk download. Expires in 24 hours.  # noqa: E501

        :return: The url of this BulkDownloadLinks.  # noqa: E501
        :rtype: str
        """
        return self._url
        
    @property
    def url_dict(self):
        """Gets the url of this BulkDownloadLinks.  # noqa: E501

        Link for accessing the bulk download. Expires in 24 hours. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The url of this BulkDownloadLinks.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.url
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
            result = { 'url': value }

        
        return result
        

    @url.setter
    def url(self, url):
        """Sets the url of this BulkDownloadLinks.

        Link for accessing the bulk download. Expires in 24 hours.  # noqa: E501

        :param url: The url of this BulkDownloadLinks.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, BulkDownloadLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
