from django.db import models


class Candidate(models.Model):
    title = models.CharField(max_length=100)
    skill = models.ManyToManyField(
        'skill.Skill',
        verbose_name='skill',
        blank=False,
    )
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'candidate'
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    def get_skills(self):
        return "\n".join([s.name for s in self.skill.all()])
