package risk;

public class PredictiveServiceConfiguration {

	private String url = null;
	
	public PredictiveServiceConfiguration()  {
		
	}
	
	public PredictiveServiceConfiguration(String url)  {
		setUrl(url);
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}
}
