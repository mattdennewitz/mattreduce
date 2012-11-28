import collections


class Step(object):

    def __init__(self, mapper, reducer):
        self.mapper = mapper
        self.reducer = reducer


class Job(object):

    def __init__(self, steps=None, finalizer=None):
        self.steps = steps or []
        self.finalizer = finalizer

    def add_step(self, mapper, reducer):
        self.steps.append(Step(mapper, reducer))

    def combine(self, mapped_values):
        """Group mapped <key, value> pairs.
        """

        combined = collections.defaultdict(list)

        # group by key
        for gen in mapped_values:
            for key, emitted in gen:
                combined[key].append(emitted)

        # re-emit to reducer
        for key in combined:
            yield (key, combined[key])

    def run(self, items):
        for step in self.steps:
            # map
            mapped = (step.mapper(item) for item in items)
            # combine
            combined = self.combine(mapped)
            # print list(combined)
            # reduce
            reduced = (step.reducer(key, values) for key, values in combined)

        return reduced


if __name__ == '__main__':
    inputs = [
        {'val': 1},
        {'val': 2},
        {'val': 3}
    ]

    def mapper(items):
        for k, v in items.items():
            yield k, v

    def reducer(key, values):
        yield key, values

    job = Job()
    job.add_step(mapper, reducer)
    results = job.run(inputs)

    for result in results:
        print list(result)
