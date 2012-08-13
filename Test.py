import subprocess
x=subprocess.Popen("ls -1", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().split('\n')
x.pop()
for y in x:
	subprocess.call(['mv',y,y[-10:]] )
