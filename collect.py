from fbminer import Collector
import argparse

parser = argparse.ArgumentParser(description='Data Collection')

parser.add_argument('--pages', nargs='+',
                    dest="pages",
                    help="List the pages you want to scrape for recent posts")

parser.add_argument("-d", "--depth", action="store",
                    dest="depth", default=5, type=int,
                    help="How many recent posts you want to gather -- in multiples of (roughly) 15.")

args = parser.parse_args()

# creating the Collector instance
OxCollect = Collector(pages=args.pages, depth=args.depth)

# generating corpus.txt
OxCollect.collect()
