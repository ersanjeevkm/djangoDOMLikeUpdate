from django.db import models

# Create your models here.


class Count(models.Model):
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def update_count(self, like=True):
        if like:
            self.likes += 1

        else:
            self.dislikes += 1
            print("hello, world!")
        self.save()
