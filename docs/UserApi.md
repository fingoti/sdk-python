# fingoti.UserApi

All URIs are relative to *https://api.fingoti.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_tokens_id**](UserApi.md#delete_user_tokens_id) | **DELETE** /v1/user/tokens/{id} | Delete a Token. Token will no longer authenticate API requests. This is not recoverable.
[**get_user**](UserApi.md#get_user) | **GET** /v1/user | Get your Fingoti user.
[**get_user_organisations**](UserApi.md#get_user_organisations) | **GET** /v1/user/organisations | Get all organisations you are a member of.
[**get_user_sessions**](UserApi.md#get_user_sessions) | **GET** /v1/user/sessions | Get all user sessions.
[**get_user_tokens**](UserApi.md#get_user_tokens) | **GET** /v1/user/tokens | Get all API tokens.
[**get_user_tokens_id**](UserApi.md#get_user_tokens_id) | **GET** /v1/user/tokens/{id} | Get specified token.
[**patch_user**](UserApi.md#patch_user) | **PATCH** /v1/user | Update Fingoti user.
[**patch_user_tokens_id**](UserApi.md#patch_user_tokens_id) | **PATCH** /v1/user/tokens/{id} | Update API token.
[**post_user**](UserApi.md#post_user) | **POST** /v1/user | Register a new Fingoti user.
[**post_user_tokens**](UserApi.md#post_user_tokens) | **POST** /v1/user/tokens | Generate new API token.


# **delete_user_tokens_id**
> Default delete_user_tokens_id(id)

Delete a Token. Token will no longer authenticate API requests. This is not recoverable.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a Token. Token will no longer authenticate API requests. This is not recoverable.
        api_response = api_instance.delete_user_tokens_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user_tokens_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Default**](Default.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetProfileResponse get_user()

Get your Fingoti user.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    
    try:
        # Get your Fingoti user.
        api_response = api_instance.get_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProfileResponse**](GetProfileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_organisations**
> PortalUserOrganisationsDto get_user_organisations(page_number=page_number, items_per_page=items_per_page, organisation_name=organisation_name)

Get all organisations you are a member of.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
organisation_name = 'organisation_name_example' # str |  (optional)

    try:
        # Get all organisations you are a member of.
        api_response = api_instance.get_user_organisations(page_number=page_number, items_per_page=items_per_page, organisation_name=organisation_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **organisation_name** | **str**|  | [optional] 

### Return type

[**PortalUserOrganisationsDto**](PortalUserOrganisationsDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_sessions**
> UserSessionsResponse get_user_sessions(page_number=page_number, items_per_page=items_per_page)

Get all user sessions.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)

    try:
        # Get all user sessions.
        api_response = api_instance.get_user_sessions(page_number=page_number, items_per_page=items_per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 

### Return type

[**UserSessionsResponse**](UserSessionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tokens**
> UserTokenResponse get_user_tokens(page_number=page_number, items_per_page=items_per_page, token_name=token_name)

Get all API tokens.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
token_name = 'token_name_example' # str |  (optional)

    try:
        # Get all API tokens.
        api_response = api_instance.get_user_tokens(page_number=page_number, items_per_page=items_per_page, token_name=token_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **token_name** | **str**|  | [optional] 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tokens_id**
> UserTokenResponse get_user_tokens_id(id)

Get specified token.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get specified token.
        api_response = api_instance.get_user_tokens_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_tokens_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user**
> Default patch_user(patch_user_request=patch_user_request)

Update Fingoti user.

Fields that do not require updating can be omitted

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    patch_user_request = fingoti.PatchUserRequest() # PatchUserRequest |  (optional)

    try:
        # Update Fingoti user.
        api_response = api_instance.patch_user(patch_user_request=patch_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->patch_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_user_request** | [**PatchUserRequest**](PatchUserRequest.md)|  | [optional] 

### Return type

[**Default**](Default.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user_tokens_id**
> Default patch_user_tokens_id(id, patch_user_token_request=patch_user_token_request)

Update API token.

Fields that do not require updating can be omitted

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    id = 'id_example' # str | 
patch_user_token_request = fingoti.PatchUserTokenRequest() # PatchUserTokenRequest |  (optional)

    try:
        # Update API token.
        api_response = api_instance.patch_user_tokens_id(id, patch_user_token_request=patch_user_token_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->patch_user_tokens_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_user_token_request** | [**PatchUserTokenRequest**](PatchUserTokenRequest.md)|  | [optional] 

### Return type

[**Default**](Default.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> DefaultWithToken post_user(register_user_dto=register_user_dto)

Register a new Fingoti user.

The returned token is a Register token and is used to register a new Organisation

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    register_user_dto = fingoti.RegisterUserDto() # RegisterUserDto |  (optional)

    try:
        # Register a new Fingoti user.
        api_response = api_instance.post_user(register_user_dto=register_user_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->post_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_dto** | [**RegisterUserDto**](RegisterUserDto.md)|  | [optional] 

### Return type

[**DefaultWithToken**](DefaultWithToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_tokens**
> TokenSuccessResponse post_user_tokens(new_user_token_dto=new_user_token_dto)

Generate new API token.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import fingoti
from fingoti.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fingoti.UserApi(api_client)
    new_user_token_dto = fingoti.NewUserTokenDto() # NewUserTokenDto | User credentials. For a token to never expire, specify 0 for the expiry (optional)

    try:
        # Generate new API token.
        api_response = api_instance.post_user_tokens(new_user_token_dto=new_user_token_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->post_user_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_user_token_dto** | [**NewUserTokenDto**](NewUserTokenDto.md)| User credentials. For a token to never expire, specify 0 for the expiry | [optional] 

### Return type

[**TokenSuccessResponse**](TokenSuccessResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

