# fingoti.FollowingsApi

All URIs are relative to *https://api.fingoti.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_followings_id**](FollowingsApi.md#delete_followings_id) | **DELETE** /v1/followings/{id} | Delete a Pin Following. This is not recoverable.
[**get_followings**](FollowingsApi.md#get_followings) | **GET** /v1/followings | Get all pin followings.
[**get_followings_id**](FollowingsApi.md#get_followings_id) | **GET** /v1/followings/{id} | Get specified pin following.
[**patch_followings_id**](FollowingsApi.md#patch_followings_id) | **PATCH** /v1/followings/{id} | Update pin following.
[**post_followings**](FollowingsApi.md#post_followings) | **POST** /v1/followings | Create a new pin following.


# **delete_followings_id**
> Default delete_followings_id(id)

Delete a Pin Following. This is not recoverable.

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
    api_instance = fingoti.FollowingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a Pin Following. This is not recoverable.
        api_response = api_instance.delete_followings_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FollowingsApi->delete_followings_id: %s\n" % e)
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_followings**
> OrganisationFollowingResponse get_followings(page_number=page_number, items_per_page=items_per_page, follow_name=follow_name, source=source, destination=destination)

Get all pin followings.

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
    api_instance = fingoti.FollowingsApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
follow_name = 'follow_name_example' # str |  (optional)
source = 'source_example' # str |  (optional)
destination = 'destination_example' # str |  (optional)

    try:
        # Get all pin followings.
        api_response = api_instance.get_followings(page_number=page_number, items_per_page=items_per_page, follow_name=follow_name, source=source, destination=destination)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FollowingsApi->get_followings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **follow_name** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **destination** | **str**|  | [optional] 

### Return type

[**OrganisationFollowingResponse**](OrganisationFollowingResponse.md)

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

# **get_followings_id**
> OrganisationFollowingResponse get_followings_id(id)

Get specified pin following.

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
    api_instance = fingoti.FollowingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get specified pin following.
        api_response = api_instance.get_followings_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FollowingsApi->get_followings_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrganisationFollowingResponse**](OrganisationFollowingResponse.md)

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

# **patch_followings_id**
> Default patch_followings_id(id, patch_follow_request=patch_follow_request)

Update pin following.

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
    api_instance = fingoti.FollowingsApi(api_client)
    id = 'id_example' # str | 
patch_follow_request = fingoti.PatchFollowRequest() # PatchFollowRequest |  (optional)

    try:
        # Update pin following.
        api_response = api_instance.patch_followings_id(id, patch_follow_request=patch_follow_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FollowingsApi->patch_followings_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_follow_request** | [**PatchFollowRequest**](PatchFollowRequest.md)|  | [optional] 

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

# **post_followings**
> DefaultWithId post_followings(add_follow_dto=add_follow_dto)

Create a new pin following.

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
    api_instance = fingoti.FollowingsApi(api_client)
    add_follow_dto = fingoti.AddFollowDto() # AddFollowDto |  (optional)

    try:
        # Create a new pin following.
        api_response = api_instance.post_followings(add_follow_dto=add_follow_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FollowingsApi->post_followings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_follow_dto** | [**AddFollowDto**](AddFollowDto.md)|  | [optional] 

### Return type

[**DefaultWithId**](DefaultWithId.md)

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

