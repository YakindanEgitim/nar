from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.date)


class Album(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.date)


class Song(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.date)
