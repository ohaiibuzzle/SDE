#!/bin/sh

if [ -d "~/.config/openbox" ]; then
    echo -e ""
fi
else
    mkdir ~/.config/openbox
fi

if [ -d "~/.config/tint2" ]; then
    echo -e ""
fi
else
    mkdir ~/.config/tint2
fi

if [ -d "~/.config/obmenu-generator" ]; then
    echo -e ""
fi
else
    mkdir ~/.config/obmenu-generator
fi

cp "$PWD/rc.xml" "~/.config/openbox/"
cp "$PWD/autostart" "~/.config/openbox/"
cp "$PWD/menu.xml" "~/.config/openbox/"
cp "$PWD/tint2rc" "~/.config/tint2"
cp "$PWD/init.sh" ~
cp "$PWD/randomWallpaper.sh" ~
cp "$PWD/setWall.sh" ~
cp "$PWD/lemon.sh" ~
cp "$PWD/volume_status.py" ~
cp "$PWD/schema.pl" "~/.config/obmenu-generator"
echo "Copied files successfully."
