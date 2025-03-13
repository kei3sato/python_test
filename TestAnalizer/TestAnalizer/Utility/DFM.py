# -*- coding: shift_jis -*-
import pandas as pd
from typing import List, Dict, Any

def Categorical(df: pd.DataFrame, column: str, categories: list, ordered: bool = True) -> pd.Categorical:
    """
    �f�[�^�t���[���̎w�肳�ꂽ����J�e�S���J���f�[�^�^�ɕϊ����܂��B

    ����:
        df (pd.DataFrame): �J�e�S���J���ϊ����s���f�[�^�t���[���B
        column (str): �J�e�S���J���ϊ����s���f�[�^�t���[�����̗񖼁B
        categories (list): �J�e�S���J���f�[�^�̃J�e�S���̃��X�g�B�J�e�S���̏������w��ł��܂��B
        ordered (bool, optional): �J�e�S���J���f�[�^�������t���ł��邩�ǂ����B�f�t�H���g��True�B

    �߂�l:
        pd.Categorical: �w�肳�ꂽ����J�e�S���J���f�[�^�^�ɕϊ��������ʁB

    ����:
        �w�肳�ꂽ�f�[�^�t���[���̗��pandas��Categorical�^�ɕϊ����A�w�肳�ꂽ�J�e�S���Ə����i�K�v�ɉ����āj��K�p���܂��B
    """
    return pd.Categorical(df[column], categories=categories, ordered=ordered)

def concatenate_dataframes(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """
    �����̃f�[�^�t���[�����c�����Ɍ������āA��̃f�[�^�t���[���ɂ��܂��B

    ����:
        dfs (list): ��������f�[�^�t���[���̃��X�g�B

    �߂�l:
        pd.DataFrame: �������ꂽ�f�[�^�t���[���B
    """
    if not dfs:
        raise ValueError("�f�[�^�t���[���̃��X�g����ł��B")
    
    return pd.concat(dfs, axis=0, ignore_index=True)


def create_pivot_table(df: pd.DataFrame, values: str, index: List[str], columns: List[str], aggfunc: str = 'mean', margins: bool = False) -> pd.DataFrame:
    """
    �w�肳�ꂽDataFrame����s�{�b�g�e�[�u�����쐬���܂��B

    ����:
        df (pd.DataFrame): �s�{�b�g�e�[�u�����쐬���錳�̃f�[�^�t���[���B
        values (str): �W�v����l�̗񖼁B
        index (list): �s�{�b�g�e�[�u���̍s���x���Ƃ��Ďg�p����񖼂̃��X�g�B
        columns (list): �s�{�b�g�e�[�u���̗񃉃x���Ƃ��Ďg�p����񖼂̃��X�g�B
        aggfunc (str, optional): �W�v�֐��B�f�t�H���g�� 'mean'�B
        margins (bool, optional): �s�Ɨ�̍��v��ǉ����邩�ǂ����B�f�t�H���g��False�B

    �߂�l:
        pd.DataFrame: �쐬���ꂽ�s�{�b�g�e�[�u���B
    """
    return pd.pivot_table(df, values=values, index=index, columns=columns, aggfunc=aggfunc, margins=margins)

def convert_to_datetime(df: pd.DataFrame, column: str, format: str | None = None) -> pd.DataFrame:
    """
    �w�肳�ꂽDataFrame�̗����t�����^�ɕϊ����܂��B

    ����:
        df (pd.DataFrame): ���t�����^�ɕϊ�����f�[�^�t���[���B
        column (str): ���t�����^�ɕϊ�����񖼁B
        format (str | None, optional): ���t������͂̂��߂̃t�H�[�}�b�g������B
                                       ���t�`�����w�肵�Ȃ��ꍇ�͎����I�ɉ�͂��܂��B�f�t�H���g��None

    �߂�l:
        pd.DataFrame: �w�肳�ꂽ�����t�����^�ɕϊ������f�[�^�t���[���B
    """
    df[column] = pd.to_datetime(df[column], format=format)
    return df

def create_dataframe(data: Dict[str, List[Any]]) -> pd.DataFrame:
    """
    �f�[�^�����pandas��DataFrame���쐬���܂��B

    ����:
        data (dict): �f�[�^�t���[�����쐬���邽�߂̃f�[�^�B�L�[���񖼁A�l���f�[�^�̃��X�g�B

    �߂�l:
        pd.DataFrame: �쐬���ꂽ�f�[�^�t���[���B
    """
    return pd.DataFrame(data)

def is_nan(value: Any) -> bool:
    """
    �^����ꂽ�l��NaN�i�����l�j���ǂ����𔻒肵�܂��B

    ����:
        value (Any): ���肷��l�B

    �߂�l:
        bool: �l��NaN�̏ꍇ��True�A����ȊO�̏ꍇ��False�B
    """
    return pd.isna(value)

def read_csv_to_dataframe(filepath: str, encoding: str | None = None) -> pd.DataFrame:
    """
    �w�肳�ꂽ�t�@�C���p�X����CSV�t�@�C����ǂݍ��݁ADataFrame��Ԃ��܂��B

    ����:
        filepath (str): �ǂݍ���CSV�t�@�C���̃p�X�B
        encoding (str | None, optional): �t�@�C���̃G���R�[�f�B���O�B�f�t�H���g��None�B

    �߂�l:
        pd.DataFrame: �ǂݍ��܂ꂽ�f�[�^�t���[���B
    """
    return pd.read_csv(filepath, encoding=encoding)

def read_excel_to_dataframe(filepath: str, sheet_name: str | None = None, skiprows: int | list[int] | None = None, usecols: list | str | None = None, names: list | None = None, header: int | list | None = 0) -> pd.DataFrame:
    """
    �w�肳�ꂽExcel�t�@�C���̃V�[�g����f�[�^��ǂݍ��݁ADataFrame��Ԃ��܂��B

    ����:
        filepath (str): �ǂݍ���Excel�t�@�C���̃p�X�B
        sheet_name (str | None, optional): �ǂݍ��ރV�[�g���B�f�t�H���g��None�ŁA�ŏ��̃V�[�g��ǂݍ��݂܂��B
        skiprows (int | list[int] | None, optional): �X�L�b�v����s���B�f�t�H���g��None�B
        usecols (list | str | None, optional): �ǂݍ��ޗ�̃��X�g�B�f�t�H���g��None�B
        names (list | None, optional): �񖼂̃��X�g�B�f�t�H���g��None�B
        header (int | list | None, optional): �w�b�_�[�s�̃C���f�b�N�X�B�f�t�H���g��0�B

    �߂�l:
        pd.DataFrame: �ǂݍ��܂ꂽ�f�[�^�t���[���B
    """
    return pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows, usecols=usecols, names=names, header=header)

