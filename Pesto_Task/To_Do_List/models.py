from djongo import models

class Task(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ])

    def __str__(self):
        return self.title
