from django.db import models


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    target_mdfile = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(blank=True, null=True)
    updated_datetime = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posts'
