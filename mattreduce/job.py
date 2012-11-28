import collections


class Job(object):

    def __init__(self, mapper, reducer, finalizer=None):
        self.mapper = mapper
        self.reducer = reducer
        self.finalizer = finalizer

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
        # map
        mapped = (self.mapper(item) for item in items)
        # combine
        combined = self.combine(mapped)
        # reduce
        reduced = (self.reducer(key, values) for key, values in combined)

        if self.finalizer is None:
            return reduced

        finalized = self.finalizer(reduced)

        return finalized
