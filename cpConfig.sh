#!/bin/sh

if [ -d "$HOME/.config/openbox" ]; then
:
else
    mkdir ~/.config/openbox
fi

if [ -d "$HOME/.config/tint2" ]; then
:
else
    mkdir ~/.config/tint2
fi

if [ -d "$HOME/.config/obmenu-generator" ]; then
:
else
    mkdir ~/.config/obmenu-generator
fi
echo "openbox/rc.xml"
cp "$PWD/rc.xml" "$HOME/.config/openbox/rc.xml"

echo "openbox/autostart"
cp "$PWD/autostart" "$HOME/.config/openbox/autostart"

echo "openbox/menu.xml"
cp "$PWD/menu.xml" "$HOME/.config/openbox/menu.xml"

echo "tint2/tint2rc"
cp "$PWD/tint2rc" "$HOME/.config/tint2/tint2rc"

echo "init.sh"
cp "$PWD/init.sh" "$HOME/init.sh"

echo "randomWallpaper.sh"
cp "$PWD/randomWallpaper.sh" "$HOME/randomWallpaper.sh"

echo "setWall.sh"
cp "$PWD/setWall.sh" "$HOME/setWall.sh"

echo "lemon.sh"
cp "$PWD/lemon.sh" "$HOME/lemon.sh"

echo "volume_status.py"
cp "$PWD/volume_status.py" "$HOME/volume_status.py"

echo "obmenu-generator/schema.pl"
cp "$PWD/schema.pl" "$HOME/.config/obmenu-generator/schema.pl"

echo "Copied files successfully."
