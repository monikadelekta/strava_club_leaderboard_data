import datetime, csv
from selenium import webdriver

def new_driver(url):
    """
    This function calls the PhantomJS driver for webscraping
    :param url: the strava URL where the club exists
    :return: the created phantomjs driver
    """
    driver = webdriver.PhantomJS('/Library/Phantom/phantomjs')
    driver.get(url)
    return driver

def get_dates():
    """
    This function gets this and last week Monday's date for the
    correct usage in filenames
    :return:
    """
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday(), weeks=1)
    coming_monday = today + datetime.timedelta(days=-today.weekday())
    return last_monday, coming_monday

def write_csv_header(filename):
    """
    Create a CSV file and add a static header to it
    :param filename: the filename for the csv to be created and saved as
    :return: none, this function creates the csv only
    """
    with open(filename, 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Rank", "Athlete", "Distance", "Runs",
                         "Longest", "Avg. Pace", "Elevation Gain", "Division"])

def this_weeks_leaderborad(driver):
    """
    Get this weeks top leader board runners
    :param driver: the phantomjs driver for webscraping
    :return: text extracted from the leader board table element
    """
    text_out = driver.find_element_by_xpath('//*[@class="dense striped sortable"]')
    return text_out

def last_weeks_leaderborad(driver):
    """
    Get last weeks top leader board runners
    :param driver: the phantomjs driver for webscraping
    :return: text extracted from the leader board table element
    """
    # .click() selects the button on the webpage to change the leader board viewed
    elem = driver.find_element_by_xpath('//*[@class="button last-week"]').click()
    text_out = driver.find_element_by_xpath('//*[@class="dense striped sortable"]')
    return text_out

def write_last_weeks_leaderboard(filename, division, driver):
    """
    Append last weeks data to the extisting csv file
    :param filename: filename for the existing csv where leader board can be saved
    :param division: part of the business (UK, Re, LM)
    :param driver: the phantomjs driver
    :return: null, this function appends to an existing CSV file
    """
    text_out = last_weeks_leaderborad(driver)
    with open(filename, 'a', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in text_out.find_elements_by_css_selector('tr'):
            row_content = [d.text for d in row.find_elements_by_css_selector('td')]
            row_content.append(division)
            if len(row_content) > 1: #don't pull through empty header row
                wr.writerow(row_content)

def write_this_weeks_leaderboard(filename, division, driver):
    """
    Append this weeks leader board data to the existing csv file
    :param filename: the filename to be used with this weeks date
    :param division: the business area (UK, Re, LM)
    :param driver: the phantomjs driver
    :return: null, this function only appends to the existing file
    """
    text_out = this_weeks_leaderborad(driver)
    with open(filename, 'a', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in text_out.find_elements_by_css_selector('tr'):
            row_content = [d.text for d in row.find_elements_by_css_selector('td')]
            row_content.append(division)
            if len(row_content) > 1:  # don't pull through empty header row
                wr.writerow(row_content)

def write_csv_by_div(filename_last, filename_this, division, url):
    """
    Function to call all functions needed to append correctly to each CSV file
    by division and specific URL
    :param filename_last: last weeks date filename
    :param filename_this: this weeks date filename
    :param division: the business area (UK, Re, LM)
    :param url: the url for the specified club
    :return: null, this function only calls other functions
    """
    driver = new_driver(url)
    
    write_this_weeks_leaderboard(filename_this, division, driver)
    write_last_weeks_leaderboard(filename_last, division, driver)


### END ###