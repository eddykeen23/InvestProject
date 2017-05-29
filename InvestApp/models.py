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


class Account(models.Model):
    owner = models.ForeignKey(User)
    accountName = models.CharField(max_length=200)
    accountType = models.CharField(max_length=200)
    totalCashValue = models.DecimalField(max_digits=6, decimal_places=2)
    totalStockValue = DecimalField(max_digits=6, decimal_places=2)
    totalAccountValue = DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """Return a string representation of the model."""
        return self.accountName


class AccountBreakdown(models.Model):
    accountID = models.ForeignKey(Account)
    etfID = models.ForeignKey(etf)
    quantity = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return '%s %s %s'%(self.accountID, self.etfID, self.quantity)

