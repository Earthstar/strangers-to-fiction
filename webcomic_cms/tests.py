import datetime
from django.test import TestCase
from webcomic_cms.models import Comic, NewsPost, Comment

# Create your tests here.
class ComicTestCase(TestCase):
    def setUp(self):
        Comic.objects.create(
            title="comic1",
            # I have no idea how storing images works
            image='test1.png',
            alt_text='alt text 1',
            commentary='commentary 1',
            date_posted = datetime.date.today(),
            )
        Comic.objects.create(
            title="comic2",
            image='test2.png',
            alt_text='alt text 1',
            commentary='commentary 1',
            date_posted = datetime.date.today(),
            )

    def test_comic_numbering(self):
        '''
        Check if comic numbering starts at 1 and increments.
        This doesn't seem to be the case?
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
        self.assertEqual(comic1.image.path, '/home/earthstar/Documents/WebDev/webcomic-stf/strangers-to-fiction/webcomic_cms/comics/test1.png')
        self.assertEqual(comic1.image.name, 'test1.png')
        # the URL seems to be
