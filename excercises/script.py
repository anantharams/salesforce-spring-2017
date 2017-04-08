"""""
Write a command line script to call your function

    scrape_channels()

and return some basic statistics (mean, median, or mode) about it. 

Examples:

    python excercises/script.py --statistic mean --odds
        - print the mean of only the odd-indexed (1 (2nd), 3 (4th), ...) frequencies

    python excercises/script.py --statistic median --even
        - print the median of only the even-ordered (0 (1st), 2 (3rd), ...) frequencies

    python excercises/script.py --statistic mode 
        - print the median of all frequencies

    python excercises/script.py 
        - print the mean of all frequencies (mean is the default)

1) Your script should also say something nice with people call for help like:

    python excercises/script.py --help

2) If a user enters a statistic not availiable, please output an error message a return a non-zero exit code. 
3) User cannot specific both evens and odds - please return error if so likewise. 

You'll probably want to use the argparse library as well as your previous code for scraping :)
""""" 

import argparse
from answers.http import scrape_channels 

# ... do your thing here!
