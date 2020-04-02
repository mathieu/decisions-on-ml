package com.ibm.decision.ml;

import java.util.HashMap;

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.api.AutomationApiV10PredictionAdminApi;
import org.openapitools.client.api.AutomationApiV10PredictionGenericApi;
import org.openapitools.client.model.ModelDescriptor;
import org.openapitools.client.model.ModelKeyDescriptor;
import org.openapitools.client.model.ModelSchema;
import org.openapitools.client.model.PredictionRequest;
import org.openapitools.client.model.PredictionResponse;

public class MLServiceClient {

	public MLServiceClient() {

	}

	public static void main(String[] args) {
		ApiClient defaultClient = Configuration.getDefaultApiClient();
		defaultClient.setBasePath("http://localhost:5000");

		AutomationApiV10PredictionAdminApi apiInstance = new AutomationApiV10PredictionAdminApi(defaultClient);
		try {
			apiInstance.getHeartBeat();
			
			ModelKeyDescriptor modelKeyDescriptor = new ModelKeyDescriptor();
			modelKeyDescriptor.setName("iris-svc");
			modelKeyDescriptor.setVersion("1.0");
			modelKeyDescriptor.setFormat("joblib");
			
			ModelSchema modelSchema = apiInstance.postModelSchema(modelKeyDescriptor);
			System.out.println(modelSchema);
			
			AutomationApiV10PredictionGenericApi predictApiInstance = new AutomationApiV10PredictionGenericApi(defaultClient);
			
			PredictionRequest predictionRequest = new PredictionRequest();
			
			ModelDescriptor modelDescriptor = new ModelDescriptor();
			modelDescriptor.setPath("iris-svc");
			modelDescriptor.setVersion("1.0");
			modelDescriptor.setFormat("joblib");
			
			predictionRequest.setModel(modelDescriptor);
			
			HashMap<String,String> featureMap = new HashMap<String,String>();
			featureMap.put("sepal length", "5.1");
			featureMap.put("sepal width", "3.5");
			featureMap.put("petal length", "1.4");
			featureMap.put("petal width", "0.2");
			
			predictionRequest.setFeatures(featureMap);
			
			PredictionResponse predictionResponse = predictApiInstance.postPredictionService(predictionRequest);
			System.out.println(predictionResponse);
			
		} catch (ApiException e) {
			System.err.println("Exception when calling AutomationApiV10PredictionAdminApi#getHeartBeat");
			System.err.println("Status code: " + e.getCode());
			System.err.println("Reason: " + e.getResponseBody());
			System.err.println("Response headers: " + e.getResponseHeaders());
			e.printStackTrace();
		}
	}
}
