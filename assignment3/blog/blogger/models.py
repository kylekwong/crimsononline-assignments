from django.db import models

# Class that represents authors
class Author(models.Model):
    first = models.CharField(max_length=128, blank=False, null=False)
    last = models.CharField(max_length=128, blank=False, null=False)
    gender = models.CharField(max_length=1, blank=False, null=False)

    def get_absolute_url(self):
        return '/authors/' + str(self.id)

    def give_backwards_name(self):
        return self.last + ' ' + self.first

    def get_gender(self):
        if self.gender.lower() == 'f':
            return 'Ms. '
        elif self.gender.lower() == 'm':
            return 'Mr. '
        else:
            return ''

    # String representation of author
    def __unicode__(self):
        return self.first + ' ' + self.last

class BlogPost(models.Model):
    # Relates each BlogPost to exactly one Author
    author = models.ForeignKey(Author, null=False)
    title = models.CharField(max_length=512, blank=False)
    post = models.TextField(blank=False, null=False)
    # If no time is given, default to time at which BlogPost is created
    time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return '/posts/' + str(self.id)

    def get_blurb(self):
        return self.post[0:100] + "..."

    # String representation of author
    def __unicode__(self):
        return self.title
