from . import TargetInfo


class iOSTargetInfo(TargetInfo):
    def __init__(self, arch):
        super().__init__('iOS', True, ['iOS_sdk'],
                         hosts=['Darwin'])
        self.arch = arch
