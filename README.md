# NoPotTukin

<details>
<summary>For macOS by Emil</summary>

## For macOS by Emil

Tested on macOS Catalina 10.15.5

**How to use:**

0. Use commonsense

**Edit py files inside python folder**

1. Replace 'putyourpasswordhere' with your password
2. Replace 'putyourNIPhere' with your NIP

**Edit plist files inside LaunchDaemons folder**

3. Rename the file name (optional)
4. Rename the <key>Label</key> string (optional)
5. Replace 'yourusername' with your macOS user name
6. Adjust the time for when the script will be excecuted at every weekday (optional)

**Open finder**

7. Put the plist files into /Library/LaunchDaemons/
8. Put the python files into ~/ (or whatever directory that you want, just don't forget to adjust the codes inside the plist and py)

**Open terminal**

9. type 'launchctl load /Library/LaunchDeamons/org.whatever.ClockOutEdjpb.plist'
10. type 'launchctl load /Library/LaunchDeamons/org.whatever.ClockInEdjpb.plist'

Enjoy your life

This method will runs even when your Mac sleep, make sure Power Nap is Enabled on System Preference. 

If anyone can improve the python script to be able to fill the health check, I'll be very thankful.

</details>

<details>
<summary>For Windows by Emil (based on Zaenal's code)</summary>

## For Windows by Emil (based on Zaenal's code)
Tested on Windows 8

**How to use:**

0. Use commonsense

**Edit config.py file**

1. Replace 'putyourpasswordhere' with your password
2. Replace 'putyourNIPhere' with your NIP
3. Adjust localTaskxls with your directory

**Edit .bat files**

4. Adjust log and python directory with your directory

**Notes for task.xlsx**

- T = Tusi, while for Non Tusi you can use anything else or just leave it blank 
- "F" column is total time you can use for task input, while "E" column is for time reduction 
- "H1" cell is the sum of all task time, it is recommended to get at least 385 minutes of task time each day

**Set Scheduller**

5. Find out how to make the scheduller on Google

You can disable task input by deleting or commenting line 168 on clock_out.py

Enjoy your life


</details>
