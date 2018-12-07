# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class StockExchangeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def filter_stock_exchanges(self, **kwargs):  # noqa: E501
        """Filter Stock Exchanges  # noqa: E501

        Return Stock Exchanges matching the given filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_stock_exchanges(async=True)
        >>> result = thread.get()

        :param async bool
        :param str city: Filter by city
        :param str country: Filter by country
        :param str country_code: Filter by ISO country code
        :return: ApiResponseStockExchanges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.filter_stock_exchanges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_stock_exchanges_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_stock_exchanges_with_http_info(self, **kwargs):  # noqa: E501
        """Filter Stock Exchanges  # noqa: E501

        Return Stock Exchanges matching the given filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_stock_exchanges_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str city: Filter by city
        :param str country: Filter by country
        :param str country_code: Filter by ISO country code
        :return: ApiResponseStockExchanges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['city', 'country', 'country_code']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_stock_exchanges" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'city' in params:
            query_params.append(('city', params['city']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/filter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchanges',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_stock_exchanges(self, **kwargs):  # noqa: E501
        """Get All Stock Exchanges  # noqa: E501

        Return All Stock Exchanges  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_stock_exchanges(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ApiResponseStockExchanges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_stock_exchanges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_stock_exchanges_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_stock_exchanges_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Stock Exchanges  # noqa: E501

        Return All Stock Exchanges  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_stock_exchanges_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ApiResponseStockExchanges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_stock_exchanges" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchanges',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_by_id(self, identifier, **kwargs):  # noqa: E501
        """Get Stock Exchange by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_by_id(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :return: StockExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_by_id_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_by_id_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_by_id_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get Stock Exchange by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_by_id_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :return: StockExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StockExchange',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_price_adjustments(self, identifier, **kwargs):  # noqa: E501
        """Get Stock Price Adjustments by Exchange  # noqa: E501

        Return stock price adjustments for the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_price_adjustments(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return price adjustments
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPriceAdjustments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_price_adjustments_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_price_adjustments_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_price_adjustments_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get Stock Price Adjustments by Exchange  # noqa: E501

        Return stock price adjustments for the Stock Exchange with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_price_adjustments_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return price adjustments
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPriceAdjustments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'date', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_price_adjustments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_price_adjustments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'date' in params:
            query_params.append(('date', params['date']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/prices/adjustments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeStockPriceAdjustments',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_prices(self, identifier, **kwargs):  # noqa: E501
        """Get Stock Prices by Exchange  # noqa: E501

        Return daily Stock Prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_prices(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return prices
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_prices_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_prices_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_prices_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get Stock Prices by Exchange  # noqa: E501

        Return daily Stock Prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_prices_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param date date: The date for which to return prices
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeStockPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'date', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_prices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_prices`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'date' in params:
            query_params.append(('date', params['date']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/prices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeStockPrices',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stock_exchange_securities(self, identifier, **kwargs):  # noqa: E501
        """Get Securities by Exchange  # noqa: E501

        Return Securities traded on the Stock Exchange with `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_securities(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeSecurities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stock_exchange_securities_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stock_exchange_securities_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_stock_exchange_securities_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get Securities by Exchange  # noqa: E501

        Return Securities traded on the Stock Exchange with `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stock_exchange_securities_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Stock Exchange identifier (MIC or Intrinio ID) (required)
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseStockExchangeSecurities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stock_exchange_securities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_stock_exchange_securities`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stock_exchanges/{identifier}/securities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStockExchangeSecurities',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
