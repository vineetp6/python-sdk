# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.25.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class ETFsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_etfs(self, **kwargs):  # noqa: E501
        """All ETFs  # noqa: E501

        Returns a list of Exchange Traded Funds (ETFs) sourced from FirstBridge  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_etfs(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str exchange:
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseETFs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_etfs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_etfs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_etfs_with_http_info(self, **kwargs):  # noqa: E501
        """All ETFs  # noqa: E501

        Returns a list of Exchange Traded Funds (ETFs) sourced from FirstBridge  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_etfs_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str exchange:
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseETFs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exchange', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_etfs" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_all_etfs`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
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
            '/etfs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseETFs',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_etf(self, identifier, **kwargs):  # noqa: E501
        """Lookup ETF  # noqa: E501

        Returns the Exchange Traded Fund (ETF) with the given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :return: ETF
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_etf_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_etf_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_etf_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Lookup ETF  # noqa: E501

        Returns the Exchange Traded Fund (ETF) with the given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :return: ETF
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
                    " to method get_etf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_etf`")  # noqa: E501

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
            '/etfs/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ETF',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_etf_analytics(self, identifier, **kwargs):  # noqa: E501
        """ETF Analytics  # noqa: E501

        Returns analytics for the Exchange Traded Fund (ETF) including volume, market cap, 52 week high, and 52 week low  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_analytics(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :return: ETFAnalytics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_etf_analytics_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_etf_analytics_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_etf_analytics_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """ETF Analytics  # noqa: E501

        Returns analytics for the Exchange Traded Fund (ETF) including volume, market cap, 52 week high, and 52 week low  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_analytics_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :return: ETFAnalytics
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
                    " to method get_etf_analytics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_etf_analytics`")  # noqa: E501

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
            '/etfs/{identifier}/analytics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ETFAnalytics',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_etf_holdings(self, identifier, **kwargs):  # noqa: E501
        """ETF Holdings  # noqa: E501

        Returns the holdings sorted by weight descending and the Exchange Traded Fund (ETF) summary  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_holdings(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseETFHoldings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_etf_holdings_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_etf_holdings_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_etf_holdings_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """ETF Holdings  # noqa: E501

        Returns the holdings sorted by weight descending and the Exchange Traded Fund (ETF) summary  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_holdings_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseETFHoldings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_etf_holdings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_etf_holdings`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_etf_holdings`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
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
            '/etfs/{identifier}/holdings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseETFHoldings',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_etf_stats(self, identifier, **kwargs):  # noqa: E501
        """Exchange Traded Fund (ETF) stats  # noqa: E501

        Returns daily stats for the Exchange Traded Fund (ETF) including net asset value, beta vs spy, returns, and volatility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_stats(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :return: ETFStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_etf_stats_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_etf_stats_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_etf_stats_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Exchange Traded Fund (ETF) stats  # noqa: E501

        Returns daily stats for the Exchange Traded Fund (ETF) including net asset value, beta vs spy, returns, and volatility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_etf_stats_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: An ETF identifier (Ticker, Figi Ticker, ISIN, RIC, Intrinio ID) (required)
        :return: ETFStats
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
                    " to method get_etf_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_etf_stats`")  # noqa: E501

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
            '/etfs/{identifier}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ETFStats',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_etfs(self, query, **kwargs):  # noqa: E501
        """Search ETFs  # noqa: E501

        Searches for Exchange Traded Funds (ETFs) matching the text `query`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_etfs(query, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: (required)
        :return: ApiResponseETFs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_etfs_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_etfs_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_etfs_with_http_info(self, query, **kwargs):  # noqa: E501
        """Search ETFs  # noqa: E501

        Searches for Exchange Traded Funds (ETFs) matching the text `query`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_etfs_with_http_info(query, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: (required)
        :return: ApiResponseETFs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_etfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_etfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

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
            '/etfs/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseETFs',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
