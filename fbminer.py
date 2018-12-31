from selenium import webdriver
import time


class Collector(object):
    """Collector of recent FaceBook group posts.
           Note: We bypass the FaceBook-Graph-API by using a 
           selenium FireFox instance! 
           This is against the FB guidelines and thus not allowed.

           USE THIS FOR EDUCATIONAL PURPOSES ONLY. DO NOT ACTAULLY RUN IT.
    """

    def __init__(self, pages=["oxfess"], corpus_file="corpus.txt", depth=5, delay=2):
        super(Collector, self).__init__()
        self.pages = pages
        self.dump = corpus_file
        self.depth = depth
        self.delay = delay
        # browser instance
        self.browser = webdriver.Firefox()

    def strip(string):
        """Helping function to remove all non alphanumeric characters"""
        words = string.split()
        words = [word for word in words if "#" not in word]
        string = " ".join(words)
        clean = ""
        for c in string:
            if str.isalnum(c) or (c in [" ", ".", ","]):
                clean += c
        return clean

    def collect_page(self, page):
        # navigate to page
        self.browser.get('https://www.facebook.com/' + page + '/')

        # Scroll down depth-times and wait delay seconds to load
        for scroll in range(self.depth):

            # Scroll down to bottom
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(self.delay)

        # Once the full page is loaded, we can start scraping
        with open(self.dump, "a+") as corpus:

            paragraphs = self.browser.find_elements_by_css_selector(
                "[data-ad-preview='message'] p")

            for p in paragraphs:
                text = strip(p.text)
                corpus.write(text)

    def collect(self):
        for page in self.pages:
            self.collect_page(page)


# if __name__ == '__main__':
#     test = Collector(pages=["oxfess", "beaverconfessions"])
#     test.collect()
