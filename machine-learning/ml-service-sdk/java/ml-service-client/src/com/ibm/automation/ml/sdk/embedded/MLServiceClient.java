package com.ibm.automation.ml.sdk.embedded;

import java.util.HashMap;

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.api.AutomationApiV10PredictionAdminApi;
import org.openapitools.client.api.AutomationApiV10PredictionInvocationApi;
import org.openapitools.client.model.ModelDescriptor;
import org.openapitools.client.model.ModelKeyDescriptor;
import org.openapitools.client.model.ModelSchema;
import org.openapitools.client.model.ModelSignature;
import org.openapitools.client.model.PredictionRequest;
import org.openapitools.client.model.PredictionResponse;

import com.google.gson.internal.LinkedTreeMap;

public class MLServiceClient {

	private String basepath;
	private ApiClient defaultClient = Configuration.getDefaultApiClient();

	public MLServiceClient(String basePath) {

		this.basepath = basePath;
		defaultClient.setBasePath(basePath); // defaultClient.setBasePath("http://localhost:5000");
	}

	public String getHeartBeat() {

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
		return "toto";

	}

	public ModelSchema getModelSchema(ModelKeyDescriptor modelKeyDescriptor) {

		AutomationApiV10PredictionAdminApi apiInstance = new AutomationApiV10PredictionAdminApi(defaultClient);

		ModelSchema modelSchema = null;

		try {
			modelSchema = apiInstance.postModelSchema(modelKeyDescriptor);
		} catch (ApiException e) {
			System.err.println("Exception when calling AutomationApiV10PredictionAdminApi#getHeartBeat");
			System.err.println("Status code: " + e.getCode());
			System.err.println("Reason: " + e.getResponseBody());
			System.err.println("Response headers: " + e.getResponseHeaders());
			e.printStackTrace();
		}

		return modelSchema;
	}

	public PredictionResponse getPrediction(PredictionRequest predictionRequest) {

		PredictionResponse predictionResponse = null;

		try {

			AutomationApiV10PredictionInvocationApi predictApiInstance = new AutomationApiV10PredictionInvocationApi(
					defaultClient);

			predictionResponse = predictApiInstance.postPredictionService(predictionRequest);
			

		} catch (ApiException e) {
			System.err.println("Exception when calling AutomationApiV10PredictionAdminApi#getHeartBeat");
			System.err.println("Status code: " + e.getCode());
			System.err.println("Reason: " + e.getResponseBody());
			System.err.println("Response headers: " + e.getResponseHeaders());
			e.printStackTrace();
		}
		return predictionResponse;

	}

	public static void main(String[] args) {

		MLServiceClient mlServiceClient = new MLServiceClient("http://localhost:5000");

		// Heartbeat
		// 
		mlServiceClient.getHeartBeat();

		testIrisClassification(mlServiceClient);
		testLoanDefautScoring(mlServiceClient);

	}
	
	public static void testIrisClassification(MLServiceClient mlServiceClient) {

		// ModelSchema
		//
		ModelKeyDescriptor modelKeyDescriptor = new ModelKeyDescriptor();
		modelKeyDescriptor.setName("iris-svc");
		modelKeyDescriptor.setVersion("1.0");
		modelKeyDescriptor.setFormat("joblib");
		
		ModelSchema modelSchema = mlServiceClient.getModelSchema(modelKeyDescriptor);
		System.out.println(modelSchema);
		
		ModelSignature modelSignature = modelSchema.getSignature();
		//Cast as the backend framework does not support models with list of nested types
		LinkedTreeMap input0 = (LinkedTreeMap) modelSignature.getInput().get(0);
		String parameterName = (String) input0.get("name");
		
		//Prediction
		//
		PredictionRequest predictionRequest = new PredictionRequest();
		
		ModelDescriptor modelDescriptor = new ModelDescriptor();
		modelDescriptor.setName("iris-svc");
		modelDescriptor.setVersion("1.0");
		modelDescriptor.setFormat("joblib");
		predictionRequest.setModel(modelDescriptor);
		
		HashMap<String, String> featureMap = new HashMap<String, String>();
		featureMap.put("sepal length", "5.1");
		featureMap.put("sepal width", "3.5");
		featureMap.put("petal length", "1.4");
		featureMap.put("petal width", "0.2");
		
		predictionRequest.setFeatures(featureMap);
		
		PredictionResponse predictionResponse = mlServiceClient.getPrediction(predictionRequest);
		System.out.println(predictionResponse);

	}
	
	public static void testLoanDefautScoring(MLServiceClient mlServiceClient) {

		// ModelSchema
		//
		ModelKeyDescriptor modelKeyDescriptor = new ModelKeyDescriptor();
		modelKeyDescriptor.setName("miniloandefault-rfc");
		modelKeyDescriptor.setVersion("1.0");
		modelKeyDescriptor.setFormat("joblib");
		
		ModelSchema modelSchema = mlServiceClient.getModelSchema(modelKeyDescriptor);
		System.out.println(modelSchema);
		
		ModelSignature modelSignature = modelSchema.getSignature();
		//Cast as the backend framework does not support models with list of nested types
		LinkedTreeMap input0 = (LinkedTreeMap) modelSignature.getInput().get(0);
		String parameterName = (String) input0.get("name");
		
		//Prediction
		//
		PredictionRequest predictionRequest = new PredictionRequest();
		
		ModelDescriptor modelDescriptor = new ModelDescriptor();
		modelDescriptor.setName("miniloandefault-rfc");
		modelDescriptor.setVersion("1.0");
		modelDescriptor.setFormat("joblib");
		predictionRequest.setModel(modelDescriptor);
		
		HashMap<String, String> featureMap = new HashMap<String, String>();
		featureMap.put("creditScore", "100");
		featureMap.put("income", "1000");
		featureMap.put("loanAmount", "1000000");
		featureMap.put("monthDuration", "120");
		featureMap.put("rate", "0.08");
		featureMap.put("yearlyReimbursement", "1000");
		
		predictionRequest.setFeatures(featureMap);
		
		PredictionResponse predictionResponse = mlServiceClient.getPrediction(predictionRequest);
		System.out.println(predictionResponse);

	}
}
