from string import digits, ascii_letters, ascii_lowercase

import io
from PIL import Image
from random import randint, choices

from django.core.files import File

from blog.tests_utils.utils import patch_file

digits_letters = digits + ascii_letters


class PrimitiveFactory:
    def get_image(self, size=None, color=None) -> Image:
        file = io.BytesIO()
        if color is None:
            color = tuple(randint(0, 255) for _ in range(3))

        image = Image.new('RGB', size=size or (100, 100), color=color)
        image.save(file, 'png')
        file.name = f'{self.get_string(16)}.png'
        file.seek(0)
        return file

    def get_string(self, length: int = 7, *, alphabet=digits_letters) -> str:
        return ''.join(choices(alphabet, k=length))

    def get_text(self, words: int) -> str:
        result = ' '.join(self.get_string() for _ in range(words))
        return result

    def get_int(self, left=0, right=100) -> int:
        return randint(left, right)

    def get_title(self, length: int = 10) -> str:
        return self.get_string(length, alphabet=ascii_lowercase).capitalize()

    @patch_file
    def get_image_file(self, image_stream=None) -> File:
        return File(image_stream or self.get_image())
