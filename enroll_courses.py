from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import smtplib
import email
from config import Config
from sys import argv
import pause

driver = None
wait = None


# def repeatedly_try(function):
#     def wrapper(*args, **kwargs):
#         result = None
#         while True:
#             try:
#                 result = function(*args, **kwargs)
#                 break
#             except Exception as e:
#                 print(str(e))
#                 sleep(1)
#         return result
#     return wrapper


def send_email(unsuccessful_list):
    msg = email.message.EmailMessage()

    msg.set_content(Config.email_message % (", ".join(unsuccessful_list)))
    msg['Subject'] = Config.email_subject

    msg['From'] = Config.email_username
    msg['To'] = ", ".join(Config.recipients)

    server = smtplib.SMTP(Config.smtp_host, Config.smtp_port)
    server.starttls()
    server.login(Config.email_username, Config.email_password)
    server.send_message(msg)
    server.quit()


def initialize():
    global driver
    global wait
    options = webdriver.chrome.options.Options()
    options.add_argument(f"user-data-dir={Config.chrome_path}")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)


def login():
    url = 'https://pcsprod.princeton.edu/psc/pcsprod/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?PortalActualURL=https%3a%2f%2fpcsprod.princeton.edu%2fpsc%2fpcsprod%2fEMPLOYEE%2fSA%2fc%2fSA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL&amp;PortalContentURL=https%3a%2f%2fpcsprod.princeton.edu%2fpsc%2fpcsprod%2fEMPLOYEE%2fSA%2fc%2fSA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL&amp;PortalContentProvider=SA&amp;PortalCRefLabel=PU%20Enroll%20Cart&amp;PortalRegistryName=EMPLOYEE&amp;PortalServletURI=https%3a%2f%2fphubprod.princeton.edu%2fpsp%2fphubprod%2f&amp;PortalURI=https%3a%2f%2fphubprod.princeton.edu%2fpsc%2fphubprod%2f&amp;PortalHostNode=EMPL&amp;NoCrumbs=yes&amp;PortalKeyStruct=yes'
    driver.get(url)
    try:
        submit_button = wait.until(
            EC.element_to_be_clickable((By.NAME, 'submit')))
        submit_button.click()
    except:
        pass


# @repeatedly_try
def enroll():
    proceed_btn = wait.until(
        EC.element_to_be_clickable((By.ID, 'DERIVED_REGFRM1_LINK_ADD_ENRL$82$')))

    pause.until(Config.enroll_time)

    proceed_btn.click()

    finish_enrolling_btn = wait.until(
        EC.element_to_be_clickable((By.ID, 'DERIVED_REGFRM1_SSR_PB_SUBMIT')))
    finish_enrolling_btn.click()


def notify_failed_classes():
    unsuccessful_list = get_unsuccessful_classes()
    send_email(unsuccessful_list)


# @repeatedly_try
def get_unsuccessful_classes():
    rows = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//tr[starts-with(@id,"trSSR_SS_ERD_ER$0_row")]')))
    unsuccessful_list = []
    for row in rows:
        if 'Error' in row.text:
            class_name = row.text.split('\n')[0]
            unsuccessful_list.append(class_name)
    return unsuccessful_list


if __name__ == '__main__':
    initialize()
    login()
    enroll()
    notify_failed_classes()
