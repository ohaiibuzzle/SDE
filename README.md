# SDE

## Introduction
Shan's Desktop Environment, a lightweight openbox-based desktop environment made to balance prettiness and performance, while not sacrificing usability.

The install script works for Ubuntu, Fedora, and Arch Linux.
If you're not on one of these, then see the section on "Unsupported environments." Feel free to add your own distro and send a pull, I will look at it at the soonest possible.

#### dependencies:

- [pamixer](https://github.com/cdemoulins/pamixer)
- [i3lock-color](https://github.com/PandorasFox/i3lock-color)
- perl
- imagemagick
- bash
- awk
- util-linux
- lm-sensors

#### Fonts
- Font Awesome 5
- Cantarell Sans


## Installing

Easy - just 

  0) Make sure the depends are taken care of first, ESPECIALLY if you're on Fedora!
  1) clone the repo
  2) cd into the directory
  3) edit init.sh replacing ```1366``` with your screen's width.
  4) run the install script with ```python3 install.py```.
  
You should then create and populate a folder in your home directory called wallpapers, containing PNG or JPG backgrounds. 

## Unsupported environments

- openbox
- obmenu-generator
- tint2
- xcompmgr
- nitrogen
- xautolock
- lemonbar
- i3lock-fancy
- flameshot
- xcape
- synapse
- xdotool
- xfce4-terminal

You will have to install the above applications yourself, then run cpConfig.sh

## Screens

##### \<fryst\> shan: nice
##### \<fryst\> you have any screens?

this one's for you, fryst.
![image](https://i.imgur.com/zPjyBbF.jpg)
![image](https://i.imgur.com/5E4l3uP.png)
