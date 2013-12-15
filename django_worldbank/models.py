from django.db import models

import wbpy

from django_data_mirror.models import DataSource, ForeignKey

class WorldBankDataSource(DataSource):
    """
    Generate or update the schema code by running:
        ./manage.py data_mirror_analyze WorldBankDataSource
    """
    
    @classmethod
    def get_feeds(cls):
        api = wbpy.IndicatorAPI()
        yield 'Indicator', api.get_indicators(common_only=True).iteritems()
        yield 'Country', api.get_countries().iteritems()
        yield 'IndicatorData', {
            'id':{
                'indicator': ForeignKey('Indicator'),
                'country': ForeignKey('Country'),
                'year':1234,
                'value':1234.0,
            }
        }.iteritems()

class Indicator(models.Model):

    id = models.CharField(max_length=45, blank=False, null=False, primary_key=True, unique=True)
    sourceOrganization = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    source = models.ForeignKey(u'Source')
    topics = models.ManyToManyField(u'Topic')
    sourceNote = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "indicator"

class Country(models.Model):

    capitalCity = models.CharField(max_length=40, blank=True, null=True, primary_key=False, unique=False)
    name = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True, primary_key=False, unique=False)
    incomeLevel = models.ForeignKey(u'IncomeLevel')
    adminregion = models.ForeignKey(u'Adminregion')
    id = models.CharField(max_length=5, blank=False, null=False, primary_key=True, unique=True)
    longitude = models.CharField(max_length=20, blank=True, null=True, primary_key=False, unique=False)
    region = models.ForeignKey(u'Region')
    lendingType = models.ForeignKey(u'LendingType')

    class Meta:
        verbose_name = "country"

class Region(models.Model):

    value = models.CharField(max_length=90, blank=True, null=True, primary_key=False, unique=False)
    id = models.CharField(max_length=5, blank=False, null=False, primary_key=True, unique=True)

    class Meta:
        verbose_name = "region"

class Adminregion(models.Model):

    value = models.CharField(max_length=90, blank=True, null=True, primary_key=False, unique=False)
    id = models.CharField(max_length=5, blank=False, null=False, primary_key=True, unique=True)

    class Meta:
        verbose_name = "adminregion"

class Topic(models.Model):

    id = models.IntegerField(blank=False, null=False, primary_key=True, unique=True)
    value = models.CharField(max_length=65, blank=True, null=True, primary_key=False, unique=False)

    class Meta:
        verbose_name = "topic"

class Source(models.Model):

    id = models.IntegerField(blank=False, null=False, primary_key=True, unique=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "source"

class IndicatorData(models.Model):

    indicator = models.ForeignKey('Indicator')
    year = models.IntegerField(blank=True, null=True, primary_key=False, unique=False)
    country = models.ForeignKey('Country')
    value = models.IntegerField(blank=True, null=True, primary_key=False, unique=False)
    id = models.CharField(max_length=5, blank=False, null=False, primary_key=True, unique=True)

    class Meta:
        verbose_name = "indicator data"

class IncomeLevel(models.Model):

    value = models.CharField(max_length=40, blank=True, null=True, primary_key=False, unique=False)
    id = models.CharField(max_length=5, blank=False, null=False, primary_key=True, unique=True)

    class Meta:
        verbose_name = "income level"

class LendingType(models.Model):

    value = models.CharField(max_length=30, blank=True, null=True, primary_key=False, unique=False)
    id = models.CharField(max_length=5, blank=False, null=False, primary_key=True, unique=True)

    class Meta:
        verbose_name = "lending type"
