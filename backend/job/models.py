from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    skill = models.ForeignKey(
        'skill.Skill',
        on_delete=models.PROTECT,
        verbose_name='skill',
        related_name='skill',
        blank=False,
        null=False
    )
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
