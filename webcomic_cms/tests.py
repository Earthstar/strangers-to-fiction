import datetime
from django.test import TestCase
from webcomic_cms.models import Comic, NewsPost, Comment

# Create your tests here.
class ComicTestCase(TestCase):
    def setUp(self):
        Comic.objects.create(
            title="comic1",
            # I have no idea how storing images works
            image='comic1.png',
            alt_text='alt text 1',
            commentary='commentary 1',
            date_posted = datetime.date.today(),
            )
        Comic.objects.create(
            title="comic2",
            image='comic2.png',
            alt_text='alt text 2',
            commentary='commentary 2',
            date_posted = datetime.date.today(),
            )

    def test_comic_numbering(self):
        '''
        Check if comic numbering starts at 1 and increments.
        No guarentee that the id starts with 1
        '''
        comic1 = Comic.objects.get(title='comic1')
        comic2 = Comic.objects.get(title='comic2')
        self.assertEqual(comic1.number, 1)
        self.assertEqual(comic2.number, 2)

    def test_comic_images(self):
        '''
        Check that URLs of the images are correct
        '''
        comic1 = Comic.objects.get(title='comic1')
        comic2 = Comic.objects.get(title='comic2')
        # This is the full file path
        self.assertEqual(comic1.image.path, '/home/earthstar/Documents/WebDev/webcomic-stf/strangers-to-fiction/webcomic_cms/comics/comic1.png')
        self.assertEqual(comic1.image.name, 'comic1.png')
        # image.url is the same as image.name in this test environment

class CommentTestCase(TestCase):
    def setUp(self):
        comic1 = Comic.objects.create(
            title="comic1",
            # I have no idea how storing images works
            image='comic1.png',
            alt_text='alt text 1',
            commentary='commentary 1',
            date_posted = datetime.date.today(),
            )
        news1 = NewsPost.objects.create(
            text='Blah blah blah')
        comment1 = Comment.objects.create(
            text='comment1',
            username='Harry Potter',
            parent_comic=comic1,
            )
        comment2 = Comment.objects.create(
            text='comment2',
            username='Ron Weasley',
            parent_news=news1)
        comment3 = Comment.objects.create(
            text='comment3',
            username='Granger')

    def test_comic_parent(self):
        comment1 = Comment.objects.get(text='comment1')
        self.assertEqual(comment1.get_parent_class(), Comic)
        comment2 = Comment.objects.get(text='comment2')
        self.assertEqual(comment2.get_parent_class(), NewsPost)
        comment3 = Comment.objects.get(text='comment3')
        self.assertRaises(Exception, comment3.get_parent_class)

