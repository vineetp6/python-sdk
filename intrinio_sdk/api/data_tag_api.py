# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.27.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class DataTagApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_data_tags(self, **kwargs):  # noqa: E501
        """All Data Tags  # noqa: E501

        Returns all Data Tags. Returns Data Tags matching parameters when specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_data_tags(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str tag: Tag
        :param str type: Type
        :param str parent: ID of tag parent
        :param str statement_code: Statement Code
        :param str fs_template: Template
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseDataTags
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_data_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_data_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_data_tags_with_http_info(self, **kwargs):  # noqa: E501
        """All Data Tags  # noqa: E501

        Returns all Data Tags. Returns Data Tags matching parameters when specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_data_tags_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str tag: Tag
        :param str type: Type
        :param str parent: ID of tag parent
        :param str statement_code: Statement Code
        :param str fs_template: Template
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseDataTags
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag', 'type', 'parent', 'statement_code', 'fs_template', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_data_tags" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_all_data_tags`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'parent' in params:
            query_params.append(('parent', params['parent']))  # noqa: E501
        if 'statement_code' in params:
            query_params.append(('statement_code', params['statement_code']))  # noqa: E501
        if 'fs_template' in params:
            query_params.append(('fs_template', params['fs_template']))  # noqa: E501
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
            '/data_tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseDataTags',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_data_tag_by_id(self, identifier, **kwargs):  # noqa: E501
        """Lookup Data Tag  # noqa: E501

        Returns the Data Tag with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_data_tag_by_id(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID or the code-name of the Data Tag (required)
        :return: DataTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_data_tag_by_id_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_data_tag_by_id_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_data_tag_by_id_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Lookup Data Tag  # noqa: E501

        Returns the Data Tag with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_data_tag_by_id_with_http_info(identifier, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID or the code-name of the Data Tag (required)
        :return: DataTag
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
                    " to method get_data_tag_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_data_tag_by_id`")  # noqa: E501

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
            '/data_tags/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataTag',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_data_tags(self, query, **kwargs):  # noqa: E501
        """Search Data Tags  # noqa: E501

        Searches for Data Tags matching the text `query`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_data_tags(query, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: (required)
        :param int page_size: The number of results to return
        :return: ApiResponseDataTagsSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_data_tags_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_data_tags_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_data_tags_with_http_info(self, query, **kwargs):  # noqa: E501
        """Search Data Tags  # noqa: E501

        Searches for Data Tags matching the text `query`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_data_tags_with_http_info(query, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: (required)
        :param int page_size: The number of results to return
        :return: ApiResponseDataTagsSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_data_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_data_tags`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `search_data_tags`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

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
            '/data_tags/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseDataTagsSearch',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
