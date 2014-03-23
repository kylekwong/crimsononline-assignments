# Kyle Kwong

from datetime import date

from PIL import Image

import re

class Content(object):
    def __init__(self, title, subtitle, creator, date=date.today()):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.date = date

    def show(self):
        print '{0}:\n{1}\n{2}\n{3}'.format(self.title, self.subtitle, self.creator, self.date)

    def matches_url(self, url):

        modified = self.subtitle.replace(" ", "_")
        if re.match("http://thecrimson.com/%s/%d/%d/%d/%s" % (self, self.date.year, self.date.month, self.date.day, modified), url) == None:
            return False
        else:
            return True


class Article(Content):
    def __init__(self, title, teaser, creator, date, related_image=None):
        super(Article, self).__init__(title, teaser, creator, date)
        self.related_image = related_image

    def show(self):
        print '{0}:\n{1}\n{2}\n{3}'.format(self.title, self.subtitle, self.creator, self.date)

        if self.related_image:
            self.related_image.show()

    def matches_url(self, url):
        super(Article, self).matches_url(url)

class Picture(Content):
    def __init__(self, title, caption, creator, date, path):
        super(Picture, self).__init__(title, caption, creator, date)
        self.path = path

    def show(self):
        Image.open(self.path).show()

    def matches_url(self, url):
        super(Picture, self).matches_url(url)

'''
Question 1e
'''
def from_url(c_lst, url):

    # initialize counter, so if there is more than one content with same url, return error

    counter = 0

    returned_content = ""
    for content in c_lst:
        if content.matches_url(url):
            returned_content = content
            counter += 1
            if counter > 1:
                print "Error: More than one content matches URL."
                return

    return returned_content

'''
Question 1e
'''
def posted_after(c_lst, dt):
    contents = [content for content in c_lst if content.date > dt]
    return contents