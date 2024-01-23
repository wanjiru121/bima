# common/models.py

from django.conf import settings
from django.db.models.deletion import SET_NULL
from django.db import models

class County(models.Model):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'Counties'


class SubCounty(models.Model):
    county = models.ForeignKey(
        County,
        on_delete=models.PROTECT,
        related_name='subcounties'
    )
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'Sub Counties'


class Ward(models.Model):
    sub_county = models.ForeignKey(
        SubCounty,
        on_delete=models.PROTECT,
        related_name="wards"
    )
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.name}"


class Village(models.Model):
    ward = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name='villages'
    )
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.name}"


class UnitAreaOfInsurance(models.Model):
    identifier = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.identifier}"

    class Meta:
        verbose_name_plural = 'Unit Area of Insurance'


class InsuranceData(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    uai = models.ForeignKey(UnitAreaOfInsurance, on_delete=models.CASCADE)
    trigger = models.DecimalField(max_digits=16, decimal_places=8)
    bag_price = models.DecimalField(max_digits=16, decimal_places=8)
    sum_insured = models.DecimalField(max_digits=16, decimal_places=8)
    actual_premium = models.DecimalField(max_digits=16, decimal_places=8)
    rounded_premium = models.DecimalField(max_digits=16, decimal_places=8)
    gok_premium_subsidy = models.DecimalField(max_digits=16, decimal_places=8)
    farmer_premium = models.DecimalField(max_digits=16, decimal_places=8)

    def __str__(self):
        return f"{self.county} - {self.sub_county} - {self.ward} - {self.village}"
    
    class Meta:
        verbose_name_plural = 'Insurance Data'

        unique_together = (
            "county",
            "sub_county",
            "ward",
            "village",
            "uai",
        )

