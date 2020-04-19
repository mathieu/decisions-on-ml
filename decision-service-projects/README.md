# Decision Service projects with ML

Decision services coming with IBM Digital Business Automation are able to consume predictions served my the dynamic ML micro service. To do so the IBM Operational Decision Manager project needs to:
- use the micro ML service sdk in its Java eXecutable Object Model,
- surface the prediction call to estimate a risk or opportunity captured through a machine learning model in its Business Object Model
- have one or more rules that calls one of predictions through a near natural language statement verbalized in English or any other suppported locale.


 ![Flow](../docs/images/decision-service-with-ml-stacks.png "Decision Service with ML microservice stacks")


The decision service projects folder includes a ![miniloan with ml](./miniloan-with-ml-README.md "miniloan with ml") project that leverages business rules the micro ml sdk to automate the processing of loan applications.

The ready to use assets are:
- the RuleApp archive. This archive contains all you need to execute the rules and delegate a remote call to the micro ML service.
- The Decision Service project. It is the set of files as you can have it on your file system to import an Eclipse project for Rule Designer 8.10.3 or later.
