import pandas as pd
import pprint
from process import read_csv, pre_multiplier, post_multiplier, split_drawings

if __name__ == "__main__":
    data_path = "Mega-Millions-Winning-Numbers.csv"
    df = read_csv(data_path)

