from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QObject, pyqtSignal, pyqtSlot


class BaseEventSignal(QObject):
    """
    공통 이벤트 시그널 class
    """
    started: pyqtSignal(bool)
    errored: pyqtSignal(bool)
    finished: pyqtSignal(bool)
    succeed: pyqtSignal(bool)


class BaseEventStatus(QObject):
    """
    위젯 상태 저장 class
    """
    is_started: bool
    is_running: bool
    is_finished: bool


class BaseWidget(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(BaseWidget, self).__init__(parent=None)
