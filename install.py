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
    },

    'flameshot': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },

    'i3lock-fancy': {
        'Arch Linux': 'repo',
        'Ubuntu': 'repo',
        'Fedora': 'repo'
    },

    'xcape': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },

    'synapse': {
        'Arch Linux': 'yay',
        'Ubuntu': 'sudo apt install',
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
        'Ubuntu': 'sudo apt install',
        'Fedora': 'sudo dnf install'
    },
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

def i3lock_fancy_install():
    i3lock_git = "https://github.com/meskarune/i3lock-fancy.git"
    subprocess.run(['git', 'clone', i3lock_git, cwd+"i3lock-fancy"])
    subprocess.run(["sudo", "make", "install"], cwd=cwd)

def install_lemonbar():
    lemon_git = "https://github.com/LemonBoy/bar"
    subprocess.run(['git', 'clone', i3lock_git, cwd+"lemonbar"])
    subprocess.run(['make'], cwd=cwd)
    subprocess.run(["sudo", "make", "install"], cwd=cwd)

def obm_gen_install():
    obm_gen_url = 'https://github.com/trizen/obmenu-generator/raw/master/obmenu-generator'
    download_file(obm_gen_url, 'obmenu-generator', cwd)
    subprocess.run(['chmod', '+x', cwd + 'obmenu-generator'])
    subprocess.run(['sudo', '/bin/cp', cwd + 'obmenu-generator /usr/bin'])
    
distro = get_os_name()
print("detected distro " + distro)

installers = {
    'lemonbar': install_lemonbar,
    'i3lock-fancy': i3lock_fancy_install,
    'obmenu-generator': obm_gen_install
}

print("installing dependencies...")

for depend in ['openbox', 'obmenu-generator', 'tint2', 'xcompmgr', 'nitrogen', 'xautolock', 'lemonbar', 'i3lock-fancy', 'flameshot', 'xcape', 'synapse']:
    print("installing " + depend + "...")
    if not depends[depend][distro] == "repo":
        subprocess.run(["sh", "-c", "\'", depends[depend][distro] + " " + depend + "\'"])
    else:
        installers[depend]()

print("copying configs...")
subprocess.run(['sh', cwd+"cpConfig.sh"])

print("SDE install completed successfully.")
