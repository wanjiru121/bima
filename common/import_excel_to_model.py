# import_excel_to_model.py

from tablib import Dataset
import pandas as pd
from common.models import County, SubCounty, Ward, Village, InsuranceData, UnitAreaOfInsurance
from import_export import resources

class InsuranceDataResource(resources.ModelResource):
    class Meta:
        model = InsuranceData

def get_or_create_county(name):
    return County.objects.get_or_create(name=name)[0]

def get_or_create_sub_county(county, name):
    return SubCounty.objects.get_or_create(county=county, name=name)[0]

def get_or_create_ward(sub_county, name):
    return Ward.objects.get_or_create(sub_county=sub_county, name=name)[0]

def get_or_create_village(ward, name):
    return Village.objects.get_or_create(ward=ward, name=name)[0]

def get_or_create_uai(identifier):
    return UnitAreaOfInsurance.objects.get_or_create(identifier=identifier)[0]

def import_excel_to_model(dataset):
    try:
        for row in dataset.dict:
            county = get_or_create_county(row['COUNTY'])
            sub_county = get_or_create_sub_county(county, row['SUB COUNTY'])
            ward = get_or_create_ward(sub_county, row['WARD'])
            village = get_or_create_village(ward, row['VILLAGE'])
            uai = get_or_create_uai(row['UAI'])

            insurance_data = InsuranceData(
                county=county,
                sub_county=sub_county,
                ward=ward,
                village=village,
                uai=uai,
                trigger=row['TRIGGER YIELD'],
                bag_price=row['BAG PRICE'],
                sum_insured=row['SUM INSURED'],
                actual_premium=row['ACTUAL PREMIUM'],
                rounded_premium=row['ROUNDED PREMIUM'],
                gok_premium_subsidy=row['GOK PREMIUM SUBSIDY'],
                farmer_premium=row['FARMER PREMIUM'],
            )
            insurance_data.save()

        print("Data imported successfully.")

    except FileNotFoundError as e:
        print(f"Error: File '{e}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
