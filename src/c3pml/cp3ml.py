import typing

AnyCallable = typing.Callable[[...], typing.Any]


class C3PML:
    def __init__(self, model_reg):
        pass

    def train(self, func: AnyCallable):
        pass

    def validate(self, func: AnyCallable):
        pass

    def inference(self, func: AnyCallable):
        pass
