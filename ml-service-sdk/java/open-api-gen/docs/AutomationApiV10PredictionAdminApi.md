# AutomationApiV10PredictionAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHeartBeat**](AutomationApiV10PredictionAdminApi.md#getHeartBeat) | **GET** /automation/api/v1.0/prediction/admin/is-alive | Returns an heart beat
[**getModel**](AutomationApiV10PredictionAdminApi.md#getModel) | **GET** /automation/api/v1.0/prediction/admin/models | Returns the list of ML models
[**postModelSchema**](AutomationApiV10PredictionAdminApi.md#postModelSchema) | **POST** /automation/api/v1.0/prediction/admin/model-schema | Returns the schema of a model


<a name="getHeartBeat"></a>
# **getHeartBeat**
> getHeartBeat()

Returns an heart beat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationApiV10PredictionAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AutomationApiV10PredictionAdminApi apiInstance = new AutomationApiV10PredictionAdminApi(defaultClient);
    try {
      apiInstance.getHeartBeat();
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationApiV10PredictionAdminApi#getHeartBeat");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

<a name="getModel"></a>
# **getModel**
> getModel()

Returns the list of ML models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationApiV10PredictionAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AutomationApiV10PredictionAdminApi apiInstance = new AutomationApiV10PredictionAdminApi(defaultClient);
    try {
      apiInstance.getModel();
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationApiV10PredictionAdminApi#getModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

<a name="postModelSchema"></a>
# **postModelSchema**
> ModelSchema postModelSchema(payload)

Returns the schema of a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationApiV10PredictionAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AutomationApiV10PredictionAdminApi apiInstance = new AutomationApiV10PredictionAdminApi(defaultClient);
    ModelKeyDescriptor payload = new ModelKeyDescriptor(); // ModelKeyDescriptor | 
    try {
      ModelSchema result = apiInstance.postModelSchema(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationApiV10PredictionAdminApi#postModelSchema");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ModelKeyDescriptor**](ModelKeyDescriptor.md)|  |

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ML Schema retrieved. |  -  |

