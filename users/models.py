from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators


class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name='email', null=True, blank=True)

    first_name = models.CharField(
        max_length=128,
        null=True,
        verbose_name='First name')

    last_name = models.CharField(
        max_length=128,
        null=True,
        verbose_name='Last name')

    mobile_number = models.CharField(
        unique=False,
        max_length=20,
        null=True,
        blank=True,
        # validators=[validators.RegexValidator(
        #    regex=r'^3(\d){9}$', message='Please entry a valid phone number.',
        # )],
        verbose_name='Phone number',
    )

    address = models.CharField(
        max_length=128, verbose_name='dirección',
        null=True,
        blank=True)

    document_type = models.CharField(
        null=True,
        blank=True,
        max_length=2,
    )

    document_number = models.CharField(
        null=True,
        blank=True,
        max_length=11,
        validators=[validators.RegexValidator(
            regex=r'^(\d)*$', message='Debe ser solo números',
        )],
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='actualizado el')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    def __str__(self):
        """Return username."""
        return str(self.pk) + ' - ' + self.email

    class Meta:
        ordering = ['id', 'email', ]
