import runner

tasks = ['1', '2', '3']


class Consoler():

    def console(self, e):
        run = [runner.Runner1(), runner.Runner2()]
        for r in run:
            if e.is_set():
                print "Key int cons"
                break
            r.batch(e, tasks)
        print 'int but here'
