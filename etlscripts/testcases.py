import logging
import pandas as pd

"""
Test cases on vehicle data

"""

def test_vehicle_df(df:pd.DataFrame):
  
  # Tests if all values in the 'Fuel Type' column are in 
  # ['Petrol and electric hybrid', 'Electric', 'Petrol or Diesel plug-in hybrid electric', 'Diesel and electric hybrid']

  allowed_values = ['Petrol and electric hybrid', 'Electric', 'Petrol or Diesel plug-in hybrid electric', 'Diesel and electric hybrid']
  assert df['Fuel Type'].isin(allowed_values).all(), "Fuel Type column values should be in {}".format(allowed_values)

  # Tests if all values in the specified column are greater than or equal to 0 and of integer type.
  assert (df["Count"] >= 0).all(), f"All values in column 'Count' must be greater than or equal to 0"
  
  # Check if the column data type is integer
  assert df["Count"].dtype == 'int64', f"Column 'Count' must be of integer type"

"""
Test Cases on Charging data

"""

def test_charging_points_df(df: pd.DataFrame,names: list):
    
  # Test if all values in the 'Country' column are 'RoI'.
  assert (df['Country'] == 'RoI').all(), "Country column should contain only 'RoI'"
  
  # Check county column values in the list of county names
  assert df['County'].isin(names).all(), "Fuel Type column values should be in {}".format(names)