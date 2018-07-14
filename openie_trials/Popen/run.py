from subprocess import PIPE, Popen

p=Popen(['java','c'],stdin=PIPE)
# print "called"

# subprocess.call(['java','-Xmx10g','-XX:+UseConcMarkSweepGC','-jar', 'openie-assembly-5.0-SNAPSHOT.jar'])
# Popen(['g++','a.cpp'])
# p=Popen(['./','a.out'],stdin=PIPE,stdout=PIPE)

# for i in range(10):
p.stdin.write("qwe")
	# print p.stdout.readline()

# p.stdin.write("-1")
# print "done dona done"


#import os

#if __name__ == "__main__":
#	startingDir = os.getcwd() # save our current directory
#	testDir = "\\test" # note that \ is windows specific, and we have to escape it
#	os.chdir(testDir) # change to our test directory
#   os.system("java -Xmx10g -XX:+UseConcMarkSweepGC -jar openie-assembly-5.0-SNAPSHOT.jar")
#	os.chdir(startingDir) # change back to where we started

