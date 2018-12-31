import argparse
import markovify


# Parsing user argument
parser = argparse.ArgumentParser(description='OxBot')

# number of posts to generate
parser.add_argument("-g", '--generate', action="store",
                    type=int, dest="g", default=10, help="Number of posts to generate.")

args = parser.parse_args()


posts_file = open("corpus.txt", "r", encoding='utf-8')
posts = posts_file.read()
# generate model
post_model = markovify.Text(posts)
for i in range(args.g):
    post = post_model.make_sentence()
    if post == None:
        pass
    else:
        print(post)
