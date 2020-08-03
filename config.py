from datetime import datetime


class Config:
    # /Selenium settings/

    # The path below is for Windows. Modify accordingly for Mac.
    chrome_path = r"C:\Users\[YOUR USERNAME]\AppData\Local\Google\Chrome\User Data"

    # /Email Settings/

    email_username = 'YOUR EMAIL'
    # need to supply an app password for EMAIL_PASSWORD if using gmail
    email_password = 'YOUR PASSWORD HERE'
    recipients = ['trump@whitehouse.gov', '123456789@tmomail.net']
    email_subject = 'TigerHub course enrollment'
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587

    # Time settings
    # From Python docs: datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
    enroll_time = datetime(2020, 8, 3, 7, 30)
