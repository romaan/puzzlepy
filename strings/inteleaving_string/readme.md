# Problem: Interleaving String

## Statement

You’re given three strings: s1, s2, and s3. Your task is to determine whether s3 can be formed by interleaving s1 and s2.

Interleaving means you take both strings and break them into smaller pieces (substrings), then merge those pieces while preserving the left-to-right order of characters within each original string.

The final mixed string might look like any of the following:


The pieces from s1 and s2 must appear in alternating segments, although either one is allowed to start first. The number of segments taken from each string should differ by at most one.

Constraints:

0 ≤ s1.length, s2.length ≤ 100

0 ≤ s3.length ≤ 200

s1, s2, and s3 consist of lowercase English letters.

# Solution

## Dynamic programming

Core idea

At every position in s3, you only have two legal choices:

Take the next character from s1

Take the next character from s2

You must:

Use characters from each string in order

Use all characters from both strings

Match s3 exactly from left to right

This naturally leads to Dynamic Programming.

Step 1: Length check (mandatory)

If s1 has n chars and s2 has m chars, then:

s3 must have n + m characters


If not → immediately False.

Step 2: Define the DP state

Define:

dp[i][j] = True if
s3[0 .. i+j-1] can be formed
using s1[0 .. i-1] and s2[0 .. j-1]


So:

i = how many chars taken from s1

j = how many chars taken from s2

i + j = how many chars built in s3

Step 3: Base case
dp[0][0] = True


Empty s1 + empty s2 forms empty s3.

Step 4: Transition (the heart of the algorithm)

To compute dp[i][j], look at the last character of the prefix:

s3[i + j - 1]


There are only two possibilities:

Option 1: Last char came from s1

This is valid if:

We already formed dp[i-1][j]

s1[i-1] == s3[i+j-1]

Option 2: Last char came from s2

This is valid if:

We already formed dp[i][j-1]

s2[j-1] == s3[i+j-1]

So:

dp[i][j] =
    (dp[i-1][j] AND s1[i-1] == s3[i+j-1])
 OR (dp[i][j-1] AND s2[j-1] == s3[i+j-1])

Step 5: Fill the table

You fill the DP table row by row or column by column, ensuring smaller prefixes are computed first.

The final answer is:

dp[len(s1)][len(s2)]

Visual intuition (grid view)

Think of a grid:

Rows = characters from s1

Columns = characters from s2

Moving down = take from s1

Moving right = take from s2

You start at (0,0) and want to reach (n,m).

Each move must match the next character in s3.

If any path reaches the bottom-right cell, interleaving is possible.

Why this guarantees correctness

You never skip characters → order preserved

You try both valid choices → no missed interleavings

DP avoids exponential backtracking

Complexity

Time: O(n × m)

Space: O(n × m) (or O(m) optimized)

One-sentence summary

The algorithm checks whether every prefix of s3 can be built by legally consuming prefixes of s1 and s2, using dynamic programming to explore all valid interleavings efficiently.

If you want, I can also draw the full DP table for "abc", "def", "abdcef" step by step.
