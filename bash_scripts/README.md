# dotfiles

### ssh-utcs-machine

A simple script to log in to one of the UTCS public machines without having to type anything in.

#### Usage:

1. Change ```myUsername```, ```a-public-machine```, ```myPassword``` to the appropriate parameters.

2. Put the script in the default working directory of your favorite iTerm2 profile.

3. In the "Command" section of the "General" pane of your profile preferences, enter ```expect ssh-utcs-machine```.

4. Whenever you open up an iTerm2 window with the profile you edited, it should automatically run this script and you should be ssh'd into a UTCS public machine without being prompted for your username or password!

