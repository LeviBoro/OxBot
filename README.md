# OxBot
_Using machine learning to immitate the style of recent posts in a FaceBook group._
____
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Backbone of the [OxBot](https://www.facebook.com/OxBot) FaceBook page.


### How does it work?
We proceed in 2 steps.

1. `collect.py` collects all recent posts from a FB page and saves it into a file.
2. `bot.py`takes the collected text corpus and generates a 3-gram language model. This model is then used to generate posts that should immitate the style of the collected posts.

### How to use it?

Firstly, you should install all the dependencies found in `requirements.txt`.

Use `collect.py` to collect the data. 
```
usage: collect.py [-h] [--pages PAGES [PAGES ...]] [-d DEPTH]
Data Collection Script
arguments:
  -h, --help            show this help message and exit
  --pages PAGES [PAGES ...]
                        List the pages you want to scrape
                        for recent posts
  
  -d DEPTH, --depth DEPTH
                        How many recent posts you want to gather in
                        multiples of (roughly) 15.
```
Example: ```python collect.py --pages page1 page2 page3 -d 20```
____
Then use `bot.py` to generate the posts.

```
usage: bot.py [-h] [-g G]

OxBot

optional arguments:
  -h, --help          show this help message and exit
  -g G, --generate G  Number of posts to generate.
```