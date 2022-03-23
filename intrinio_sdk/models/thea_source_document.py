# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.27.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TheaSourceDocument(object):
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
        'tags': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'tags': 'tags'
    }

    def __init__(self, id=None, tags=None):  # noqa: E501
        """TheaSourceDocument - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this TheaSourceDocument.  # noqa: E501

        The unique id for the Thea source document  # noqa: E501

        :return: The id of this TheaSourceDocument.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this TheaSourceDocument.  # noqa: E501

        The unique id for the Thea source document as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this TheaSourceDocument.  # noqa: E501
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
        """Sets the id of this TheaSourceDocument.

        The unique id for the Thea source document  # noqa: E501

        :param id: The id of this TheaSourceDocument.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tags(self):
        """Gets the tags of this TheaSourceDocument.  # noqa: E501

        Entity identifying tags associated with the source document  # noqa: E501

        :return: The tags of this TheaSourceDocument.  # noqa: E501
        :rtype: list[object]
        """
        return self._tags
        
    @property
    def tags_dict(self):
        """Gets the tags of this TheaSourceDocument.  # noqa: E501

        Entity identifying tags associated with the source document as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The tags of this TheaSourceDocument.  # noqa: E501
        :rtype: list[object]
        """

        result = None

        value = self.tags
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
            result = { 'tags': value }

        
        return result
        

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TheaSourceDocument.

        Entity identifying tags associated with the source document  # noqa: E501

        :param tags: The tags of this TheaSourceDocument.  # noqa: E501
        :type: list[object]
        """

        self._tags = tags

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
        if not isinstance(other, TheaSourceDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
