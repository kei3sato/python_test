# -*- coding: shift_jis -*-
import pandas as pd
from typing import List, Dict, Any

def Categorical(df: pd.DataFrame, column: str, categories: list, ordered: bool = True) -> pd.Categorical:
    """
    データフレームの指定された列をカテゴリカルデータ型に変換します。

    引数:
        df (pd.DataFrame): カテゴリカル変換を行うデータフレーム。
        column (str): カテゴリカル変換を行うデータフレーム内の列名。
        categories (list): カテゴリカルデータのカテゴリのリスト。カテゴリの順序も指定できます。
        ordered (bool, optional): カテゴリカルデータが順序付きであるかどうか。デフォルトはTrue。

    戻り値:
        pd.Categorical: 指定された列をカテゴリカルデータ型に変換した結果。

    動作:
        指定されたデータフレームの列をpandasのCategorical型に変換し、指定されたカテゴリと順序（必要に応じて）を適用します。
    """
    return pd.Categorical(df[column], categories=categories, ordered=ordered)

def concatenate_dataframes(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """
    複数のデータフレームを縦方向に結合して、一つのデータフレームにします。

    引数:
        dfs (list): 結合するデータフレームのリスト。

    戻り値:
        pd.DataFrame: 結合されたデータフレーム。
    """
    if not dfs:
        raise ValueError("データフレームのリストが空です。")
    
    return pd.concat(dfs, axis=0, ignore_index=True)


def create_pivot_table(df: pd.DataFrame, values: str, index: List[str], columns: List[str], aggfunc: str = 'mean', margins: bool = False) -> pd.DataFrame:
    """
    指定されたDataFrameからピボットテーブルを作成します。

    引数:
        df (pd.DataFrame): ピボットテーブルを作成する元のデータフレーム。
        values (str): 集計する値の列名。
        index (list): ピボットテーブルの行ラベルとして使用する列名のリスト。
        columns (list): ピボットテーブルの列ラベルとして使用する列名のリスト。
        aggfunc (str, optional): 集計関数。デフォルトは 'mean'。
        margins (bool, optional): 行と列の合計を追加するかどうか。デフォルトはFalse。

    戻り値:
        pd.DataFrame: 作成されたピボットテーブル。
    """
    return pd.pivot_table(df, values=values, index=index, columns=columns, aggfunc=aggfunc, margins=margins)

def convert_to_datetime(df: pd.DataFrame, column: str, format: str | None = None) -> pd.DataFrame:
    """
    指定されたDataFrameの列を日付時刻型に変換します。

    引数:
        df (pd.DataFrame): 日付時刻型に変換するデータフレーム。
        column (str): 日付時刻型に変換する列名。
        format (str | None, optional): 日付時刻解析のためのフォーマット文字列。
                                       日付形式を指定しない場合は自動的に解析します。デフォルトはNone

    戻り値:
        pd.DataFrame: 指定された列を日付時刻型に変換したデータフレーム。
    """
    df[column] = pd.to_datetime(df[column], format=format)
    return df

def create_dataframe(data: Dict[str, List[Any]]) -> pd.DataFrame:
    """
    データを基にpandasのDataFrameを作成します。

    引数:
        data (dict): データフレームを作成するためのデータ。キーが列名、値がデータのリスト。

    戻り値:
        pd.DataFrame: 作成されたデータフレーム。
    """
    return pd.DataFrame(data)

def is_nan(value: Any) -> bool:
    """
    与えられた値がNaN（欠損値）かどうかを判定します。

    引数:
        value (Any): 判定する値。

    戻り値:
        bool: 値がNaNの場合はTrue、それ以外の場合はFalse。
    """
    return pd.isna(value)

def read_csv_to_dataframe(filepath: str, encoding: str | None = None) -> pd.DataFrame:
    """
    指定されたファイルパスからCSVファイルを読み込み、DataFrameを返します。

    引数:
        filepath (str): 読み込むCSVファイルのパス。
        encoding (str | None, optional): ファイルのエンコーディング。デフォルトはNone。

    戻り値:
        pd.DataFrame: 読み込まれたデータフレーム。
    """
    return pd.read_csv(filepath, encoding=encoding)

def read_excel_to_dataframe(filepath: str, sheet_name: str | None = None, skiprows: int | list[int] | None = None, usecols: list | str | None = None, names: list | None = None, header: int | list | None = 0) -> pd.DataFrame:
    """
    指定されたExcelファイルのシートからデータを読み込み、DataFrameを返します。

    引数:
        filepath (str): 読み込むExcelファイルのパス。
        sheet_name (str | None, optional): 読み込むシート名。デフォルトはNoneで、最初のシートを読み込みます。
        skiprows (int | list[int] | None, optional): スキップする行数。デフォルトはNone。
        usecols (list | str | None, optional): 読み込む列のリスト。デフォルトはNone。
        names (list | None, optional): 列名のリスト。デフォルトはNone。
        header (int | list | None, optional): ヘッダー行のインデックス。デフォルトは0。

    戻り値:
        pd.DataFrame: 読み込まれたデータフレーム。
    """
    return pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows, usecols=usecols, names=names, header=header)

