Testing:
Due to the 90 minute time constraint, I was unable to test the code as
extensively as I would have liked. I tested the individual components through
manual unit testing by creating objects and verifying that they had the correct
properties. Most of my system testing was carried out using the example rule file.
I manually tested various inputs, including edge cases, and ensured that these had the correct outputs.
Given more time I would create a larger rule file with a wider variety of test inputs and work on automating some tests.

Design choices:
To allow greater efficiency than simply searching the entire list of rules, I chose to create a dictionary
that maps the tuple of direction and protocol to a list for each combination. Since there are only four
valid direction/protocol combinations, this allows reduction in search time of up to a factor of four
without major additional space use.

I also considered opening the csv file for each packet and iterating lines until a matching line
was found. This would have saved some memory, as it would no longer require the entire set of
rules to be stored in memory. However, this has a higher search time and incurs the
overhead of frequent file IO.

Team preference:
Based on my skills and interests, I am most interested in the Policy team.
