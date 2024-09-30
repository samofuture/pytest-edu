import pytest
import pandas as pd
from lotto_analysis.process import read_csv, pre_multiplier, post_multiplier


@pytest.fixture(scope="session")
def data() -> pd.DataFrame:
    return read_csv("Mega-Millions-Winning-Numbers.csv")


def test_column_names(data):
    pass


def test_pre_multiplier_nan(data):
    pre_data = pre_multiplier(data)
    multiplier_list: list = list(pre_data['Multiplier'])
    nan_list = list(filter(lambda x: x != float('nan'), enumerate(multiplier_list)))

    assert len(nan_list) == len(multiplier_list)


def test_post_multiplier_nan(data):
    post_data = post_multiplier(data)
    multiplier_list: list = list(post_data['Multiplier'])
    nan_list = list(filter(lambda x: x != x, enumerate(multiplier_list)))

    assert len(nan_list) == 0


def test_split_drawings(data):
    for index, row in data.iterrows():
        processed_nums = [row.iloc[3], row.iloc[4], row.iloc[5], row.iloc[6], row.iloc[7]]
        assert list(map(int, row.iloc[0].split())) == processed_nums
