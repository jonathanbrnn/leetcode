class Foo:
    def __init__(self):
        self.called = 3


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.called -= 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.called != 2:
            pass
        if self.called == 2:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.called -= 1



    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.called != 1:
            pass
        if self.called == 1:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
            self.called -= 1
