class Article:  
    def __init__(self, headline, content, creator):
        self.headline = headline
        self.content = content
        self.creator = creator
        self.related_image = None
    def save(self):
        import os.path
        filename = ""
        for i in range(1, 999):
            if not os.path.isfile("%s%d.txt" % (headline, i)):
                filename = "%s%d.txt" % (headline, i)
                break
        import json
        with open(filename, 'w+') as outfile:
            json.dump(self, outfile)
    def load(self, txtfile):
        try:
            f = open(txtfile)
        except IOError:
            print "File not found!"
    def show (self):
        return "Headline: {0}\nContent: {1}\nCreator: {2}\nRelated Image Info: {3}".format(self.headline, self.content, self.creator, self.related_image)

class Picture:
    def __init__(self, image_file, creator):
        self.image_file = image_file
        self.creator = creator
    def show(self):
        from PIL import Image
        im = Image.open(self.image_file)
    def __str__(self):
        return "Filepath: {0}\nCreator: {1}".format(self.image_file, self.creator)
