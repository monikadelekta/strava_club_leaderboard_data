# Club Leaderboard Data Pulled From Strava

Strava is a social fitness network that tracks athletes running, cycling and swimming activites. Strava provides athletes the opportunity to join several clubs each with their own goals i.e. who can run/cycle/swim the fastest and/or furtherest. Each club page offers a leaderboard allowing the admin to track winners, this leaderboard shows the whole club those in the lead for both this week and the previous week. 

The aim of this repository is to gather the information from the leaderboard so the club can track winners over a longer period of time and compare themselves against other clubs. 

#### Strava API

Strava currently offers an [API](https://developers.strava.com), which is very useful to gether individual athlete information however, it does not provide a call for pulling any information from clubs or their leaderboards. 

#### How The Code Works

This code uses a selenium webdriver and Python to scrape the information from the Strava website and then pulls out only the leaderboard information.

The code will output two CSV files, this weeks leaderboard and last weeks leaderboard (with the week commencing Monday's date in the file name). Currently the code works for three clubs but this can be easily changed:

* [Hiscox LM Virtual Running Club](https://www.strava.com/clubs/HiscoxLM)
* [Hiscox U.K. Virtual WFH Running Club](https://www.strava.com/clubs/hiscox-u-k-virtual-wfh-running-club-598151)
* [Runners of HiscoxRe](https://www.strava.com/clubs/runners-of-hiscoxre-598340)

NOTE - This code needs to be run once a week to pull the weekly leaderboard

#### Python Packages Used

* Selenium 3.141.0
* CSV
* Datetime
