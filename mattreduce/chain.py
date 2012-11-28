class JobChain(object):

    def __init__(self, jobs, finalizer=None):
        self.jobs = job
        self.finalizer = finalizer
        self.state = None

    def run(self, items):
        self.state = items

        for job in self.jobs:
            results = job.run(self.state)
            self.state = results

        if self.finalizer is not None:
            return self.finalizer(self.state)

        return self.state
