from django.db import models
from django.contrib.auth.models import User


class etf(models.Model):
    """The ETF model"""
    owner = models.ForeignKey(User)
    symbol = models.CharField(max_length=4)
    name = models.CharField(max_length=200)
    currentPrice = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        """Return a string representation of the model."""
        return '%s %s $%s'%(self.symbol, self.name, self.currentPrice)


class account(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    totalCashValue = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    totalStockValue = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    totalAccountValue = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        """Return a string representation of the model."""
        return '%s %s'%(self.name, self.type)


class accountBreakdown(models.Model):
    accountID = models.ForeignKey(account)
    etfID = models.ForeignKey(etf)
    quantity = models.IntegerField()
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return '%s %s %s'%(self.accountID, self.etfID, self.quantity)

