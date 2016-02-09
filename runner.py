import subprocess
import signal

def ign():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

class Runner1(object):

    def run(self, task):
        print 'runner1 %s' %task
        res = subprocess.check_output(
                ["sleep", "30"],
            preexec_fn=ign)
        #res = subprocess.check_output(
        #        ["docker", "exec", "-it", "5eb66619e742", "sleep", "30"],
        #        preexec_fn=ign)

        print 'wake up1'

    def batch(self, e, tasks):
        for task in tasks:
            if e.is_set():
                print 'key int run 1'
                break
            self.run(task)
        print 'keuy int but here run1'


class Runner2(object):

    def run(self, task):
        print 'runner2 %s' %task
        res = subprocess.check_output(["sleep", "30"],
            preexec_fn=ign)
        #res = subprocess.check_output(
        #        ["docker", "exec", "-it", "5eb66619e742", "sleep", "30"],
        #        preexec_fn=ign)

        print 'wake up2'

    def batch(self,e, tasks):
        for task in tasks:
            if e.is_set():
                print 'key int run 2'
                break
            self.run(task)

        print "key int but here 2"