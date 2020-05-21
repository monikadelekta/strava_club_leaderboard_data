# Club Leaderboard Data 

Strava is a social fitness network that tracks athletes running, cycling and swimming activites. It provides athletes the opportunity to join several clubs each with their own goals i.e. who can run/cycle/swim the fastest and/or furtherest. Each club page offers a leaderboard allowing the admin to track winners, this leaderboard shows the whole club those in the lead for both this week and the previous week. 

The aim of this repository is to gather the information from the leaderboard so the club can track winners over a longer period of time and compare themselves against other clubs. 

#### How The Code Works

This code uses a selenium webdriver and Python to scrape the information from the Strava website and then pulls out only the leaderboard information.

The code will output two CSV files, this weeks leaderboard and last weeks leaderboard (with the week commencing Monday's date in the file name).

#### Python Packages Used

* Selenium 3.141.0
* CSV
* Datetime
