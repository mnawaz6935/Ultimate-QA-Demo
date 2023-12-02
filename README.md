## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.

Page Object Model is followed in this framework

**Elements** folder contains all the xpaths of all the elements elements

**pages** folder contains methods for corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**drivers** directory contains the chrome and firefox driver for mac

**requirements.txt** file contains all the python packages needed to run this framework

**allure** directory contains the files generated with allure reports

### Test Configuration
**Constants > TestConfig.py** file have test configuration which are need to be adjusted before execution.

**email** requires a valid/signed-up user email address

**password** requires a valid/signed-up user password against the above email address
### **Commands to run the tests**

**To run the test with allure report**
```shell
behave -f allure_behave.formatter:AllureFormatter -o allure/allure-results ./features -D url=https://courses.ultimateqa.com/
```
**To run the test without allure report** 
```shell
behave ./features
```

**To run the test with allure report in parallel**
  ```shell
python ./behave_parallel.py "-D url=https://courses.ultimateqa.com/"
```
