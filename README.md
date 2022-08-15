# Task 1 Software configuration

Subtask 1: "Why did I choose to participate in the challenge portfolio?”

Hello! My name is Olha and I am really  grateful to be a participant in the program Dare IT «Portfolio Challenge». 
Undoubtedly, the IT sphere is developing every day and every minute. To keep up with that immense pace, I consider it essential to be in a state of constant learning and self-improvement. My passion for learning and studying complements the trends of the modern world and the values of this project. My goal is not only to successfully reach the final of the project «Portfolio Challenge», but also to pick up every piece of knowledge I am offered. I want to obtain the possibility to work in a company and to get experience in the area I chose.  I expect that this project will help me find the learning vector so I can proceed with learning on my own later.


TASK 2: selectors

1. Scouts Panel_hyperlink_xpath
//*[@id='__next']/form/div/div[1]/h5
//*[contains(@class, "MuiTypography-root MuiTypography")]
//*[text()='Scouts Panel']
//child::div/h5

2. Login_hyperlink_xpath
//*[@id="login"]
//*[contains(@class, "MuiInputBase-input MuiInput-input")]     - not unique
//*[@id='__next']/form/div/div/div/div/input - not unique
//child::div/input  - not unique

3.  Password_hyperlink_xpath
//*[@id='password']//*[contains(@class, "MuiInputBase-input MuiInput-input")]  - not unique
//*[@id='__next']/form/div/div/div/div/input  - not unique
//child::div/input   - not unique

4. Remind_password_hyperlink_xpath
//*[@id='__next']/form/div/div[1]/a
//*[text()='Remind password']
//child::div/a

5. English_hyperlink_xpath
//*[@id='__next']/form/div/div[2]/div
//*[text()='English]
//*[contains(@class, "MuiInputBase-input MuiInput-input")]  - not unique

6. Polski_hyperlink_xpath
//*[@id='__next']/form/div/div[2]/div/div
//*[text()='Polski']
//child::div/input  - not unique

7. Sign in_hyperlink_xpath
//*[@id='__next']/form/div/div[2]/button/span[1]
//*[text()='Sign in']
//child::div/button/span
