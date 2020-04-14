# MiniLoan Decision Service project with ML

This project is a variation of the sample project coming with IBM ODM.

Decision services coming with IBM Digital Business Automation are able to consume predictions served my the dynamic ML micro service. To do so the IBM Operational Decision Manager project needs to:
- use the micro ML service sdk in its Java eXecutable Object Model,
- surface the prediction call to estimate a risk or opportunity captured through a machine learning model in its Business Object Model
- have one or more rules that calls one of predictions through a near natural language statement verbalized in English or any other suppported locale.

<img src="../docs/images/miniloan-with-ml-rule-explorer.png" alt="Decision Service project in the Rule Explorer" width="200" height="600">

![Decision Service project in the Rule Explorer](../docs/images/miniloan-with-ml-rule-explorer.png "The extended miniloan project in the Rule Explorer")

![Ruleflow calling the prediction](../docs/images/miniloan-with-ml-ruleflow.png "A ruleflow with a task that cares about the ML estimated risk management")

![Rule calling the prediction](../docs/images/rule-with-ml.png "A rule calling a prediction of a repayment loan default")
 
The decision service projects folder includes a miniloan project that leverages business rules the micro ml sdk to automate the processing of loan applications.

The ready to use assets are:
- the RuleApp archive. This archive contains all you need to execute the rules and delegate a remote call to the micro ML service.
- The Decision Service project. It is the set of files as you can have it on your file system to import an Eclipse project for Rule Designer 8.10.3 or later.
