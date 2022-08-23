# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.29.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.thea_source_document import TheaSourceDocument  # noqa: F401,E501


class TheaEntityAnswer(object):
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
        'answer': 'str',
        'content': 'str',
        'source_documents': 'list[TheaSourceDocument]'
    }

    attribute_map = {
        'answer': 'answer',
        'content': 'content',
        'source_documents': 'source_documents'
    }

    def __init__(self, answer=None, content=None, source_documents=None):  # noqa: E501
        """TheaEntityAnswer - a model defined in Swagger"""  # noqa: E501

        self._answer = None
        self._content = None
        self._source_documents = None
        self.discriminator = None

        if answer is not None:
            self.answer = answer
        if content is not None:
            self.content = content
        if source_documents is not None:
            self.source_documents = source_documents

    @property
    def answer(self):
        """Gets the answer of this TheaEntityAnswer.  # noqa: E501

        The summarized answer returned from Thea  # noqa: E501

        :return: The answer of this TheaEntityAnswer.  # noqa: E501
        :rtype: str
        """
        return self._answer
        
    @property
    def answer_dict(self):
        """Gets the answer of this TheaEntityAnswer.  # noqa: E501

        The summarized answer returned from Thea as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The answer of this TheaEntityAnswer.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.answer
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
            result = { 'answer': value }

        
        return result
        

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this TheaEntityAnswer.

        The summarized answer returned from Thea  # noqa: E501

        :param answer: The answer of this TheaEntityAnswer.  # noqa: E501
        :type: str
        """

        self._answer = answer

    @property
    def content(self):
        """Gets the content of this TheaEntityAnswer.  # noqa: E501

        The underlying content the answer was sourced from  # noqa: E501

        :return: The content of this TheaEntityAnswer.  # noqa: E501
        :rtype: str
        """
        return self._content
        
    @property
    def content_dict(self):
        """Gets the content of this TheaEntityAnswer.  # noqa: E501

        The underlying content the answer was sourced from as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The content of this TheaEntityAnswer.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.content
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
            result = { 'content': value }

        
        return result
        

    @content.setter
    def content(self, content):
        """Sets the content of this TheaEntityAnswer.

        The underlying content the answer was sourced from  # noqa: E501

        :param content: The content of this TheaEntityAnswer.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def source_documents(self):
        """Gets the source_documents of this TheaEntityAnswer.  # noqa: E501

        The documents from which Thea answer data is sourced  # noqa: E501

        :return: The source_documents of this TheaEntityAnswer.  # noqa: E501
        :rtype: list[TheaSourceDocument]
        """
        return self._source_documents
        
    @property
    def source_documents_dict(self):
        """Gets the source_documents of this TheaEntityAnswer.  # noqa: E501

        The documents from which Thea answer data is sourced as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The source_documents of this TheaEntityAnswer.  # noqa: E501
        :rtype: list[TheaSourceDocument]
        """

        result = None

        value = self.source_documents
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
            result = { 'source_documents': value }

        
        return result
        

    @source_documents.setter
    def source_documents(self, source_documents):
        """Sets the source_documents of this TheaEntityAnswer.

        The documents from which Thea answer data is sourced  # noqa: E501

        :param source_documents: The source_documents of this TheaEntityAnswer.  # noqa: E501
        :type: list[TheaSourceDocument]
        """

        self._source_documents = source_documents

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
        if not isinstance(other, TheaEntityAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
