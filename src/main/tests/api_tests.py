from blog.tests_utils import BaseTestCase, patch_storage, ProfileAPITestCase
from pprint import pprint
from random import sample

print = pprint

MULTIPART = 'multipart'


class TestSignUpView(BaseTestCase):
    VIEW = 'api:sign_up'

    @patch_storage
    def test_post(self):
        password = self.main_factory.get_password()
        data = {
            'email': self.main_factory.get_email(),
            'password': password,
            'confirm_password': password,
            'first_name': self.main_factory.get_name(),
            'last_name': self.main_factory.get_name(),
            'avatar': self.primitive_factory.get_image(),
            'wallpaper': self.primitive_factory.get_image(),
        }

        r = self.client.post(self.url, data, format=MULTIPART)

        self.assert201(r)


class TestSignInView(BaseTestCase):
    VIEW = 'api:sign_in'

    def test_post(self):
        password = self.main_factory.get_password()
        profile = self.main_factory.get_profile(user=self.main_factory.get_user(password=password))

        data = {
            'email': profile.user.email,
            'password': password,
        }

        r = self.client.post(self.url, data=data)

        self.assert200(r)


class TestPostView(ProfileAPITestCase):
    VIEW = 'api:posts'

    def get_tags(self):
        TAGS = 5
        return [self.main_factory.get_tag() for _ in range(TAGS)]

    def arrange(self):
        tags = self.get_tags()
        AUTHORS = 2
        self.POSTS = 2
        COMMENTS = 2
        for _a in range(AUTHORS):
            author = self.main_factory.get_profile()
            for _p in range(self.POSTS):
                post = self.main_factory.get_post(author=author)
                post.tags.set(sample(tags, k=2))
                for _c in range(COMMENTS):
                    self.main_factory.get_comment(post=post)

    def test_get(self):
        self.arrange()
        r = self.client.get(self.url)
        self.assert200(r)
        self.assertEqual(len(r.json()['results']), self.POSTS)

    def test_get_page_2(self):
        self.arrange()
        r = self.client.get(self.url, {'page': 2})
        self.assert200(r)
        self.assertEqual(len(r.json()['results']), self.POSTS)

    @patch_storage
    def test_post(self):
        data = {
            'tags': [tag.pk for tag in self.get_tags()[::2]],
            'title': self.primitive_factory.get_title(),
            'image': self.primitive_factory.get_image(),
            'text': self.primitive_factory.get_text(5),
        }

        r = self.client.post(self.url, data, format=MULTIPART)

        self.assert201(r)


class TestPostDetailViewAsAuthor(ProfileAPITestCase):
    VIEW = 'api:posts_detail'

    def setUp(self):
        super().setUp()
        self.post = self.main_factory.get_post(author=self.profile, tags_count=2)

    def get_reverse_kwargs(self):
        return {'id': self.post.pk}

    def test_get(self):
        r = self.client.get(self.url)
        self.assert200(r)

    def test_put(self):
        data = {
            'tags': [self.main_factory.get_tag().pk for _ in range(2)],
            'title': self.primitive_factory.get_title(),
            'image': self.primitive_factory.get_image(),
            'text': self.primitive_factory.get_text(10),
        }

        r = self.client.put(self.url, data, format=MULTIPART)

        self.assert200(r)

    def test_patch(self):
        data = {
            'title': self.primitive_factory.get_title(),
            'text': self.primitive_factory.get_text(5),
        }

        r = self.client.patch(self.url, data)

        self.assert200(r)
        self.post.refresh_from_db(fields=['title', 'text'])
        self.assertEqual(self.post.title, data['title'])
        self.assertEqual(self.post.text, data['text'])


class TestPostDetailViewAsProfile(ProfileAPITestCase):
    VIEW = 'api:posts_detail'

    def setUp(self):
        super().setUp()
        self.post = self.main_factory.get_post(tags_count=2)

    def get_reverse_kwargs(self):
        return {'id': self.post.pk}

    def test_get(self):
        r = self.client.get(self.url)
        self.assert200(r)

    def test_put(self):
        r = self.client.put(self.url, {})
        self.assert403(r)

    def test_patch(self):
        r = self.client.put(self.url, {})
        self.assert403(r)


class TestCommentView(ProfileAPITestCase):
    VIEW = 'api:comments'


class TestCommentDetailView(ProfileAPITestCase):
    VIEW = 'api:comments_detail'


class TestTagView(ProfileAPITestCase):
    VIEW = 'api:tags'


class TestTagPostsView(ProfileAPITestCase):
    VIEW = 'api:tags_detail_posts'


class TestProfileView(ProfileAPITestCase):
    VIEW = 'api:profiles'


class TestProfileDetailView(ProfileAPITestCase):
    VIEW = 'api:profiles_detail'


class TestProfilePostView(ProfileAPITestCase):
    VIEW = 'api:profile_detail_posts'


class TestProfileSelfView(ProfileAPITestCase):
    VIEW = 'api:self'
