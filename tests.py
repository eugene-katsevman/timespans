from timespans import TimeSpanSet, TimeSpan
from datetime import datetime
from unittest import TestCase


class SpanSetCase(TestCase):
    def test_converge(self):
        span_set = TimeSpanSet([TimeSpan(datetime(2015, 5, 1, 0), datetime(2015, 5, 1, 4)),
                                TimeSpan(datetime(2015, 5, 1, 0), datetime(2015, 5, 1, 5)),
                                TimeSpan(datetime(2015, 5, 1, 5,30), datetime(2015, 5, 1, 6))])

        self.assertEqual(span_set, TimeSpanSet([TimeSpan(datetime(2015, 5, 1), datetime(2015, 5, 1, 5)),
                                    TimeSpan(datetime(2015, 5, 1, 5, 30), datetime(2015, 5, 1, 6))]))

    def test_add(self):
        span_set = TimeSpanSet([TimeSpan(datetime(2015, 5, 1, 0), datetime(2015, 5, 1, 4)),
                                TimeSpan(datetime(2015, 5, 1, 0), datetime(2015, 5, 1, 5)),
                                TimeSpan(datetime(2015, 5, 1, 5, 30), datetime(2015, 5, 1, 6))])

        span_set2 = TimeSpanSet(TimeSpan(start=datetime(2015, 5, 1, 5), end=datetime(2015, 5, 1, 7)))

        self.assertEqual(span_set + span_set2,
                         TimeSpanSet([TimeSpan(datetime(2015, 5, 1), datetime(2015, 5, 1, 7))]))

    def test_sub(self):
        span_set = TimeSpanSet([TimeSpan(datetime(2015, 5, 1, 0), datetime(2015, 5, 1, 4)),
                                TimeSpan(datetime(2015, 5, 1, 0), datetime(2015, 5, 1, 5)),
                                TimeSpan(datetime(2015, 5, 1, 5, 30), datetime(2015, 5, 1, 6))])

        span_set2 = TimeSpanSet(TimeSpan(start=datetime(2015, 5, 1, 5), end=datetime(2015, 5, 1, 7)))

        self.assertEqual(span_set - span_set2,
                         TimeSpanSet([TimeSpan(datetime(2015, 5, 1), datetime(2015, 5, 1, 5))]))
