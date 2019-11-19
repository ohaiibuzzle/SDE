#!/bin/bash

Clock() {
	TIME=$(date "+%S seconds past %H%M")
	echo -e -n "%{B#444444}%{F#f5f4f0} \uf017  ${TIME}"
}

Cal() {
    DATE=$(date "+%a, %m %B %Y")
    echo -e -n "%{B#f2e5bc}%{F#303030} \uf073  ${DATE}"
}

ActiveWindow() {
	len=$(echo -n "$(xdotool getwindowfocus getwindowname)" | wc -m)
	max_len=70
	if [ "$len" -gt "$max_len" ];then
		echo -n "$(xdotool getwindowfocus getwindowname | cut -c 1-$max_len)..."
	else
		echo -n "$(xdotool getwindowfocus getwindowname)"
	fi
}

Sound() {
	echo -n $(python3 ~/volume_status.py)
}

CPUTemp() {
    temp=$($(echo cat "/sys/class/thermal/$(ls /sys/class/thermal/ | grep thermal_zone | tail -1)/temp") | sed s/000//)
	echo -e "%{B#fbf1fc} %{F#cc241d}cpu at ${temp}\u00B0C"
}

while true; do
	echo -e "%{B#007cdf}%{F#f5f4f0}%{l} $(ActiveWindow) %{c}$(Clock) %{r}$(Cal) $(CPUTemp) $(Sound) %{B#003c3836}"
	sleep 0.1s
done
