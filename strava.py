from functions import *

#declare filenames with this weeks and last weeks date
last_monday, this_monday = get_dates()
filename_this = "Leaderboard_" + str(this_monday) + ".csv"
filename_last = "Leaderboard_" + str(last_monday) + ".csv"
write_csv_header(filename_this)
write_csv_header(filename_last)

#append all divisions data
write_csv_by_div(filename_last,
                 filename_this,
                 "London Market",
                 "https://www.strava.com/clubs/hiscox-lm-virtual-running-club-598946")

write_csv_by_div(filename_last,
                 filename_this,
                 "Reinsurance",
                 "https://www.strava.com/clubs/runners-of-hiscoxre-598340")

write_csv_by_div(filename_last,
                 filename_this,
                 "UK",
                 "https://www.strava.com/clubs/hiscox-u-k-virtual-wfh-running-club-598151")



### END ###






