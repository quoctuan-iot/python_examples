# Interview questions?
    
1. How to install, download webdriver?

2. How to load webdriver?

3. How to Send request to server?

4. Method to controll web? Some the common web driver command?

5. What is selenium?
    - open-source automated testing framework for validating web app. across multiple browser and 
    platforms.
    Components:
        - IDE, Selenium RC, Selenium Web driver, Selenium GRID

6. What is mean by selenium suite and what are its different components?
7. What is automation testing, and what are its advantages?
    - Automation testing or test automation 
    - Paralled execution 
    - It supports both the performance and functional testing.
    - Helps in testing a large scale matrix
    - save time, money

8. What are the advantages of using selenium as an automation tool?
    - open-source
    - Language assistance
    - Compatible with a variety of operating system
    - Regular updateds
    - Tests on varuety of deivices
    - Selenium suites wit a lot of content

9. Can selenium be used to launch web browsers?
    - Selenium provides good support to launch web browsers:
    Google chrome, Firefox, Explorer,etc.

30. What are the disadvantages of using Selenium as a testing tool?
    - Tests web only: Mobile app, captcha, barcode reader canoot be tested.
    - No build-in reporting and testing: Using third-party
    - Since Selenium is a open source, no dedicated support for user

10. What is meant by selenese? Explain different types of selenium commamds?
    - selenese is Language used for writin test scropts in Selenium IDE.
    - Actions: 
    - Accessors:
    - Assertions:

11. What is meant by a locator and name a few different types of locators present in selenium?
    - locator is address for uniquely identifying web elements.
    - ID, 
    - ClassName, 
    - Name , 
    - TangName, 
    - Linktest, 
    - PartialLinkTest, 
    - Xpath, 
    - CSS selector, 
    - DOM

12. State the major difference between "assert" and verify" commamds in selenium?
    - Assert: Stop executeion of the testing if condition is true, false is continue
    - Verify: Don't stop flow of execution, only verify the condition

13. What is meant by XPath in selenium. Explain XPath absolute and XPath relative?
    - XPath is a language used to query XML document.
    - A single slash '/' for creating an absolute,
    - A double slase '//' for creating a relative path.

14. In XPath, what is difference between "/" and "//"
    - Absolute: /html/body/div/div/form/input
    - Relative: //input[@id = 'emial']

15. What is the difference between the commands "type" and "typeAndWait" in the context of selenium?
    - type: used to enter keyboard key values into web app text box, combo box.
    - typeAndWait: used when finish typing and page begins to reload. If there is not page reload event on
    typing, then you have to use simple 'type' commnad.
    
16. Differentiale betwenn "findElement()" and "findElements()" in the context of selenium with proper example
    - findElement: Return the first web element that matches the locator.
                    Exception No such Element -> Produced.
    
    - findElements: Return list of all the web items that match the locator.
                    Empty list is returned.

17. In selenium, How will you wait until a web pae has been loaded completely?
    - There are two methods.
    - set an implicit wait: 
        temp = driver.Manage().Timeouts().ImplicitWait;
        On every page navigation or reload. this will try to wait until the page is fully loaded.
    
    - Call JavaScript return. 
        new WebDriverWait(firefoxDriver, pageLoadTimeout).until(
        webDriver -> ((JavascriptExecutor) webDriver).executeScript("return document.readyState").equals("complete"));
    
18. Explain the difference between driver.close() and driver.quit() command in selenium?
    - close(): close the curently active window. which the accessed by the web driver.
    - quit(): close all the windows opened by the program.

19. Explain the various navigation commands support ed by selenium?
    - 4 navigation commands:
        - navigate().back(): taking the user to te last webpage of the browser history
        - .forward(): next page
        - refresh(): refresh it
        - to(): navigate to particular URL, URL as a parameter.

20. Explain the same origin policy and how selenium handles its?
    - 

22. What do you understand about Jenkins? Why are the benifits of using it with selenium?
    - Jenkins is a jave application.
    - Is the most popular open-source 
    - To keep track of any job.
    - Specific event in an application occurs, ->It triggers actions.

    - test project in continuous integration using Maven
    - Execute at a predetermined time.
    - Execution history can be saved.
    
23. What do you understand about kroken links? How can you detect broken links in Selenium?
Explain properly with code?
    - Link are not reachable.
    - The 4xx class of status code: client-side errors,
    - the 5xx class is: response errors.


24. What is a basic step to crawl data from web browser?
    - Open web driver
    - Login ()
    - Search for information we want
    - Save information


# Session

    1. Simpile usage

from selenium import webdriver 
- Provide Webdriver as Firefox,...

from selenium.webdriver.common.keys import Keys
- Provide keys in the keyboard enter, return, F1,...

driver = webdriver.Firefox()
- Create instance

    2. Navigating to page

driver.get('url')

- This method will navigate to a page given by URL
- Need to ensure pages are fully loaded. Using 'waits'


    3. Interacting with the page.

        3.1 Find element within page
Examlple:      
<input type="text" name="passwd" id="passwd-id" />

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")

- If the's more than one element that matches query, only the first
will be returned. 
- If nothing can be found.  NoSuchElementException returned

        3.2 Enter text into a textbox

element.clear()
element.send_keys("some text")
    or
element.send_keys(" and some", Keys.ARROW_DOWN)

- Send keys and press arrow down

        Validate some existing text 
element.get_attribute("value")

        - Fetch text already in a text box.

        3.3 Check box
element.click()

        Validate check box is selected.
element.is_selected()
    or
element.get_attribute("checked")

- Checkbox is checked we would get a True value else we will get
    False

        How to deselect a checkbox only when it is selected
element.click()

        3.4 Radio button
Similar Checkbox.
element.click()

        Validate radio button is selected.
element.is_selected()
    or
element.get_attribute("checked")

        How to deselect a radio button only when it is selected
element.click()

        3.5 Link
element.click()

        Validate link 
element.get_attribute('href')

        3.6 Dropdown

Examlple:
<td>
    <select id="search_grade">
        <option selected>(no value)</option>
        <option value="K">K</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
    </select>
</td>

grade_dropdown = Select(driver.find_element_by_id("search_grade"))
grade_dropdown.select_by_value("5")

    We can deselect any selected value.
grade_dropdown.deselect_by_value("5")

        Validate dropdown 
.all_selected_options 

- Get the list of all the selected options.

.first_selected_option

- Rertun the first option that has been selected.

.options

- Get a list of all available options.

        3.7 Button.
element.click()

        3.8 Element not interactable exception.
- Example: We may not be able to click or send keys.
    - Not visible/ not displayed
    - off screen
    - behind
    - Some other action needs to be performed by the user first.

            3.8.1 Wait until clickable
1
time.sleep()

    Other way more efficient than.
2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

table = WebDriverWait(driver, seconds).until(EC.presence_of_element_located((By.ID, "resulttable")))

3
driver.implicitly_wait(seconds)

            3.8.2 Scroll untill on-screen
    
- scroll to a certain height
driver.execute_script("window.scrollTo(0, 5000)")

- scroll to the bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            --> Add into a DOM structure

            3.8.3 Execute JavaScript
-Example: error: 'element not interactable' Because form submission button is hidden.
driver.execute_script(f'document.getElementById("search").click();')

            3.8.4 Perform preliminary action.
from selenium.webdriver.common.action_chains import ActionChains
hov = ActionChains(driver).move_to_element(name_tag)
hov.perform()
    
    4. Scrape data.
        4.1 Scrape tables.

