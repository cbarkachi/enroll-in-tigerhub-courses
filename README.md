# Enroll in Tigerhub Courses
Automatically enrolls in the courses you've sent to the queue on TigerHub.

Uses Selenium and the Chrome web driver to automatically enroll in classes at Princeton's horrendously scheduled 7:30am time (or whatever draconian time they happen to set this year).

## Some notes
Start by installing the required packages
pip3 install -r requirements.txt

I've added the latest Windows version of the web driver to the repo but you should update to the latest version for your platform--even if you're on Windows--[here](https://chromedriver.chromium.org/downloads).

Optimal usage: schedule the enroll_courses.py to run about a minute before the scheduled enrollment time. After navigating to the right page and logging you in, the script is set to wait until the exact enrollment time.

The purpose of including your Chrome profile is to avoid having to deal with Duo's two-factor authentication (the alternative would be saving your Duo auth token cookies, which would be significantly harder to do programmatically on a user-by-user basis).
