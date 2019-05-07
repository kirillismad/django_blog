import math
from string import digits, ascii_letters, ascii_lowercase

import io
from PIL import Image
from random import randint, choices

from django.core.files import File

from blog.tests_utils.utils import patch_file
from datetime import date

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

    def _days_in_month(self, m_index):
        return 28 + (m_index + math.floor(m_index / 8)) % 2 + 2 % m_index + 2 * math.floor(1 / m_index)

    def get_date(self, day=None, month=None, year=None):
        if month is None:
            month = self.get_int(1, 12)

        if day is None:
            day = self.get_int(1, self._days_in_month(month))

        if year is None:
            year = self.get_int(1970, 2000)

        return date(year, month, day)
