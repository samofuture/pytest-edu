import pandas as pd


def read_csv(filename: str) -> pd.DataFrame:

    df: pd.DataFrame = pd.read_csv(filename, index_col='Draw Date')
    df.index = pd.to_datetime(df.index)

    df.sort_index(inplace=True)

    df = split_drawings(df)

    return df


def pre_multiplier(df: pd.DataFrame) -> pd.DataFrame:

    start_date = pd.to_datetime('2011-01-17')
    pre_multiplier_df: pd.DataFrame = df[:start_date]
    # post_multiplier_df: pd.DataFrame = df[start_date:]

    return pre_multiplier_df


def post_multiplier(df: pd.DataFrame) -> pd.DataFrame:

    start_date = pd.to_datetime('2011-01-17')
    post_multiplier_df: pd.DataFrame = df[start_date:]

    return post_multiplier_df


def split_drawings(df: pd.DataFrame) -> pd.DataFrame:

    raw_drawings = [list(map(int, row.split())) for row in df['Winning Numbers']]
    ret_df = df

    drawings: list[list[int]] = [[], [], [], [], []]
    for drawing in raw_drawings:
        for index, num in enumerate(drawing):
            drawings[index].append(num)

    for draw_num, draw in enumerate(drawings):
        ret_df[f'#{draw_num+1}'] = draw

    return ret_df
