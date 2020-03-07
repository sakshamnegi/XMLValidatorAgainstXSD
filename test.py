import os

currentdir = os.getcwd()
logdir = os.path.join(currentdir,'logs')

if not os.path.exists(logdir):
    os.mkdir(logdir)
    print("Log Directory created ")
else:    
    print("Log Directory already exists")
logdir = os.path.join(logdir,'file.txt')
f = open(logdir,'w')
f.write("hi")
