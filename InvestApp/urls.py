"""Defines URL patterns for your Application."""
from django.conf.urls import url

from . import views

urlpatterns = [
     # Home page
     url(r'^$', views.index, name='index'),

    # List of all ETFs.
    url(r'^etf_list/$', views.etf_list, name='etf_list'),

    # Pager for single ETF details
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
]