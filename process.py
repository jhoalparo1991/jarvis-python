import subprocess as sp
import pywhatkit as kit


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+57{number}", message)

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

