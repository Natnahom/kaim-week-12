import pytest
import pandas as pd
from scripts.load_data import *
from scripts.EDA import *

def test_load_data():
    # Test loading data
    data = load_data("../../Data/raw_analyst_ratings.csv")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_perform_eda():
    # Test EDA functions
    data = pd.DataFrame({
        'headline': ['Stock prices rise', 'Market crashes'],
        'publisher': ['Publisher A', 'Publisher B'],
        'date': ['2023-01-01', '2023-01-02']
    })
    perform_eda(data)  # Ensure no errors are raised