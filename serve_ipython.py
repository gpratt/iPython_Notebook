#!/nas/nas0/gpratt/gabe_default/bin/python
import sys
from subprocess import Popen

port = sys.argv[1]
mongoport=sys.argv[2]
print port, mongoport

try:
    c = Popen(["ssh", "-L", ("%s:localhost:%s" %(mongoport, mongoport)), "oolite", "-N"])
except:
    print "not linking mongodb"


b = Popen(["ipython", "notebook", "--no-browser", "--port", "%s" %(port), "--pylab", "inline"])
b.wait()

a = Popen(["ssh", "-R", ("%s:localhost:%s" %(port, port)), "oolite", "-N"])




a.wait()

if c:
    c.wait()
