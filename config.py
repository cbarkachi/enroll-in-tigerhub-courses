from datetime import datetime


class Config:
    # /Selenium settings/

    # The path below is for Windows. Modify accordingly for Mac.
    # https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/#:~:text=The%20location%20for%20Chrome's%20default,Support%2FGoogle%2FChrome%2FDefault
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
