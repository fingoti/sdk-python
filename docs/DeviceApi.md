# fingoti.DeviceApi

All URIs are relative to *https://api.fingoti.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device_id**](DeviceApi.md#delete_device_id) | **DELETE** /v1/device/{id} | Unclaim a Fingoti device.
[**get_device**](DeviceApi.md#get_device) | **GET** /v1/device | Get all devices.
[**get_device_id**](DeviceApi.md#get_device_id) | **GET** /v1/device/{id} | Get specified device.
[**get_device_id_nodes**](DeviceApi.md#get_device_id_nodes) | **GET** /v1/device/{id}/nodes | Get all nodes latched to a gateway.
[**patch_device_id**](DeviceApi.md#patch_device_id) | **PATCH** /v1/device/{id} | Update your Fingoti device.
[**post_device**](DeviceApi.md#post_device) | **POST** /v1/device | Claim a new Fingoti device.
[**post_device_sendrequest**](DeviceApi.md#post_device_sendrequest) | **POST** /v1/device/sendrequest | Send a request to a Fingoti device.
[**post_device_update**](DeviceApi.md#post_device_update) | **POST** /v1/device/update | Initiate a device update.


# **delete_device_id**
> UpdateResponse delete_device_id(id)

Unclaim a Fingoti device.

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
    api_instance = fingoti.DeviceApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unclaim a Fingoti device.
        api_response = api_instance.delete_device_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->delete_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

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

# **get_device**
> ClaimedDevicesDto get_device(last_updated=last_updated)

Get all devices.

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
    api_instance = fingoti.DeviceApi(api_client)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get all devices.
        api_response = api_instance.get_device(last_updated=last_updated)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **datetime**|  | [optional] 

### Return type

[**ClaimedDevicesDto**](ClaimedDevicesDto.md)

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

# **get_device_id**
> ClaimedDeviceResponse get_device_id(id)

Get specified device.

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
    api_instance = fingoti.DeviceApi(api_client)
    id = 'id_example' # str | Device ID to query.

    try:
        # Get specified device.
        api_response = api_instance.get_device_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID to query. | 

### Return type

[**ClaimedDeviceResponse**](ClaimedDeviceResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_id_nodes**
> DeviceNodesResponse get_device_id_nodes(id)

Get all nodes latched to a gateway.

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
    api_instance = fingoti.DeviceApi(api_client)
    id = 'id_example' # str | Device ID to query.

    try:
        # Get all nodes latched to a gateway.
        api_response = api_instance.get_device_id_nodes(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_id_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID to query. | 

### Return type

[**DeviceNodesResponse**](DeviceNodesResponse.md)

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

# **patch_device_id**
> Default patch_device_id(id, patch_gateway=patch_gateway)

Update your Fingoti device.

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
    api_instance = fingoti.DeviceApi(api_client)
    id = 'id_example' # str | 
patch_gateway = fingoti.PatchGateway() # PatchGateway |  (optional)

    try:
        # Update your Fingoti device.
        api_response = api_instance.patch_device_id(id, patch_gateway=patch_gateway)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->patch_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_gateway** | [**PatchGateway**](PatchGateway.md)|  | [optional] 

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device**
> ClaimResult post_device(claim_request=claim_request)

Claim a new Fingoti device.

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
    api_instance = fingoti.DeviceApi(api_client)
    claim_request = fingoti.ClaimRequest() # ClaimRequest | The claim object. (optional)

    try:
        # Claim a new Fingoti device.
        api_response = api_instance.post_device(claim_request=claim_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->post_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claim_request** | [**ClaimRequest**](ClaimRequest.md)| The claim object. | [optional] 

### Return type

[**ClaimResult**](ClaimResult.md)

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

# **post_device_sendrequest**
> MqttDeviceResponse post_device_sendrequest(device_request=device_request)

Send a request to a Fingoti device.

The payload object varies depending on the property used, please refer to our protocol documentation <a href=\"https://help.fingoti.com\">here</a> for more infomation. <br />   Multiple objects can be sent in the request array and will be executed in order.

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
    api_instance = fingoti.DeviceApi(api_client)
    device_request = fingoti.DeviceRequest() # DeviceRequest | The command object. (optional)

    try:
        # Send a request to a Fingoti device.
        api_response = api_instance.post_device_sendrequest(device_request=device_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->post_device_sendrequest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_request** | [**DeviceRequest**](DeviceRequest.md)| The command object. | [optional] 

### Return type

[**MqttDeviceResponse**](MqttDeviceResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device_update**
> MqttDeviceResponse post_device_update(update_request=update_request)

Initiate a device update.

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
    api_instance = fingoti.DeviceApi(api_client)
    update_request = fingoti.UpdateRequest() # UpdateRequest |  (optional)

    try:
        # Initiate a device update.
        api_response = api_instance.post_device_update(update_request=update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->post_device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_request** | [**UpdateRequest**](UpdateRequest.md)|  | [optional] 

### Return type

[**MqttDeviceResponse**](MqttDeviceResponse.md)

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

