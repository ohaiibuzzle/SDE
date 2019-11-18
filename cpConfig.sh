#!/bin/sh

if [ -d "$HOME/.config/openbox" ]; then
    echo -e ""
else
    mkdir ~/.config/openbox
fi

if [ -d "$HOME/.config/tint2" ]; then
    echo -e ""
else
    mkdir ~/.config/tint2
fi

if [ -d "$HOME/.config/obmenu-generator" ]; then
    echo -e ""
else
    mkdir ~/.config/obmenu-generator
fi

cp "$PWD/rc.xml" "$HOME/.config/openbox/rc.xml"
cp "$PWD/autostart" "$HOME/.config/openbox/autostart"
cp "$PWD/menu.xml" "$HOME/.config/openbox/menu.xml"
cp "$PWD/tint2rc" "$HOME/.config/tint2/tint2rc"
cp "$PWD/init.sh" "$HOME/init.sh"
cp "$PWD/randomWallpaper.sh" "$HOME/randomWallpaper.sh"
cp "$PWD/setWall.sh" "$HOME/setWall.sh"
cp "$PWD/lemon.sh" "$HOME/lemon.sh"
cp "$PWD/volume_status.py" "$HOME/volume_status.py"
cp "$PWD/schema.pl" "$HOME/.config/obmenu-generator/schema.pl"
echo "Copied files successfully."
