# StrawPoll_Scraper
Basic scraper for Strawpoll(dot)me site polls, using BeautifulSoup

I'm currently working on updating it with a pandas/matplotlib version for displaying data in a graph, by default it saves data in a CSV file for later use.

##  REQUIRED:

* PYTHON 3
* BeautifulSoup (*pip install beautifulsoup4*)

##  SYNTAX:

> strawpoll_scraper.py --url <POLL-RESULTS-URL> --name <CSV-FILE-NAME-WITHOUT-EXTENSION> --> feeds the scraper with the URL then loads the data in a CSV file using the --name variable [if --name is omitted the output file will be a generic "poll.csv"]
> strawpoll_scraper.py --help                                                            --> **helper**
