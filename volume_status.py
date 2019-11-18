import subprocess
mute_status = subprocess.run(["pamixer", "--get-mute"], capture_output=True)
vol = subprocess.run(["pamixer", "--get-volume"], capture_output=True)
if (mute_status.stdout.decode().strip() == "true"):
    print("%{B#Ff5555}%{F#F5F4F0}[muted] " + vol.stdout.decode().strip() + "% ")
else:
    print("%{B#FABD2f}%{F#F5F4F0} " + vol.stdout.decode().strip() + "% ")