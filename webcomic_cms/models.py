from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Comic(models.Model):
    '''
    ./manage.py sqlclear webcomic_cms | ./manage.py dbshell
    Represents a comic entry.
    May want to add ability to queue posts in the future.
    title - title of comic
    number - number of comic.
    image - comic image data
    alt_text - alt text for comic, optional
    commentary - artist-submitted text specific to comic, optional
    date_posted - date from which the comic should be visible
    on the website
    '''
    title = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    # Actually stores an URL
    image = models.ImageField(upload_to='comics', max_length=255)
    alt_text = models.CharField(max_length=255, blank=True)
    commentary = models.TextField(blank=True)
    date_posted = models.DateField()

    def save(self, *args, **kwargs):
        '''
        Override save to set incrementing Comic.number
        '''
        # If there are no comics yet, set number to 1
        if Comic.objects.count() == 0:
            self.number = 1
        # If there is a comic, set number to one more than original
        else:
            # Get the number of the last comic posted
            self.number = 1 + Comic.objects.all().latest('date_posted').number
        super(Comic, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.number)

class NewsPost(models.Model):
    '''
    Represents a news post.
    text - text of news post
    datetime - date and time that the comic was posted
    TODO add ability to edit posts?
    '''
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

class Comment(models.Model):
    '''
    Represents a comment on a comic or a news post.
    text - the text of the comment
    datetime - the datetime that the comment was posted
    username - user's given name. May be blank, in which case anonymous post.
    parent_comic, parent_news - the parent which the comment is tied to.
    Need to validate that only one field is entered. Sort of hacky.
    '''
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255, blank=True)
    parent_comic = models.ForeignKey(Comic, blank=True, null=True)
    parent_news = models.ForeignKey(NewsPost, blank=True, null=True)

    def get_parent_class(self):
        '''
        Returns the class of the parent.
        '''
        if self.parent_comic and not self.parent_news:
            return Comic
        elif not self.parent_comic and self.parent_news:
            return NewsPost
        else:
            raise Exception('A Comment should have exactly one parent, but this comment has {0} parent(s)'.format(
                bool(self.parent_comic) + bool(self.parent_news)))

    def __unicode__(self):
        return self.text