#!/bin/sh

sleep 2 && sh -c "~/setWall.sh" &
sleep 1 && export TERMINAL="xfce4-terminal" &
sleep 1 && sh -c "xautolock -time 5 -locker /usr/bin/i3lock-fancy -detectsleep" &
sleep 1 && sh -c "xcompmgr -cfn" &
sleep 1 && sh -c "./lemon.sh | lemonbar -g 1366x28+0+0 -f \"Cantarell\"-12 -f \"Font Awesome 5 Free:size=11\" -n \"openbox\"" &
sleep 1 && sh -c "xcape -e 'Super_L=Control_L|Shift_L|Alt_L|Super_L|D'" &
sleep 1 && tint2 &
