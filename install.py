import requests
import os
import subprocess

cwd = os.getcwd()

depends = {
    'tint2': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },

    'xcompmgr': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'xcompmgr'
    },

    'nitrogen': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },

    'openbox': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },

    'xautolock': {
        'Arch Linux': 'yay' ,
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install',
    },

    'lemonbar': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'repo'
    }

    'flameshot': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    }
    
    'i3lock-fancy': {
        'Arch Linux': 'repo',
        'Ubuntu': 'repo',
        'Fedora': 'repo'
    }

    
    'xcape': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    }
}

def download_file(url, filename, location):
    print("downloading " + filename + "...")
    r = requests.get(url)
    with open(location + filename, 'wb') as f:
        f.write(r.content)
    print("Download completed.")

def get_os_name():
        with open("/etc/os-release") as osr:
            return (osr.readline().strip().split("=")[1].replace("\"", ""))

distro = get_os_name()
print("detected distro " + distro)

def i3lock_fancy_install():
    i3lock_git = "https://github.com/meskarune/i3lock-fancy.git"
    subprocess.run(['git', 'clone', i3lock_git, cwd+"i3lock-fancy"])
    subprocess.run(["sudo", "make", "install"], cwd=cwd)

def install_lemonbar():
    lemon_git = "https://github.com/LemonBoy/bar"
    subprocess.run(['git', 'clone', i3lock_git, cwd+"lemonbar"])
    subprocess.run(['make'], cwd=cwd])
    subprocess.run(["sudo", "make", "install"], cwd=cwd])

installers = {
    'lemonbar': install_lemonbar,
    'i3lock-fancy': i3lock_fancy_install,
}

for depend in ['openbox', 'tint2', 'xcompmgr', 'nitrogen', 'xautolock', 'lemonbar', 'i3lock-fancy']:
    if not depends[depend][distro] == "repo":
        subprocess.run("sh", "-c", "\'", [depends[depend][distro] + depend] + "\'")
    else:
        installers[depend]()
