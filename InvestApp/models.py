from django.db import models
from django.contrib.auth.models import User

class etf(models.Model):
    """The ETF model"""
    symbol = models.CharField(max_length=4)
    name = models.CharField(max_length=200)
    currentPrice = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return '%s %s $%s'%(self.symbol, self.name, self.currentPrice)