def save_dataframe_to_excel(df: pd.DataFrame, filepath: str, sheet_name: str = 'Sheet1') -> None:
    """
    DataFrameを指定されたファイルパスのExcelファイルに保存します。

    引数:
        df (pd.DataFrame): 保存するデータフレーム。
        filepath (str): 保存先のExcelファイルのパス。
        sheet_name (str, optional): 保存するシート名。デフォルトは'Sheet1'。

    戻り値:
        なし
    """
    df.to_excel(filepath, sheet_name=sheet_name, index=False)

def create_empty_dataframe(num_columns: int) -> pd.DataFrame:
    """
    指定された列数を持つ空のDataFrameを作成します。

    引数:
        num_columns (int): 作成するDataFrameの列数。

    戻り値:
        pd.DataFrame: 指定された列数を持つ空のデータフレーム。
    """
    columns = [f'Column{i+1}' for i in range(num_columns)]
    return pd.DataFrame(columns=columns)

class DataFrameManager:
    """
    pandas DataFrame を管理するクラス。
    """

    def __init__(self, df: pd.DataFrame = None):
        """
        コンストラクタ。

        引数:
            df (pd.DataFrame, optional): 管理するデータフレーム。デフォルトはNone。
        """
        self.__df = df

    @property
    def dataframe(self) -> pd.DataFrame:
        """
        管理されているデータフレームを取得します。

        戻り値:
            pd.DataFrame: 管理されているデータフレーム。
        """
        return self.__df
    
    @dataframe.setter
    def dataframe(self, df: pd.DataFrame) -> None:
        """
        管理されているデータフレームを設定します。

        引数:
            df (pd.DataFrame): 設定するデータフレーム。
        """
        self.__df = df

    def has_column(self, column_name: str) -> bool:
        """
        指定された列名がデータフレームに存在するかを確認します。

        引数:
            column_name (str): 確認する列名。

        戻り値:
            bool: 列名が存在する場合はTrue、存在しない場合はFalse。
        """
        if self.__df is not None:
            return column_name in self.__df.columns
        return False
    
    def has_columns(self, column_names: List[str]) -> bool:
        """
        指定された複数の列名がデータフレームに存在するかを確認します。

        引数:
            column_names (List[str]): 確認する列名のリスト。

        戻り値:
            bool: 全ての列名が存在する場合はTrue、存在しない場合はFalse。
        """
        if self.__df is not None:
            return all(column in self.__df.columns for column in column_names)
        return False
    
    def rename_columns(self, columns_dict: Dict[str, str]) -> None:
        """
        DataFrame 内の列名を指定された辞書に基づいて変更します。

        引数:
            columns_dict (Dict[str, str]): 変更する列名の辞書。キーが現在の列名、値が新しい列名。

        戻り値:
            なし
        """
        if self.__df is not None:
            self.__df.rename(columns=columns_dict, inplace=True)