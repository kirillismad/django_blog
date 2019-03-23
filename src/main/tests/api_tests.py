from blog.tests_utils import BaseTestCase, patch_storage


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

        r = self.client.post(self.url, data, format='multipart')

        self.assert201(r, r.json())


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

        self.assert200(r, r.json())
