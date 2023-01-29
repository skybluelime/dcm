from enum import Enum
from collections import deque
from dataclasses import dataclass
import pandas as pd
from PyQt5.QtCore import Qt
import logging

logger = logging.Logger(__name__)

"""
BaseDataControlDataObject: dcdo
"""


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

    def reset_filter(self):
        self._filters.clear()


class HistoryType(Enum):
    MODIFIED = 0
    FILTER_EVENT = 1
    REMOVE_ROW = 11
    INSERT_ROW = 12
    MOVE_ROW = 13
    REMOVE_COLUMN = 21
    INSERT_COLUMN = 22
    MOVE_COLUMN = 23


class History:
    history_type: HistoryType
    """
    화면 에서 데이터 관련 레이아웃이 변경될 시 변경 전 데이터를 저장 관리
    """
    def __init__(self, parent, history_type: HistoryType, data=None, index=None):
        """
        @TODO parent 오브젝트가 해제 되었을 시 History Object 해제 되는지 확인 필요
        @param parent: 이벤트가 발생한 부모 위젯
        @param history_type: Filter, remove_row(행삭제), insert_row(행삽입), modified(값변경), move_row(행이동),
                        remove_column(열삭제), insert_column(열삽입), move_column(열이동)
        @param data: Filter인 경우 이벤트를 적용, 취소
                     DataObject의 경우 변경전 데이터의 값, 인덱스 정보 등
        """
        self.parent = parent
        self.history_type = history_type
        self.data = data
        self.index = index


class HistoryStack:
    _undo_stack: deque
    _redo_stack: deque

    """
    History Object를 보관 관리
    되돌리기, 다시실행(undo, redo) 이벤트 관리   
    """
    def add_history(self, history: History):
        """
        @TODO parent 오브젝트가 해제 되었을 시 HistoryStack Object 해제 되는지 확인 필요
        #@고민 히스토리를 decorator로 제공해야 할지? instance 생성 방식으로 해야 할지?

        def add_to_history(func):
            @wraps(func)
            def wrapper(self, *args, **kw):
                self.history.append(func.__name__)
                return func(self, *args, **kw)
            return wrapper

        class MyClass(object):
            def __init__(self):
                self.history = []

            @add_to_history
            def methodA(self):
                return "method A"

            @add_to_history
            def methodB(self, input):
                return "method B %s" % input

            def methodC(self):
                return "methodC"



        inst = MyClass()
        print(inst.history)

        inst.methodA()
        print(inst.history)

        inst.methodB("myinput")
        print(inst.history)

        inst.methodC()
        print(inst.history)

        @param history:
        @return:
        """
        # self._current_index = 0

    def append_history(self, history: History):
        history_count = len(self._undo_stack)

        # redo deque에 저장된 데이터가 있으면 redo 초기화 하고 다시 쌓는다.
        if len(self._redo_stack) > 0:
            self._redo_stack.clear()

        self._undo_stack.append(history)

    def redo(self):
        if len(self._redo_stack) > 0:
            redo_item = self._undo_stack.pop()
            self._undo_stack.append(redo_item)
        return redo_item

    def undo(self):
        if len(self._undo_stack) > 0:
            undo_item = self._undo_stack.pop()
            self._redo_stack.append(undo_item)
        return undo_item


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

