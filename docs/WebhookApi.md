# fingoti.WebhookApi

All URIs are relative to *https://api.fingoti.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook_id**](WebhookApi.md#delete_webhook_id) | **DELETE** /v1/webhook/{id} | Delete a Webhook. This is not recoverable.
[**get_webhook**](WebhookApi.md#get_webhook) | **GET** /v1/webhook | Get all registered webhooks.
[**get_webhook_id**](WebhookApi.md#get_webhook_id) | **GET** /v1/webhook/{id} | Get specified webhook.
[**get_webhook_logs**](WebhookApi.md#get_webhook_logs) | **GET** /v1/webhook/logs | Get all registered webhooks with call logs.
[**patch_webhook_id**](WebhookApi.md#patch_webhook_id) | **PATCH** /v1/webhook/{id} | Update Fingoti webhook.
[**post_webhook**](WebhookApi.md#post_webhook) | **POST** /v1/webhook | Register a new webhook.
[**post_webhook_retry**](WebhookApi.md#post_webhook_retry) | **POST** /v1/webhook/retry | Retry a webhook.


# **delete_webhook_id**
> Default delete_webhook_id(id)

Delete a Webhook. This is not recoverable.

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
    api_instance = fingoti.WebhookApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a Webhook. This is not recoverable.
        api_response = api_instance.delete_webhook_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->delete_webhook_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> EngineWebhooksResponse get_webhook(page_number=page_number, items_per_page=items_per_page, webhook_number=webhook_number, _property=_property)

Get all registered webhooks.

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
    api_instance = fingoti.WebhookApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
webhook_number = 'webhook_number_example' # str |  (optional)
_property = '_property_example' # str |  (optional)

    try:
        # Get all registered webhooks.
        api_response = api_instance.get_webhook(page_number=page_number, items_per_page=items_per_page, webhook_number=webhook_number, _property=_property)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **webhook_number** | **str**|  | [optional] 
 **_property** | **str**|  | [optional] 

### Return type

[**EngineWebhooksResponse**](EngineWebhooksResponse.md)

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

# **get_webhook_id**
> EngineWebhookResponse get_webhook_id(id, page_number=page_number, items_per_page=items_per_page, status=status)

Get specified webhook.

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
    api_instance = fingoti.WebhookApi(api_client)
    id = 'id_example' # str | 
page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
status = [56] # list[int] |  (optional)

    try:
        # Get specified webhook.
        api_response = api_instance.get_webhook_id(id, page_number=page_number, items_per_page=items_per_page, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **status** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**EngineWebhookResponse**](EngineWebhookResponse.md)

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

# **get_webhook_logs**
> WebhookLogsResponse get_webhook_logs(page_number=page_number, items_per_page=items_per_page, status=status, webhook_number=webhook_number)

Get all registered webhooks with call logs.

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
    api_instance = fingoti.WebhookApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
status = [56] # list[int] |  (optional)
webhook_number = 'webhook_number_example' # str |  (optional)

    try:
        # Get all registered webhooks with call logs.
        api_response = api_instance.get_webhook_logs(page_number=page_number, items_per_page=items_per_page, status=status, webhook_number=webhook_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **status** | [**list[int]**](int.md)|  | [optional] 
 **webhook_number** | **str**|  | [optional] 

### Return type

[**WebhookLogsResponse**](WebhookLogsResponse.md)

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

# **patch_webhook_id**
> Default patch_webhook_id(id, patch_webhook_request=patch_webhook_request)

Update Fingoti webhook.

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
    api_instance = fingoti.WebhookApi(api_client)
    id = 'id_example' # str | 
patch_webhook_request = fingoti.PatchWebhookRequest() # PatchWebhookRequest |  (optional)

    try:
        # Update Fingoti webhook.
        api_response = api_instance.patch_webhook_id(id, patch_webhook_request=patch_webhook_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->patch_webhook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_webhook_request** | [**PatchWebhookRequest**](PatchWebhookRequest.md)|  | [optional] 

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

# **post_webhook**
> AddWebhookResult post_webhook(add_webhook_dto=add_webhook_dto)

Register a new webhook.

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
    api_instance = fingoti.WebhookApi(api_client)
    add_webhook_dto = fingoti.AddWebhookDto() # AddWebhookDto |  (optional)

    try:
        # Register a new webhook.
        api_response = api_instance.post_webhook(add_webhook_dto=add_webhook_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->post_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_webhook_dto** | [**AddWebhookDto**](AddWebhookDto.md)|  | [optional] 

### Return type

[**AddWebhookResult**](AddWebhookResult.md)

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

# **post_webhook_retry**
> Default post_webhook_retry(webhook_retry_request=webhook_retry_request)

Retry a webhook.

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
    api_instance = fingoti.WebhookApi(api_client)
    webhook_retry_request = fingoti.WebhookRetryRequest() # WebhookRetryRequest |  (optional)

    try:
        # Retry a webhook.
        api_response = api_instance.post_webhook_retry(webhook_retry_request=webhook_retry_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->post_webhook_retry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_retry_request** | [**WebhookRetryRequest**](WebhookRetryRequest.md)|  | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

