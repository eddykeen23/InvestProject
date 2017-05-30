"""Defines URL patterns for your Application."""
from django.conf.urls import url

from . import views

urlpatterns = [
     # Home page
     url(r'^$', views.index, name='index'),

    # List of all ETFs.
    url(r'^etf_list/$', views.etf_list, name='etf_list'),

    # Page for single ETF details
    url(r'^etf_list/(?P<etf_id>\d+)/$', views.etf_details, name='etf_details'),

    # Page for adding a new ETF
    url(r'^new_etf/$', views.new_etf, name='new_etf'),

    # Page for editing an ETF
    url(r'^edit_etf/(?P<etf_id>\d+)/$', views.edit_etf, name='edit_etf'),

    # Deleting ETFs
    url(r'^delete_etf/(?P<etf_id>\d+)/$', views.delete_etf, name='delete_etf'),

    # Update Individual ETF Price
    url(r'^update_etf_price/(?P<etf_id>\d+)/$', views.update_etf_price, name='update_etf_price'),

    # Refresh All ETF Prices
    url(r'^refresh_etf_prices/$', views.refresh_etf_prices, name='refresh_etf_prices'),

    # List of all Accounts.
    url(r'^accounts_list/$', views.accounts_list, name='accounts_list'),

    # Pager for Account Details
    url(r'^accounts_list/(?P<account_id>\d+)/$', views.account_details, name='account_details'),

    # Page for adding a new Account
    url(r'^new_account/$', views.new_account, name='new_account'),

    # Deleting Accounts
    url(r'^delete_account/(?P<account_id>\d+)/$', views.delete_account, name='delete_account'),

    # Page for editing an Account
    url(r'^edit_account/(?P<account_id>\d+)/$', views.edit_account, name='edit_account'),

    # Page for adding an ETF to an Account
    url(r'^addETFtoAccount/(?P<account_id>\d+)/$', views.addETFtoAccount, name='addETFtoAccount'),

]