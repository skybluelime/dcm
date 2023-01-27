from dataclasses import dataclass
import pandas as pd


@dataclass
class Filter:
    condition: str


class FilterStack:
    """
    _filters: Filter Object 의 집합
    """
    _filters: dict

    def __init__(self):
        pass

    def add_filter(self, filter_obj: Filter): ...
    def remove_filter(self, filter_obj: Filter): ...


class History:
    """
    데이터 변경 전 저장
    """
    pass


class HistoryStack:
    """
    History 아이템 의 이력성 관리
    """
    pass


class BaseDataControlDataObject:
    _origin_df: pd.DataFrame
    _df: pd.DataFrame
    """
    데이터 타입에 상관 없이 보여 주기 위한 Base class
    _origin_df: 원본 데이터프레임 보관
    _df: 현재 데이터 프레임
    _filters:
    """
    def __init__(self): ...
    def cell(self, row: int, column: int): ...


class OutputConverter:
    def __init__(self, data):
        self._data = data
    
    def to_list(self): ...
    def to_dict(self): ...
    def to_dataframe(self): ...

