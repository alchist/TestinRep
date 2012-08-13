from subprocess import Popen, PIPE
x=Popen("ls -1", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split('\n')
x.pop()
for y in x:
	print y