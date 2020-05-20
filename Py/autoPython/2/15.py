import subprocess,os
Proc = subprocess.Popen("D:\\portable program\\texstudio-2.12.22-win-portable-qt5\\texstudio.exe")
print(Proc.poll() == None)
print(Proc.wait())
Proc.poll()
filename = 'hello.txt'
if not os.path.exists(filename ):
    a = open('hello.txt', 'w')
    a.close()
subprocess.Popen(['start', 'hello.txt'],shell = True)