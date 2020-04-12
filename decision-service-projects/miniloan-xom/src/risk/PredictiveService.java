package risk;

import java.util.HashMap;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.openapitools.client.model.ModelDescriptor;
import org.openapitools.client.model.ModelKeyDescriptor;
import org.openapitools.client.model.ModelSchema;
import org.openapitools.client.model.ModelSignature;
import org.openapitools.client.model.PredictionRequest;
import org.openapitools.client.model.PredictionResponse;

import com.google.gson.internal.LinkedTreeMap;
import com.ibm.automation.ml.sdk.embedded.MLServiceClient;

import ilog.rules.bom.annotations.*;

import miniloan.Borrower;
import miniloan.Loan;

/**
 * This class models a predictive service.
 *
 */
public class PredictiveService {
	
	/**
	 * @return The risk score of having a repayment default for the application
	 */
	public static double GetRepaymentDefaultRiskScore(Borrower borrower, Loan loan) {

		//Constant to be moved
		MLServiceClient mlServiceClient = new MLServiceClient("http://localhost:5000");
		
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
		//borrower
		featureMap.put("creditScore", String.valueOf(borrower.getCreditScore()));
		featureMap.put("income", String.valueOf(borrower.getYearlyIncome()));
		//loan
		featureMap.put("loanAmount", String.valueOf(loan.getAmount()));
		featureMap.put("monthDuration", String.valueOf(loan.getDuration()));
		featureMap.put("rate", String.valueOf(loan.getYearlyInterestRate()));
		featureMap.put("yearlyReimbursement", String.valueOf(loan.getYearlyRepayment()));
			
		predictionRequest.setFeatures(featureMap);
			
		PredictionResponse predictionResponse = mlServiceClient.getPrediction(predictionRequest);
		System.out.println(predictionResponse);

		String strValue = predictionResponse.getProbabilities().get("1");
		return Double.parseDouble(strValue);
	}
}
