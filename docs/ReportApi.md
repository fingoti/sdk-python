# fingoti.ReportApi

All URIs are relative to *https://api.fingoti.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_id_commands**](ReportApi.md#get_report_id_commands) | **GET** /v1/report/{id}/commands | Retrieve command log
[**get_report_usage**](ReportApi.md#get_report_usage) | **GET** /v1/report/usage | Retrieve property usage statistics per day per device


# **get_report_id_commands**
> CommandLogResponse get_report_id_commands(id, start=start, end=end, direction=direction)

Retrieve command log

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
    api_instance = fingoti.ReportApi(api_client)
    id = 'id_example' # str | 
start = 'start_example' # str |  (optional)
end = 'end_example' # str |  (optional)
direction = fingoti.CommandDirection() # CommandDirection |  (optional)

    try:
        # Retrieve command log
        api_response = api_instance.get_report_id_commands(id, start=start, end=end, direction=direction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportApi->get_report_id_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start** | **str**|  | [optional] 
 **end** | **str**|  | [optional] 
 **direction** | [**CommandDirection**](.md)|  | [optional] 

### Return type

[**CommandLogResponse**](CommandLogResponse.md)

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

# **get_report_usage**
> UsageTrackingResponse get_report_usage(start=start, end=end)

Retrieve property usage statistics per day per device

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
    api_instance = fingoti.ReportApi(api_client)
    start = 'start_example' # str |  (optional)
end = 'end_example' # str |  (optional)

    try:
        # Retrieve property usage statistics per day per device
        api_response = api_instance.get_report_usage(start=start, end=end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportApi->get_report_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] 
 **end** | **str**|  | [optional] 

### Return type

[**UsageTrackingResponse**](UsageTrackingResponse.md)

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

