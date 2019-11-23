from time import sleep
from datetime import datetime
from sh import gphoto2 as gp

def killGphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            pid = int(line.split(None,1)[0])
            os.kill(pid,signal.SIGKILL)

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiShots"

clearCommand = ["--folder", "/storage_xxxxxxxx/DCIM/100CANON", "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]


save_location = "/home/pi/Destkop/gphoto/img"

def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("bestaat al")
    os.chdir(save_location)

def catprueImages():
    gp(triggerCommand)
    sleep(1)
    gp(downloadCommand)
    gp(clearCommand)
    
def captureSetup():
    killGphoto2Process()
    createSaveFolder()
    catprueImages()
    print("setup complete")

    
    
