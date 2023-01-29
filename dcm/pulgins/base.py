from PyQt5.Qt import QObject


class BasePluginWidget(QObject):
    """
    기본 창들을 제외한 작업들 은 플러그 인 방식 으로 생성 예정
    """
    def __init__(self, parent):
        super().__init__(parent)
        pass