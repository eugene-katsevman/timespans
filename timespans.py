from datetime import datetime, timedelta
from operator import attrgetter


class TimeSpan:
    @property
    def empty(self):
        return self.start == self.end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value or datetime.min

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value or datetime.max

    @property
    def duration(self):
        return self.end - self.start

    def __init__(self, start, end):
        self._start = None
        self._end = None

        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "(%s, %s)" % (self.start, self.end)

    def __sub__(self, other):
        if other.start <= other.end <= self.start:
            return [self]
        elif self.end <= other.start <= other.end:
            return [self]
        elif other.start <= self.start <= other.end <= self.end:
            return [TimeSpan(other.end, self.end)]
        elif self.start <= other.start <= self.end <= other.end:
            return [TimeSpan(self.start, other.start)]
        elif other.start <= self.start <= self.end <= other.end:
            return []
        elif self.start <= other.start <= other.end <= self.end:
            return [TimeSpan(self.start, other.start),
                    TimeSpan(other.end, self.end)]
        else:
            raise Exception("Strange TimeSpan")


class TimeSpanSet:

    @property
    def duration(self):
        return sum([x.duration for x in self.spans], timedelta())

    def _converge(self):
        result = []
        current_span = None
        for span in sorted(self.spans, key=attrgetter('start')):
            if current_span is None:
                current_span = span
            else:
                if current_span.end == datetime.max:
                    break
                if current_span.end < span.start:
                    result.append(current_span)
                    current_span = span
                elif current_span.end < span.end:
                    current_span.end = span.end
        if current_span:
            result.append(current_span)

        result = [r for r in result if not r.empty]
        self.spans = result

    def __init__(self, timespans=None):
        self.spans = []
        if timespans:
            if isinstance(timespans, TimeSpan):
                self.spans.append(timespans)
            else:
                self.spans.extend(timespans)
        self._converge()

    def __sub__(self, other):
        spans = self.spans
        for span in other.spans:
            spans = sum((current_span - span for current_span in spans), [])

        return TimeSpanSet(spans)

    def __add__(self, other):
        return TimeSpanSet(self.spans + other.spans)

    def __eq__(self, other):
        assert isinstance(other, TimeSpanSet)

        return len(self.spans) == len(other.spans) and all(
            [x == y for x, y in zip(self.spans, other.spans)]
        )

    def __str__(self):
        return "["+", ".join([str(s) for s in self.spans])+"]"
