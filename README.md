# NoPotTukin

For macOS:

eDJPB:

Tested on macOS Catalina 10.15.5

How to use:

0. Use commonsense

--edit py files inside python folder--
1. Replace 'putyourpasswordhere' with your password
2. Replace 'putyourNIPhere' with your NIP

--edit plist files inside LaunchDaemons folder--

3. Rename the file name (optional)
4. Rename the <key>Label</key> string (optional)
5. Replace 'yourusername' with your macOS user name
6. Adjust the time for when the script will be excecuted at every weekday (optional)

--open finder--
7. Put the plist files into /Library/LaunchDaemons/
8. Put the python files into ~/ (or whatever directory that you want, just don't forget to adjust the codes inside the plist and py)

--open terminal--
9. type 'launchutil load /Library/LaunchDeamons/org.whatever.ClockOutEdjpb.plist'
10. type 'launchutil load /Library/LaunchDeamons/org.whatever.ClockInEdjpb.plist'

Enjoy your life

This method will runs even when your Mac sleep, make sure Power Nap is Enabled on System Preference. 