def save_dataframe_to_excel(df: pd.DataFrame, filepath: str, sheet_name: str = 'Sheet1') -> None:
    """
    DataFrame���w�肳�ꂽ�t�@�C���p�X��Excel�t�@�C���ɕۑ����܂��B

    ����:
        df (pd.DataFrame): �ۑ�����f�[�^�t���[���B
        filepath (str): �ۑ����Excel�t�@�C���̃p�X�B
        sheet_name (str, optional): �ۑ�����V�[�g���B�f�t�H���g��'Sheet1'�B

    �߂�l:
        �Ȃ�
    """
    df.to_excel(filepath, sheet_name=sheet_name, index=False)

def create_empty_dataframe(num_columns: int) -> pd.DataFrame:
    """
    �w�肳�ꂽ�񐔂������DataFrame���쐬���܂��B

    ����:
        num_columns (int): �쐬����DataFrame�̗񐔁B

    �߂�l:
        pd.DataFrame: �w�肳�ꂽ�񐔂�����̃f�[�^�t���[���B
    """
    columns = [f'Column{i+1}' for i in range(num_columns)]
    return pd.DataFrame(columns=columns)

class DataFrameManager:
    """
    pandas DataFrame ���Ǘ�����N���X�B
    """

    def __init__(self, df: pd.DataFrame = None):
        """
        �R���X�g���N�^�B

        ����:
            df (pd.DataFrame, optional): �Ǘ�����f�[�^�t���[���B�f�t�H���g��None�B
        """
        self.__df = df

    @property
    def dataframe(self) -> pd.DataFrame:
        """
        �Ǘ�����Ă���f�[�^�t���[�����擾���܂��B

        �߂�l:
            pd.DataFrame: �Ǘ�����Ă���f�[�^�t���[���B
        """
        return self.__df
    
    @dataframe.setter
    def dataframe(self, df: pd.DataFrame) -> None:
        """
        �Ǘ�����Ă���f�[�^�t���[����ݒ肵�܂��B

        ����:
            df (pd.DataFrame): �ݒ肷��f�[�^�t���[���B
        """
        self.__df = df

    def has_column(self, column_name: str) -> bool:
        """
        �w�肳�ꂽ�񖼂��f�[�^�t���[���ɑ��݂��邩���m�F���܂��B

        ����:
            column_name (str): �m�F����񖼁B

        �߂�l:
            bool: �񖼂����݂���ꍇ��True�A���݂��Ȃ��ꍇ��False�B
        """
        if self.__df is not None:
            return column_name in self.__df.columns
        return False
    
    def has_columns(self, column_names: List[str]) -> bool:
        """
        �w�肳�ꂽ�����̗񖼂��f�[�^�t���[���ɑ��݂��邩���m�F���܂��B

        ����:
            column_names (List[str]): �m�F����񖼂̃��X�g�B

        �߂�l:
            bool: �S�Ă̗񖼂����݂���ꍇ��True�A���݂��Ȃ��ꍇ��False�B
        """
        if self.__df is not None:
            return all(column in self.__df.columns for column in column_names)
        return False
    
    def rename_columns(self, columns_dict: Dict[str, str]) -> None:
        """
        DataFrame ���̗񖼂��w�肳�ꂽ�����Ɋ�Â��ĕύX���܂��B

        ����:
            columns_dict (Dict[str, str]): �ύX����񖼂̎����B�L�[�����݂̗񖼁A�l���V�����񖼁B

        �߂�l:
            �Ȃ�
        """
        if self.__df is not None:
            self.__df.rename(columns=columns_dict, inplace=True)