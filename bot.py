import argparse
import markovify


# Parsing user argument
parser = argparse.ArgumentParser(description='OxBot')

# number of posts to generate
parser.add_argument("-g", '--generate', action="store",
                    type=int, dest="g", default=10, help="Number of posts to generate.")

args = parser.parse_args()

with open("corpus.txt", "r") as f:
    posts = f.read()
    # generate model
    model = markovify.Text(posts)
    for i in range(args.g):
        post = model.make_sentence()
        if post is None:
            pass
        else:
            print(post)
