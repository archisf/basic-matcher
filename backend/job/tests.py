from django.test import TestCase

from job.models import Job
from skill.models import Skill


class JobModelTest(TestCase):
    test_skill = Skill.objects.create(name='test_name')
    test_job = Job.objects.create(title='test_title', skill=test_skill)

    def test_title_content(self):
        expected_object_title = f'{self.test_job.title}'
        self.assertEqual(expected_object_title, 'test_title')

    def test_skill_content(self):
        self.assertEqual(self.test_job.skill.id, self.test_skill.id)

