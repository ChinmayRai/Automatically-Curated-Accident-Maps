import subprocess

# subprocess.call(['df','-h'])
p = subprocess.Popen(["echo","hello world"], stdout=subprocess.PIPE)

print p.stdout.read()
print p.stdout.read()

print p.communicate()
