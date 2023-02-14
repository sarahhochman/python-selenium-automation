# Amazon Logo
driver.find_element(By.CSS_SELECTOR, "i[role='img'][aria-label='Amazon']")

# email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

#need help link
driver.find_element(By.CSS_SELECTOR ".a-expander-prompt")

#Forgot your password link, this would need a comment to explain as the id does not
driver.find_element(By.CSS_SELECTOR, "#auth-fpp-link-bottom")

#other issues with sign in link
driver.find_element(By.CSS_SELECTOR, "#ap-other-signin-issues-link")

#create amazon account
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit")

#conditions of use link
driver.find_element(By.CSS_SELECTOR, "a*[href='condition_of_use']")

#privacy notice link
driver.find_element(By.CSS_SELECTOR, "a*[href='notification_privacy_notice']")
