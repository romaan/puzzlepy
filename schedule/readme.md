You’re given n tasks, each as an interval [start, end].

One machine can run only one task at a time.

A new task can start exactly when another ends (so [1,3] and [3,5] don’t overlap).

You have unlimited machines.

Goal: Find the minimum number of machines needed so that all tasks can be run.

That number is exactly the maximum number of tasks overlapping at any moment.


Solution

Sorted events:

(1, +1)
(2, +1)
(4, -1)
(4, +1)
(5, -1)
(6, -1)

Sweeping through time

We walk through the events in order, keeping a running count.

Time	Change	Running Tasks
1	+1	1
2	+1	2
4	-1	1
4	+1	2
5	-1	1
6	-1	0

The maximum running tasks = 2, so we need 2 machines.
