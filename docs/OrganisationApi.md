# fingoti.OrganisationApi

All URIs are relative to *https://api.fingoti.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organisation_addresses_id**](OrganisationApi.md#delete_organisation_addresses_id) | **DELETE** /v1/organisation/addresses/{id} | Delete an address. This is not recoverable.
[**delete_organisation_presets_id**](OrganisationApi.md#delete_organisation_presets_id) | **DELETE** /v1/organisation/presets/{id} | Delete specified preset.
[**delete_organisation_roles_id**](OrganisationApi.md#delete_organisation_roles_id) | **DELETE** /v1/organisation/roles/{id} | Delete a role. Role must not be assigned to any users. This is not recoverable.
[**delete_organisation_tokens_id**](OrganisationApi.md#delete_organisation_tokens_id) | **DELETE** /v1/organisation/tokens/{id} | Delete a Token. Token will no longer authenticate API requests. This is not recoverable.
[**delete_organisation_users_id**](OrganisationApi.md#delete_organisation_users_id) | **DELETE** /v1/organisation/users/{id} | Remove a user from the organisation.
[**get_organisation**](OrganisationApi.md#get_organisation) | **GET** /v1/organisation | Get your Fingoti organisaiton information.
[**get_organisation_addresses**](OrganisationApi.md#get_organisation_addresses) | **GET** /v1/organisation/addresses | Get all addresses.
[**get_organisation_addresses_id**](OrganisationApi.md#get_organisation_addresses_id) | **GET** /v1/organisation/addresses/{id} | Get specified address.
[**get_organisation_partner**](OrganisationApi.md#get_organisation_partner) | **GET** /v1/organisation/partner | Get partner information.
[**get_organisation_presets**](OrganisationApi.md#get_organisation_presets) | **GET** /v1/organisation/presets | Get all presets.
[**get_organisation_presets_id**](OrganisationApi.md#get_organisation_presets_id) | **GET** /v1/organisation/presets/{id} | Get specified preset.
[**get_organisation_roles**](OrganisationApi.md#get_organisation_roles) | **GET** /v1/organisation/roles | Get all roles.
[**get_organisation_roles_id**](OrganisationApi.md#get_organisation_roles_id) | **GET** /v1/organisation/roles/{id} | Get specified role.
[**get_organisation_tenants**](OrganisationApi.md#get_organisation_tenants) | **GET** /v1/organisation/tenants | Get all tenants.
[**get_organisation_tokens**](OrganisationApi.md#get_organisation_tokens) | **GET** /v1/organisation/tokens | Get all API tokens.
[**get_organisation_tokens_id**](OrganisationApi.md#get_organisation_tokens_id) | **GET** /v1/organisation/tokens/{id} | Get specified token.
[**get_organisation_users**](OrganisationApi.md#get_organisation_users) | **GET** /v1/organisation/users | Get all users.
[**get_organisation_users_id**](OrganisationApi.md#get_organisation_users_id) | **GET** /v1/organisation/users/{id} | Get specidfied user.
[**patch_organisation**](OrganisationApi.md#patch_organisation) | **PATCH** /v1/organisation | Update your Fingoti organisation.
[**patch_organisation_addresses_id**](OrganisationApi.md#patch_organisation_addresses_id) | **PATCH** /v1/organisation/addresses/{id} | Update organisation address.
[**patch_organisation_presets_id**](OrganisationApi.md#patch_organisation_presets_id) | **PATCH** /v1/organisation/presets/{id} | Update organisation preset.
[**patch_organisation_roles_id**](OrganisationApi.md#patch_organisation_roles_id) | **PATCH** /v1/organisation/roles/{id} | Update organisation role.
[**patch_organisation_tokens_id**](OrganisationApi.md#patch_organisation_tokens_id) | **PATCH** /v1/organisation/tokens/{id} | Update API token.
[**patch_organisation_users_id**](OrganisationApi.md#patch_organisation_users_id) | **PATCH** /v1/organisation/users/{id} | Update organisation user.
[**post_organisation**](OrganisationApi.md#post_organisation) | **POST** /v1/organisation | Register a new Fingoti organisation.
[**post_organisation_addresses**](OrganisationApi.md#post_organisation_addresses) | **POST** /v1/organisation/addresses | Create a new address.
[**post_organisation_presets**](OrganisationApi.md#post_organisation_presets) | **POST** /v1/organisation/presets | Create a new preset.
[**post_organisation_roles**](OrganisationApi.md#post_organisation_roles) | **POST** /v1/organisation/roles | Create a new role.
[**post_organisation_tenants**](OrganisationApi.md#post_organisation_tenants) | **POST** /v1/organisation/tenants | Create new tenant. This is only available to partner organisations.
[**post_organisation_tokens**](OrganisationApi.md#post_organisation_tokens) | **POST** /v1/organisation/tokens | Generate new API token.
[**post_organisation_users**](OrganisationApi.md#post_organisation_users) | **POST** /v1/organisation/users | Invite a new user to the organisation.


# **delete_organisation_addresses_id**
> Default delete_organisation_addresses_id(id)

Delete an address. This is not recoverable.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an address. This is not recoverable.
        api_response = api_instance.delete_organisation_addresses_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->delete_organisation_addresses_id: %s\n" % e)
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

# **delete_organisation_presets_id**
> Default delete_organisation_presets_id(id)

Delete specified preset.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete specified preset.
        api_response = api_instance.delete_organisation_presets_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->delete_organisation_presets_id: %s\n" % e)
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

# **delete_organisation_roles_id**
> Default delete_organisation_roles_id(id)

Delete a role. Role must not be assigned to any users. This is not recoverable.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | Role ID to delete

    try:
        # Delete a role. Role must not be assigned to any users. This is not recoverable.
        api_response = api_instance.delete_organisation_roles_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->delete_organisation_roles_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Role ID to delete | 

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

# **delete_organisation_tokens_id**
> Default delete_organisation_tokens_id(id)

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a Token. Token will no longer authenticate API requests. This is not recoverable.
        api_response = api_instance.delete_organisation_tokens_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->delete_organisation_tokens_id: %s\n" % e)
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

# **delete_organisation_users_id**
> Default delete_organisation_users_id(id)

Remove a user from the organisation.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Remove a user from the organisation.
        api_response = api_instance.delete_organisation_users_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->delete_organisation_users_id: %s\n" % e)
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

# **get_organisation**
> OrganisationResponse get_organisation()

Get your Fingoti organisaiton information.

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
    api_instance = fingoti.OrganisationApi(api_client)
    
    try:
        # Get your Fingoti organisaiton information.
        api_response = api_instance.get_organisation()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganisationResponse**](OrganisationResponse.md)

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

# **get_organisation_addresses**
> OrganisationAddressResponse get_organisation_addresses(page_number=page_number, items_per_page=items_per_page, address=address, postcode=postcode)

Get all addresses.

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
    api_instance = fingoti.OrganisationApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
address = 'address_example' # str |  (optional)
postcode = 'postcode_example' # str |  (optional)

    try:
        # Get all addresses.
        api_response = api_instance.get_organisation_addresses(page_number=page_number, items_per_page=items_per_page, address=address, postcode=postcode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **address** | **str**|  | [optional] 
 **postcode** | **str**|  | [optional] 

### Return type

[**OrganisationAddressResponse**](OrganisationAddressResponse.md)

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

# **get_organisation_addresses_id**
> OrganisationAddressResponse get_organisation_addresses_id(id)

Get specified address.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get specified address.
        api_response = api_instance.get_organisation_addresses_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_addresses_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrganisationAddressResponse**](OrganisationAddressResponse.md)

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

# **get_organisation_partner**
> OrganisationPartnerResponse get_organisation_partner()

Get partner information.

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
    api_instance = fingoti.OrganisationApi(api_client)
    
    try:
        # Get partner information.
        api_response = api_instance.get_organisation_partner()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_partner: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganisationPartnerResponse**](OrganisationPartnerResponse.md)

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

# **get_organisation_presets**
> OrganisationPresetResponse get_organisation_presets(page_number=page_number, items_per_page=items_per_page, preset_number=preset_number, preset_name=preset_name)

Get all presets.

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
    api_instance = fingoti.OrganisationApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
preset_number = 'preset_number_example' # str |  (optional)
preset_name = 'preset_name_example' # str |  (optional)

    try:
        # Get all presets.
        api_response = api_instance.get_organisation_presets(page_number=page_number, items_per_page=items_per_page, preset_number=preset_number, preset_name=preset_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_presets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **preset_number** | **str**|  | [optional] 
 **preset_name** | **str**|  | [optional] 

### Return type

[**OrganisationPresetResponse**](OrganisationPresetResponse.md)

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

# **get_organisation_presets_id**
> OrganisationPresetResponse get_organisation_presets_id(id)

Get specified preset.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get specified preset.
        api_response = api_instance.get_organisation_presets_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_presets_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrganisationPresetResponse**](OrganisationPresetResponse.md)

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

# **get_organisation_roles**
> OrganisationRoleResponse get_organisation_roles(page_number=page_number, items_per_page=items_per_page, role_name=role_name)

Get all roles.

0 = None, 1 = Read, 2 = Write

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
    api_instance = fingoti.OrganisationApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
role_name = 'role_name_example' # str |  (optional)

    try:
        # Get all roles.
        api_response = api_instance.get_organisation_roles(page_number=page_number, items_per_page=items_per_page, role_name=role_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **role_name** | **str**|  | [optional] 

### Return type

[**OrganisationRoleResponse**](OrganisationRoleResponse.md)

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

# **get_organisation_roles_id**
> OrganisationRoleResponse get_organisation_roles_id(id)

Get specified role.

0 = None, 1 = Read, 2 = Write

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | Role ID to get

    try:
        # Get specified role.
        api_response = api_instance.get_organisation_roles_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_roles_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Role ID to get | 

### Return type

[**OrganisationRoleResponse**](OrganisationRoleResponse.md)

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

# **get_organisation_tenants**
> OrganisationTenantsResponse get_organisation_tenants(page_number=page_number, items_per_page=items_per_page, organisation_number=organisation_number, organisation_name=organisation_name)

Get all tenants.

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
    api_instance = fingoti.OrganisationApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
organisation_number = 'organisation_number_example' # str |  (optional)
organisation_name = 'organisation_name_example' # str |  (optional)

    try:
        # Get all tenants.
        api_response = api_instance.get_organisation_tenants(page_number=page_number, items_per_page=items_per_page, organisation_number=organisation_number, organisation_name=organisation_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **organisation_number** | **str**|  | [optional] 
 **organisation_name** | **str**|  | [optional] 

### Return type

[**OrganisationTenantsResponse**](OrganisationTenantsResponse.md)

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

# **get_organisation_tokens**
> UserTokenResponse get_organisation_tokens(page_number=page_number, items_per_page=items_per_page, token_name=token_name)

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
    api_instance = fingoti.OrganisationApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
token_name = 'token_name_example' # str |  (optional)

    try:
        # Get all API tokens.
        api_response = api_instance.get_organisation_tokens(page_number=page_number, items_per_page=items_per_page, token_name=token_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_tokens: %s\n" % e)
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

# **get_organisation_tokens_id**
> UserTokenResponse get_organisation_tokens_id(id)

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get specified token.
        api_response = api_instance.get_organisation_tokens_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_tokens_id: %s\n" % e)
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

# **get_organisation_users**
> OrganisationUserResponse get_organisation_users(page_number=page_number, items_per_page=items_per_page, name=name, email=email)

Get all users.

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
    api_instance = fingoti.OrganisationApi(api_client)
    page_number = 56 # int |  (optional)
items_per_page = 56 # int |  (optional)
name = 'name_example' # str |  (optional)
email = 'email_example' # str |  (optional)

    try:
        # Get all users.
        api_response = api_instance.get_organisation_users(page_number=page_number, items_per_page=items_per_page, name=name, email=email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] 
 **name** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 

### Return type

[**OrganisationUserResponse**](OrganisationUserResponse.md)

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

# **get_organisation_users_id**
> OrganisationUserResponse get_organisation_users_id(id)

Get specidfied user.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get specidfied user.
        api_response = api_instance.get_organisation_users_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_users_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrganisationUserResponse**](OrganisationUserResponse.md)

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

# **patch_organisation**
> Default patch_organisation(patch_organisation_request=patch_organisation_request)

Update your Fingoti organisation.

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
    api_instance = fingoti.OrganisationApi(api_client)
    patch_organisation_request = fingoti.PatchOrganisationRequest() # PatchOrganisationRequest |  (optional)

    try:
        # Update your Fingoti organisation.
        api_response = api_instance.patch_organisation(patch_organisation_request=patch_organisation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->patch_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_organisation_request** | [**PatchOrganisationRequest**](PatchOrganisationRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_organisation_addresses_id**
> Default patch_organisation_addresses_id(id, patch_address_request=patch_address_request)

Update organisation address.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 
patch_address_request = fingoti.PatchAddressRequest() # PatchAddressRequest |  (optional)

    try:
        # Update organisation address.
        api_response = api_instance.patch_organisation_addresses_id(id, patch_address_request=patch_address_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->patch_organisation_addresses_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_address_request** | [**PatchAddressRequest**](PatchAddressRequest.md)|  | [optional] 

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

# **patch_organisation_presets_id**
> Default patch_organisation_presets_id(id, patch_preset_request=patch_preset_request)

Update organisation preset.

Fields that do not require updating can be omitted.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 
patch_preset_request = fingoti.PatchPresetRequest() # PatchPresetRequest |  (optional)

    try:
        # Update organisation preset.
        api_response = api_instance.patch_organisation_presets_id(id, patch_preset_request=patch_preset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->patch_organisation_presets_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_preset_request** | [**PatchPresetRequest**](PatchPresetRequest.md)|  | [optional] 

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

# **patch_organisation_roles_id**
> Default patch_organisation_roles_id(id, patch_role_request=patch_role_request)

Update organisation role.

Fields that do not require updating can be omitted. 0 = None, 1 = Read, 2 = Write

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | Role ID to update
patch_role_request = fingoti.PatchRoleRequest() # PatchRoleRequest |  (optional)

    try:
        # Update organisation role.
        api_response = api_instance.patch_organisation_roles_id(id, patch_role_request=patch_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->patch_organisation_roles_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Role ID to update | 
 **patch_role_request** | [**PatchRoleRequest**](PatchRoleRequest.md)|  | [optional] 

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

# **patch_organisation_tokens_id**
> Default patch_organisation_tokens_id(id, patch_organisation_token_request=patch_organisation_token_request)

Update API token.

Fields that do not require updating can be omitted. AssignedUsers array must contain all users that are to be assigned to the token

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 
patch_organisation_token_request = fingoti.PatchOrganisationTokenRequest() # PatchOrganisationTokenRequest |  (optional)

    try:
        # Update API token.
        api_response = api_instance.patch_organisation_tokens_id(id, patch_organisation_token_request=patch_organisation_token_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->patch_organisation_tokens_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patch_organisation_token_request** | [**PatchOrganisationTokenRequest**](PatchOrganisationTokenRequest.md)|  | [optional] 

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

# **patch_organisation_users_id**
> Default patch_organisation_users_id(id, update_user_role=update_user_role)

Update organisation user.

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
    api_instance = fingoti.OrganisationApi(api_client)
    id = 'id_example' # str | 
update_user_role = fingoti.UpdateUserRole() # UpdateUserRole |  (optional)

    try:
        # Update organisation user.
        api_response = api_instance.patch_organisation_users_id(id, update_user_role=update_user_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->patch_organisation_users_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_user_role** | [**UpdateUserRole**](UpdateUserRole.md)|  | [optional] 

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

# **post_organisation**
> Default post_organisation(regiser_organisation_dto=regiser_organisation_dto)

Register a new Fingoti organisation.

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
    api_instance = fingoti.OrganisationApi(api_client)
    regiser_organisation_dto = fingoti.RegiserOrganisationDto() # RegiserOrganisationDto |  (optional)

    try:
        # Register a new Fingoti organisation.
        api_response = api_instance.post_organisation(regiser_organisation_dto=regiser_organisation_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regiser_organisation_dto** | [**RegiserOrganisationDto**](RegiserOrganisationDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organisation_addresses**
> Default post_organisation_addresses(add_address_request=add_address_request)

Create a new address.

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
    api_instance = fingoti.OrganisationApi(api_client)
    add_address_request = fingoti.AddAddressRequest() # AddAddressRequest |  (optional)

    try:
        # Create a new address.
        api_response = api_instance.post_organisation_addresses(add_address_request=add_address_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_address_request** | [**AddAddressRequest**](AddAddressRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organisation_presets**
> AddPresetResult post_organisation_presets(add_preset_request=add_preset_request)

Create a new preset.

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
    api_instance = fingoti.OrganisationApi(api_client)
    add_preset_request = fingoti.AddPresetRequest() # AddPresetRequest |  (optional)

    try:
        # Create a new preset.
        api_response = api_instance.post_organisation_presets(add_preset_request=add_preset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation_presets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_preset_request** | [**AddPresetRequest**](AddPresetRequest.md)|  | [optional] 

### Return type

[**AddPresetResult**](AddPresetResult.md)

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

# **post_organisation_roles**
> DefaultWithId post_organisation_roles(add_role_request=add_role_request)

Create a new role.

0 = None, 1 = Read, 2 = Write

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
    api_instance = fingoti.OrganisationApi(api_client)
    add_role_request = fingoti.AddRoleRequest() # AddRoleRequest |  (optional)

    try:
        # Create a new role.
        api_response = api_instance.post_organisation_roles(add_role_request=add_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_role_request** | [**AddRoleRequest**](AddRoleRequest.md)|  | [optional] 

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

# **post_organisation_tenants**
> RegisterOrganisationResult post_organisation_tenants(regiser_tenant_dto=regiser_tenant_dto)

Create new tenant. This is only available to partner organisations.

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
    api_instance = fingoti.OrganisationApi(api_client)
    regiser_tenant_dto = fingoti.RegiserTenantDto() # RegiserTenantDto |  (optional)

    try:
        # Create new tenant. This is only available to partner organisations.
        api_response = api_instance.post_organisation_tenants(regiser_tenant_dto=regiser_tenant_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regiser_tenant_dto** | [**RegiserTenantDto**](RegiserTenantDto.md)|  | [optional] 

### Return type

[**RegisterOrganisationResult**](RegisterOrganisationResult.md)

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

# **post_organisation_tokens**
> TokenSuccessResponse post_organisation_tokens(new_organisation_token_dto=new_organisation_token_dto)

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
    api_instance = fingoti.OrganisationApi(api_client)
    new_organisation_token_dto = fingoti.NewOrganisationTokenDto() # NewOrganisationTokenDto | User credentials. For a token to never expire, specify 0 for the expiry (optional)

    try:
        # Generate new API token.
        api_response = api_instance.post_organisation_tokens(new_organisation_token_dto=new_organisation_token_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_organisation_token_dto** | [**NewOrganisationTokenDto**](NewOrganisationTokenDto.md)| User credentials. For a token to never expire, specify 0 for the expiry | [optional] 

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

# **post_organisation_users**
> Default post_organisation_users(invite_user_dto=invite_user_dto)

Invite a new user to the organisation.

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
    api_instance = fingoti.OrganisationApi(api_client)
    invite_user_dto = fingoti.InviteUserDto() # InviteUserDto |  (optional)

    try:
        # Invite a new user to the organisation.
        api_response = api_instance.post_organisation_users(invite_user_dto=invite_user_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganisationApi->post_organisation_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_dto** | [**InviteUserDto**](InviteUserDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

