import requests
import os
import subprocess

cwd = os.getcwd() + "/"

depends = {
    'tint2': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },

    'xcompmgr': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'xcompmgr'
    },

    'nitrogen': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },

    'openbox': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },

    'xautolock': {
        'Arch Linux': 'yay' ,
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install',
    },

    'lemonbar': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'repo'
    },

    'flameshot': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },

    'i3lock-fancy': {
        'Arch Linux': 'repo',
        'Ubuntu': 'repo',
        'Fedora': 'repo'
    },

    'xcape': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },

    'synapse': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },

    'obmenu-generator': {
        'Arch Linux': 'yay',
        'Ubuntu': 'repo',
        'Fedora': 'repo',
    },

    'xdotool': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },

    'xfce4-terminal': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt-get install',
        'Fedora': 'sudo dnf install'
    },
}

def download_file(url, filename, location):
    print("downloading " + filename + " from " + url + "...")
    r = requests.get(url)
    with open(location + filename, 'wb') as f:
        f.write(r.content)
    print("Download completed.")

def get_os_name():
        with open("/etc/os-release") as osr:
            return (osr.readline().strip().split("=")[1].replace("\"", ""))

def i3lock_fancy_install():
    i3lock_git = "https://github.com/meskarune/i3lock-fancy.git"
    subprocess.run(['git', 'clone', i3lock_git], cwd="/tmp")
    subprocess.run(["sudo", "make", "install"], cwd="/tmp/i3lock-fancy")

def install_lemonbar():
    lemon_git = "https://github.com/LemonBoy/bar"
    subprocess.run(['git', 'clone', lemon_git], cwd="/tmp")
    subprocess.run(['make'], cwd="/tmp/bar")
    subprocess.run(["sudo", "make", "install"], cwd="/tmp/bar")

def obm_gen_install():
    obm_gen_url = 'https://github.com/trizen/obmenu-generator/raw/master/obmenu-generator'
    download_file(obm_gen_url, 'obmenu-generator', "/tmp")
    subprocess.run(['chmod', '+x', '/tmp/obmenu-generator'])
    subprocess.run(['sudo', '/bin/cp', '/tmp/obmenu-generator', '/usr/bin/obmenu-generator'])
    
distro = get_os_name()
print("detected distro " + distro)

if distro == 'Arch Linux':
    print("This script requires yay to install packages on Arch Linux. Install it? (y/n) ")
    answer = input("> ")
    if str(answer) == "y":
        subprocess.run(['sudo', 'pacman', '-Sy', 'yay'])
    else:
        print("Script cannot continue without yay. Exiting...")
        exit()

installers = {
    'lemonbar': install_lemonbar,
    'i3lock-fancy': i3lock_fancy_install,
    'obmenu-generator': obm_gen_install
}

print("installing dependencies...")

for depend in ['openbox', 'obmenu-generator', 'xfce4-terminal', 'tint2', 'xcompmgr', 'nitrogen', 'xautolock', 'lemonbar', 'i3lock-fancy', 'flameshot', 'xcape', 'synapse']:
    print("installing " + depend + " via method \'" + depends[depend][distro] + "\'...")
    if not depends[depend][distro] == "repo":
        subprocess.run(["sh", "-c", depends[depend][distro] + " " + depend + " > /dev/null"])
    else:
        installers[depend]()

print("copying files...")
subprocess.run(['sh', cwd+"copyFiles.sh"])

print("SDE install completed successfully. You should create and populate ~/wallpapers now.")
