import unittest
from app.models import Comment,User,Pitch,Group

class TestComment(unittest.TestCase):
    def setUp(self):
        self.group_pick_up = Group( name="Pick-up lines" )
        self.user_jane = User(username = "Jane", password = "banana", email = "jane@doe.com" )
        self.new_line = Pitch( line_content="I am Groot", group = self.group_pick_up, user = self.user_jane )
        self.new_comment = Comment(comment_content="You need more practice")

    def test_instance(self):
        self.assertTrue( isinstance( self.new_comment, Comment) )

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue( len(Comment.query.all()) > 0)

    def test_get_comments(self):
        self.new_comment.save_comment()
        gotten_comments = Comment.get_comments(49)
        self.assertFalse( len(gotten_comments) == 1)


