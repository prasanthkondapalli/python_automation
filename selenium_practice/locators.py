from selenium.webdriver.common.by import By

#Mandatory Fields

FIRST_NAME = (By.XPATH,"//input[@name='fname']")
EMAIL_FIELD =(By.XPATH,"//input[@type='email']")
SUBJECT_FIELD =(By.XPATH,"(//input[@type='text'])[3]")

#Non Mandatory fields
LAST_NAME = (By.XPATH,"//input[@name='lname']")
MESSAGE_FIELD = (By.XPATH,"//textarea[@class='TC0a5swwrteZsfBY7ttl']")
NO_RESPONSE_REQUIRED_CHECKBOX =(By.XPATH,"(//fieldset[@id='checkbox-b5b9cc19-24e5-4c8c-960a-055837723942']/div/label/span)[1]")
RESPONSE_REQUIRED_CHECKBOX = (By.XPATH,"(//fieldset[@id='checkbox-b5b9cc19-24e5-4c8c-960a-055837723942']/div/label/span)[2]")

PRIVATE_SHOW_RADIO_BUTTON = (By.XPATH,"(//fieldset[@class='form-item field radio']/div/label/span[2])[1]")
PUBLIC_SHOW_RAIDO_BUTTON = (By.XPATH,"(//fieldset[@class='form-item field radio']/div/label/span[2])[2]")

SELECT_DROPDOWN = (By.XPATH,"//select[@id='select-e1f50715-c8a7-48eb-bc99-2c245676068c-field']")

SURVEY_RADIO_BUTTONS = (By.XPATH,"//fieldset[@class='item']/div")

SUBMIT_BUTTON  = (By.XPATH,"//button[@type='submit']")
