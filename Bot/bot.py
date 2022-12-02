from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=chow+chow+filhote+gordo&rlz=1C1GCEA_enBR983BR983&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizi5Pr8Nr7AhXXAjQIHZbAAGsQ_AUoAXoECAEQAw&biw=1745&bih=838&dpr=1.1#imgrc=G4SrwJo8aPxDhM")
img = driver.find_element("xpath",'//*[@id="Sva75c"]/div/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')
img.screenshot("chow.png")
driver.get("https://mail.google.com/mail/?tab=rm&ogbl")