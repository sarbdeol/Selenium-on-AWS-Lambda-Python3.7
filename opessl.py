import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_pdf(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as pdf_file:
        pdf_file.write(response.content)

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/path/to/save/directory",  # Replace with your desired download directory
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })
    
    # Set up Chrome driver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.louisianaworks.net/hire/vosnet/Default.aspx")

    element = driver.find_element(By.XPATH, "//a[@title='File Employee Separation Notice']")
    element.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains('EmployerSeparationNoticeRedirector'))

    # Rest of your form filling code here...

    input_accountNumber = driver.find_element(By.ID, "ctl00_Main_content_txtAccountNumber")
    input_accountNumber.send_keys('4401784')

    btnSearch = driver.find_element(By.ID, "ctl00_Main_content_btnSearch")
    btnSearch.click()

    wait = WebDriverWait(driver, 1000)
    wait.until(EC.url_contains('separationnoticeforguest'))


    input_address1 = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerAddress1")
    input_address1.send_keys('TEST')

    input_address2 = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerAddress2")
    input_address2.send_keys('')

    input_city = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerCity")
    input_city.send_keys('TEST')

    input_state = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_ddlEmployerState")
    input_state.send_keys('TEST')

    input_name = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtYourname")
    input_name.send_keys('TEST')

    input_zip = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerZip")
    input_zip.send_keys('70000')

    input_title = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerContactTitle")
    input_title.send_keys('HR Administrator')

    # input_phone = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtYourPhone")
    # input_phone.clear()
    # input_phone.send_keys('2253643062')
    script = "document.querySelector('#ctl00_Main_content_ucSeparationNoticeForm_txtYourPhone').value='123-123-1233';"
    driver.execute_script(script)

    input_email = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerContactEmail")
    input_email.send_keys('smartinez@employersupport.com')

    input_firstName = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeFirstName")
    input_firstName.send_keys('Test')

    input_lastName = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeLastName")
    input_lastName.send_keys('Test')

    input_SSN = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeSSN")
    input_SSN.send_keys('2222222222')

    input_DateOfSeparation = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeDateSeparation_dateInput")
    input_DateOfSeparation.send_keys('2023-07-20')

    input_DateOfHired = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeDateHired_dateInput")
    input_DateOfHired.send_keys('2023-03-10')

    input_DateLastWorked = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeDateLastWorked_dateInput")
    input_DateLastWorked.send_keys('2023-07-18')

    input_SeparationCategory = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_ddlSeparationCategory")
    input_SeparationCategory.send_keys('Terminated')

    input_SeparationReason = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtSeparationReasonExplain_txtComments")
    input_SeparationReason.send_keys('Termniated Reason')

    input_HourlyRateOfPay = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtHourlyRateOfPay")
    input_HourlyRateOfPay.send_keys('5.5000')

    input_HoursWorkedPerWeek = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtHoursWorkedPerWeek")
    input_HoursWorkedPerWeek.send_keys('10')

    btnSubmit = driver.find_element(By.ID, "ctl00_Main_content_btnSave")
    btnSubmit.click()

    # Find the PDF URL
    print_button = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_Main_content_lbPrint")))
    pdf_url = print_button.get_attribute("href")

    # Close the browser
    driver.quit()

    # Download the PDF file using requests
    download_pdf(pdf_url, "/path/to/save/directory/output.pdf")  # Replace with your desired save path

    print("PDF file downloaded successfully.")
























# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService

# def main(event, context):
#     options = Options()
#     options.binary_location = '/opt/headless-chromium'
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--single-process')
#     options.add_argument('--disable-dev-shm-usage')
    
#     options.add_experimental_option("prefs", {
#         "download.default_directory": "/tmp", # Store downloaded files in /tmp directory
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "plugins.always_open_pdf_externally": True
#     })

#     driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
    
    
#     # Go to the initial page
#     driver.get("https://www.louisianaworks.net/hire/vosnet/Default.aspx")


#     element = driver.find_element(By.XPATH, "//a[@title='File Employee Separation Notice']")
#     element.click()

#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.url_contains('EmployerSeparationNoticeRedirector'))


#     input_accountNumber = driver.find_element(By.ID, "ctl00_Main_content_txtAccountNumber")
#     input_accountNumber.send_keys('4401784')

#     btnSearch = driver.find_element(By.ID, "ctl00_Main_content_btnSearch")
#     btnSearch.click()
#     # Close the browser

#     wait = WebDriverWait(driver, 1000)
#     wait.until(EC.url_contains('separationnoticeforguest'))


#     input_address1 = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerAddress1")
#     input_address1.send_keys('TEST')

#     input_address2 = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerAddress2")
#     input_address2.send_keys('')

#     input_city = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerCity")
#     input_city.send_keys('TEST')

#     input_state = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_ddlEmployerState")
#     input_state.send_keys('TEST')

#     input_name = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtYourname")
#     input_name.send_keys('TEST')

#     input_zip = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerZip")
#     input_zip.send_keys('70000')

#     input_title = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerContactTitle")
#     input_title.send_keys('HR Administrator')

#     # input_phone = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtYourPhone")
#     # input_phone.clear()
#     # input_phone.send_keys('2253643062')
#     script = "document.querySelector('#ctl00_Main_content_ucSeparationNoticeForm_txtYourPhone').value='123-123-1233';"
#     driver.execute_script(script)

#     input_email = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployerContactEmail")
#     input_email.send_keys('smartinez@employersupport.com')

#     input_firstName = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeFirstName")
#     input_firstName.send_keys('Test')

#     input_lastName = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeLastName")
#     input_lastName.send_keys('Test')

#     input_SSN = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeSSN")
#     input_SSN.send_keys('2222222222')

#     input_DateOfSeparation = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeDateSeparation_dateInput")
#     input_DateOfSeparation.send_keys('2023-07-20')

#     input_DateOfHired = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeDateHired_dateInput")
#     input_DateOfHired.send_keys('2023-03-10')

#     input_DateLastWorked = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtEmployeeDateLastWorked_dateInput")
#     input_DateLastWorked.send_keys('2023-07-18')

#     input_SeparationCategory = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_ddlSeparationCategory")
#     input_SeparationCategory.send_keys('Terminated')

#     input_SeparationReason = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtSeparationReasonExplain_txtComments")
#     input_SeparationReason.send_keys('Termniated Reason')

#     input_HourlyRateOfPay = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtHourlyRateOfPay")
#     input_HourlyRateOfPay.send_keys('5.5000')

#     input_HoursWorkedPerWeek = driver.find_element(By.ID, "ctl00_Main_content_ucSeparationNoticeForm_txtHoursWorkedPerWeek")
#     input_HoursWorkedPerWeek.send_keys('10')


#     btnSubmit = driver.find_element(By.ID, "ctl00_Main_content_btnSave")
#     btnSubmit.click()
#     # Close the browser

#     print_button = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_Main_content_lbPrint")))

#     # Get the URL of the PDF
#     pdf_url = print_button.get_attribute("href")

#     print(pdf_url)


#     driver.get(pdf_url)
#     wait = WebDriverWait(driver, 20)
#     try:
#         element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > embed")))
#         print(element)
#         time.sleep(4)
#         response = {
#             "statusCode": 200,
#             "element": element
#         }


#     except:
#         print('not availabe')
#         pass
#     # Navigate to the PDF URL

#     # Close the browser
#     driver.quit()

    

#     return response