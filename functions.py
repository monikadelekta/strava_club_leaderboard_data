import datetime, csv
from selenium import webdriver

# call PhantomJS driver for webscraping
def new_driver(url):
    driver = webdriver.PhantomJS('/Library/Phantom/phantomjs')
    driver.get(url)
    return driver

#get correct dates for file names
def get_dates():
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday(), weeks=1)
    coming_monday = today + datetime.timedelta(days=-today.weekday())
    return last_monday, coming_monday

def write_csv_header(filename):
    with open(filename, 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Rank", "Athlete", "Distance", "Runs",
                         "Longest", "Avg. Pace", "Elevation Gain", "Division"])

# get this weeks top leaderboard runners
def this_weeks_leaderborad(driver):
    text_out = driver.find_element_by_xpath('//*[@class="dense striped sortable"]')
    return text_out

# get last weeks top leaderboard runners
def last_weeks_leaderborad(driver):
    elem = driver.find_element_by_xpath('//*[@class="button last-week"]').click()
    text_out = driver.find_element_by_xpath('//*[@class="dense striped sortable"]')
    return text_out


def write_last_weeks_leaderboard(filename, division, driver):
    text_out = last_weeks_leaderborad(driver)
    with open(filename, 'a', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in text_out.find_elements_by_css_selector('tr'):
            row_content = [d.text for d in row.find_elements_by_css_selector('td')]
            row_content.append(division)
            if len(row_content) > 1: #don't pull through empty header row
                wr.writerow(row_content)


def write_this_weeks_leaderboard(filename, division, driver):
    text_out = this_weeks_leaderborad(driver)
    with open(filename, 'a', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in text_out.find_elements_by_css_selector('tr'):
            row_content = [d.text for d in row.find_elements_by_css_selector('td')]
            row_content.append(division)
            if len(row_content) > 1:  # don't pull through empty header row
                wr.writerow(row_content)

def write_csv_by_div(filename_last, filename_this, division, url):
    driver = new_driver(url)
    write_last_weeks_leaderboard(filename_last, division, driver)
    write_this_weeks_leaderboard(filename_this, division, driver)