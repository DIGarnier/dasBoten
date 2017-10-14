import b3

__all__ = ['Decorator']


class Decorator(b3.BaseNode):
    category = b3.DECORATOR

    def __init__(self, child=None):
        super().__init__()

        self.child = child or []
