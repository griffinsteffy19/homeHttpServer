from django.db import models


class Source(models.Model):
    source_name = models.CharField(max_length=32)
    target_port = models.IntegerField(default=80)


class Target(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=32)
    local_ipaddr = models.CharField(max_length=32)
