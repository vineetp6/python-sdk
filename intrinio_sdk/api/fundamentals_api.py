# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.43.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class FundamentalsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def filter_fundamental(self, **kwargs):  # noqa: E501
        """Filter Fundamental  # noqa: E501

        Returns fundamentals that meet the set of filters specified in parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_fundamental(_async=True)
        >>> result = thread.get()

        :param async bool
        :param date filed_after: Only include fundamentals that were filed on or after this date.
        :param date filed_before: Only include fundamentals that were filed on or before this date.
        :param bool reported_only: Only as-reported fundamentals
        :param int fiscal_year: Only for the given fiscal year
        :param str statement_code: Only of the given statement code
        :param str type: Only of the given type
        :param str fiscal_period: The fiscal period
        :param date start_date: Only include fundamentals where covered period is on or after this date.
        :param date end_date: Only include fundamentals where covered period is on or before this date.
        :param str next_page: Gets the next page of data from a previous API call
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.filter_fundamental_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_fundamental_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_fundamental_with_http_info(self, **kwargs):  # noqa: E501
        """Filter Fundamental  # noqa: E501

        Returns fundamentals that meet the set of filters specified in parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_fundamental_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param date filed_after: Only include fundamentals that were filed on or after this date.
        :param date filed_before: Only include fundamentals that were filed on or before this date.
        :param bool reported_only: Only as-reported fundamentals
        :param int fiscal_year: Only for the given fiscal year
        :param str statement_code: Only of the given statement code
        :param str type: Only of the given type
        :param str fiscal_period: The fiscal period
        :param date start_date: Only include fundamentals where covered period is on or after this date.
        :param date end_date: Only include fundamentals where covered period is on or before this date.
        :param str next_page: Gets the next page of data from a previous API call
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filed_after', 'filed_before', 'reported_only', 'fiscal_year', 'statement_code', 'type', 'fiscal_period', 'start_date', 'end_date', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_fundamental" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filed_after' in params:
            query_params.append(('filed_after', params['filed_after']))  # noqa: E501
        if 'filed_before' in params:
            query_params.append(('filed_before', params['filed_before']))  # noqa: E501
        if 'reported_only' in params:
            query_params.append(('reported_only', params['reported_only']))  # noqa: E501
        if 'fiscal_year' in params:
            query_params.append(('fiscal_year', params['fiscal_year']))  # noqa: E501
        if 'statement_code' in params:
            query_params.append(('statement_code', params['statement_code']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'fiscal_period' in params:
            query_params.append(('fiscal_period', params['fiscal_period']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
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
            '/fundamentals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fundamental',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundamental_by_id(self, id, **kwargs):  # noqa: E501
        """Fundamental by ID  # noqa: E501

        Returns a specific fundamental associated with a particular unique fundamental ID. Useful for pulling reference data for a specific fundamental.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_by_id(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID for the Fundamental (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fundamental_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Fundamental by ID  # noqa: E501

        Returns a specific fundamental associated with a particular unique fundamental ID. Useful for pulling reference data for a specific fundamental.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_by_id_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID for the Fundamental (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/fundamentals/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fundamental',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundamental_reported_financials(self, id, **kwargs):  # noqa: E501
        """Reported Financials  # noqa: E501

        Returns as-reported financial statement data for income statement, balance sheet, and cash flow statement. Data for income statement and cash flow statement is available on a FY, QTR (Q1, Q2, Q3, Q4), TTM (Q1TTM, Q2TTM, Q3TTM), and YTD (Q2YTD, Q3YTD) basis. Data for the balance sheet is available on a FY or QTR (Q1, Q2, Q3, Q4) basis only due its point-in-time nature.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_reported_financials(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseReportedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_reported_financials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_reported_financials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fundamental_reported_financials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Reported Financials  # noqa: E501

        Returns as-reported financial statement data for income statement, balance sheet, and cash flow statement. Data for income statement and cash flow statement is available on a FY, QTR (Q1, Q2, Q3, Q4), TTM (Q1TTM, Q2TTM, Q3TTM), and YTD (Q2YTD, Q3YTD) basis. Data for the balance sheet is available on a FY or QTR (Q1, Q2, Q3, Q4) basis only due its point-in-time nature.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_reported_financials_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseReportedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_reported_financials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_reported_financials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/fundamentals/{id}/reported_financials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseReportedFinancials',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundamental_standardized_financials(self, id, **kwargs):  # noqa: E501
        """Standardized Financials  # noqa: E501

        Returns standardized financial statement data for income statement, balance sheet, cash flow statement and over 100 associated calculations for a given company. Data for income statement, cash flow statement, and calculations is available on a FY, QTR (Q1, Q2, Q3, Q4), TTM (Q1TTM, Q2TTM, Q3TTM), and YTD (Q2YTD, Q3YTD) basis. Data for the balance sheet is available on a FY or QTR (Q1, Q2, Q3, Q4) basis only due its point-in-time nature.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_standardized_financials(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseStandardizedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_standardized_financials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_standardized_financials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fundamental_standardized_financials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Standardized Financials  # noqa: E501

        Returns standardized financial statement data for income statement, balance sheet, cash flow statement and over 100 associated calculations for a given company. Data for income statement, cash flow statement, and calculations is available on a FY, QTR (Q1, Q2, Q3, Q4), TTM (Q1TTM, Q2TTM, Q3TTM), and YTD (Q2YTD, Q3YTD) basis. Data for the balance sheet is available on a FY or QTR (Q1, Q2, Q3, Q4) basis only due its point-in-time nature.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_standardized_financials_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseStandardizedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_standardized_financials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_standardized_financials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/fundamentals/{id}/standardized_financials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStandardizedFinancials',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundamental_standardized_financials_dimensions(self, id, tag, **kwargs):  # noqa: E501
        """Standardized Financials Dimensions  # noqa: E501

        Returns as reported dimensionality of a data tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_standardized_financials_dimensions(id, tag, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :param str tag: An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>) (required)
        :return: ApiResponseStandardizedFinancialsDimensions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_standardized_financials_dimensions_with_http_info(id, tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_standardized_financials_dimensions_with_http_info(id, tag, **kwargs)  # noqa: E501
            return data

    def get_fundamental_standardized_financials_dimensions_with_http_info(self, id, tag, **kwargs):  # noqa: E501
        """Standardized Financials Dimensions  # noqa: E501

        Returns as reported dimensionality of a data tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_standardized_financials_dimensions_with_http_info(id, tag, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :param str tag: An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>) (required)
        :return: ApiResponseStandardizedFinancialsDimensions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_standardized_financials_dimensions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_standardized_financials_dimensions`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_fundamental_standardized_financials_dimensions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'tag' in params:
            path_params['tag'] = params['tag']  # noqa: E501

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
            '/fundamentals/{id}/standardized_financials/dimensions/{tag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStandardizedFinancialsDimensions',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lookup_fundamental(self, identifier, statement_code, fiscal_year, fiscal_period, **kwargs):  # noqa: E501
        """Lookup Fundamental  # noqa: E501

        Returns a specific fundamental with unique fundamental ID associated with a particular company, year, period and statement. Useful for pulling the unique fundamental ID and reference data for a specific fundamental.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.lookup_fundamental(identifier, statement_code, fiscal_year, fiscal_period, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Company identifier (Ticker, CIK, LEI, Intrinio ID) (required)
        :param str statement_code: The statement code (required)
        :param int fiscal_year: The fiscal year (required)
        :param str fiscal_period: The fiscal period (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.lookup_fundamental_with_http_info(identifier, statement_code, fiscal_year, fiscal_period, **kwargs)  # noqa: E501
        else:
            (data) = self.lookup_fundamental_with_http_info(identifier, statement_code, fiscal_year, fiscal_period, **kwargs)  # noqa: E501
            return data

    def lookup_fundamental_with_http_info(self, identifier, statement_code, fiscal_year, fiscal_period, **kwargs):  # noqa: E501
        """Lookup Fundamental  # noqa: E501

        Returns a specific fundamental with unique fundamental ID associated with a particular company, year, period and statement. Useful for pulling the unique fundamental ID and reference data for a specific fundamental.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.lookup_fundamental_with_http_info(identifier, statement_code, fiscal_year, fiscal_period, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Company identifier (Ticker, CIK, LEI, Intrinio ID) (required)
        :param str statement_code: The statement code (required)
        :param int fiscal_year: The fiscal year (required)
        :param str fiscal_period: The fiscal period (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'statement_code', 'fiscal_year', 'fiscal_period']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_fundamental" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `lookup_fundamental`")  # noqa: E501
        # verify the required parameter 'statement_code' is set
        if ('statement_code' not in params or
                params['statement_code'] is None):
            raise ValueError("Missing the required parameter `statement_code` when calling `lookup_fundamental`")  # noqa: E501
        # verify the required parameter 'fiscal_year' is set
        if ('fiscal_year' not in params or
                params['fiscal_year'] is None):
            raise ValueError("Missing the required parameter `fiscal_year` when calling `lookup_fundamental`")  # noqa: E501
        # verify the required parameter 'fiscal_period' is set
        if ('fiscal_period' not in params or
                params['fiscal_period'] is None):
            raise ValueError("Missing the required parameter `fiscal_period` when calling `lookup_fundamental`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'statement_code' in params:
            path_params['statement_code'] = params['statement_code']  # noqa: E501
        if 'fiscal_year' in params:
            path_params['fiscal_year'] = params['fiscal_year']  # noqa: E501
        if 'fiscal_period' in params:
            path_params['fiscal_period'] = params['fiscal_period']  # noqa: E501

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
            '/fundamentals/lookup/{identifier}/{statement_code}/{fiscal_year}/{fiscal_period}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fundamental',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
