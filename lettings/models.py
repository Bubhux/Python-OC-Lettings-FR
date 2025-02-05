import logging

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


# Initialisation du logger
logger = logging.getLogger(__name__)


class Address(models.Model):
    """
    Représente une adresse avec différents champs tels que le numéro, la rue, la ville, etc.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Renvoie une représentation lisible par l'humain de l'adresse.
        """

        # Méthode logger_debug pour enregistrer des messages de débogage.
        logger.debug("Adresse convertie en chaîne : %s %s, %s %s, %s %s",
                     self.number,
                     self.street,
                     self.city,
                     self.state,
                     self.zip_code,
                     self.country_iso_code)

        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Représente une location avec un titre et une adresse associée.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Renvoie une représentation lisible par l'humain de la location.
        """

        # Méthode logger_debug pour enregistrer des messages de débogage.
        logger.debug("Location convertie en chaîne : %s, Adresse : %s", self.title, self.address)
        return self.title
