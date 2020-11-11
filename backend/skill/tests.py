from django.test import TestCase

from backend.skill.models import Skill


class SomeModelModelTest(TestCase):

    def test_name_content(self):
        Skill.objects.create(name='test_name')
        skill = Skill.objects.get(id=1)
        expected_object_name = f'{skill.name}'
        self.assertEqual(expected_object_name, 'test_name')
