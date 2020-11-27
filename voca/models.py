from django.db import models


"""
The profiles
"""
class Profile(models.Model):
    name = models.CharField(max_length=126)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

"""
All the words processed
"""
class MidnightOil(models.Model):
    word = models.CharField(max_length=52)
    burnt = models.BooleanField(default=False)
    already_know = models.BooleanField(default=False)
    learnt_date = models.DateTimeField('learnt_date', null=True, blank=True)
    added_word_date = models.DateTimeField('added_date', auto_now_add=True)
    number_of_tries = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
