#!/bin/sh
echo "Backing up existing config files if any..."

if [ -d "$HOME/.config/openbox" ]; then
    mv "$HOME/.config/openbox" "$HOME/.config/openbox.bak"
fi
mkdir ~/.config/openbox

if [ -d "$HOME/.config/tint2" ]; then
    mv "$HOME/.config/tint2" "$HOME/.config/tint2.bak"
fi
mkdir ~/.config/tint2

if [ -d "$HOME/.config/obmenu-generator" ]; then
    mv "$HOME/.config/obmenu-generator" "$HOME/.config/obmenu-generator.bak"
fi
mkdir ~/.config/obmenu-generator

echo -n "->"
echo "openbox/rc.xml"
cp "$PWD/rc.xml" "$HOME/.config/openbox/rc.xml"

echo -n "->"
echo "openbox/autostart"
cp "$PWD/autostart" "$HOME/.config/openbox/autostart"

echo -n "->"
echo "openbox/menu.xml"
cp "$PWD/menu.xml" "$HOME/.config/openbox/menu.xml"

echo -n "->"
echo "tint2/tint2rc"
cp "$PWD/tint2rc" "$HOME/.config/tint2/tint2rc"

echo -n "->"
echo "init.sh"
cp "$PWD/init.sh" "$HOME/init.sh"
chmod +x "$HOME/init.sh"

echo -n "->"
echo "randomWallpaper.sh"
cp "$PWD/randomWallpaper.sh" "$HOME/randomWallpaper.sh"
chmod +x "$HOME/randomWallpaper.sh"

echo -n "->"
echo "setWall.sh"
cp "$PWD/setWall.sh" "$HOME/setWall.sh"
chmod +x "$HOME/setWall.sh"

echo -n "->"
echo "lemon.sh"
cp "$PWD/lemon.sh" "$HOME/lemon.sh"
chmod +x "$HOME/lemon.sh"

echo -n "->"
echo "volume_status.py"
cp "$PWD/volume_status.py" "$HOME/volume_status.py"

echo -n "->"
echo "obmenu-generator/schema.pl"
cp "$PWD/schema.pl" "$HOME/.config/obmenu-generator/schema.pl"

echo "Copied files successfully."
