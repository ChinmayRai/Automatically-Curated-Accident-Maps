from subprocess import call,PIPE, Popen

call(["g++","a.cpp"])
p=Popen(['./a.out'],stdin=PIPE,stdout=PIPE)

for i in range(30):
	# print str(i)
	print p.stdin.write(str(i))
	# print p.stdout.readline()

print p.communicate("-1")

# print p.stdin.write("-1")
# print p.stdout.readline()

# p=Popen(['java','c'],stdin=PIPE)
# print "called"

# subprocess.call(['java','-Xmx10g','-XX:+UseConcMarkSweepGC','-jar', 'openie-assembly-5.0-SNAPSHOT.jar'])

# Popen(['g++','a.cpp'])
# p=Popen(['./a.out'],stdin=PIPE,stdout=PIPE)

# p=Popen(['python','b.py'])

# for i in range(10):
# p.stdin.write("qwe")
	# print p.stdout.readline()

# p.stdin.write("-1")

# print "ending c program now"
# p.stdin.write("^C")
# print "done dona done"

#import os

#if __name__ == "__main__":
#	startingDir = os.getcwd() # save our current directory
#	testDir = "\\test" # note that \ is windows specific, and we have to escape it
#	os.chdir(testDir) # change to our test directory
#   os.system("java -Xmx10g -XX:+UseConcMarkSweepGC -jar openie-assembly-5.0-SNAPSHOT.jar")
#	os.chdir(startingDir) # change back to where we started

