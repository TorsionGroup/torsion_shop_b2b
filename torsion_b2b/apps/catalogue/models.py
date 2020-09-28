from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    specification = models.CharField(max_length=250, null=True)

from oscar.apps.catalogue.models import *

