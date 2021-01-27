from django.db import models

# Create your models here.


class DeviceCore(models.Model):
    """ The core data of a device in the database"""

    # Fields - identification data
    product_family = models.CharField(
        max_length=32,
        help_text="the family of the product",
        null=False,
        blank=False,
        choices=["safety", "distance"],
        primary_key=False
    )

    product_name = models.CharField(
        max_length=32,
        help_text="the name of the product",
        null=False,
        blank=False,
        choices=["R2000", "R1000"],
        primary_key=False
    )

    device_id = models.CharField(
        max_length=32,
        help_text="the id of the device",
        null=False,
        blank=False,
        choices=["0000000000001", "000000000001"],
        primary_key=False
    )

    # Fields - timing data
    created = models.DateTimeField(
        auto_now_add=True
    )

    last_modified = models.DateTimeField(
        auto_now=True
    )


# TODO declare function of that model
# TODO declare other models