# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.52.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.data_tag_api import DataTagApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestDataTagApi(unittest.TestCase):
    """DataTagApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.data_tag_api.DataTagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_data_tags(self):
        """Test case for get_all_data_tags

        All Data Tags  # noqa: E501
        """
        pass

    def test_get_data_tag_by_id(self):
        """Test case for get_data_tag_by_id

        Lookup Data Tag  # noqa: E501
        """
        pass

    def test_search_data_tags(self):
        """Test case for search_data_tags

        Search Data Tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
