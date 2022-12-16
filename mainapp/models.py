from django.db import models

# Create your models here.


class Recipient(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=150)
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )


class gift(models.Model):
    def __str__(self):
        return self.gift_name

    gift_name = models.CharField(max_length=150)
    price = models.FloatField()
    type = models.CharField(max_length=150)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    year = models.IntegerField()
