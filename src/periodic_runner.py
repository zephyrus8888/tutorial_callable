from time import sleep


class PeriodicRunner:

    def __init__(self, period=1.0, callback=None, **kwargs):
        self.period = period
        self.callback = callback
        self.kwargs = kwargs

    def start(self):
        while True:
            sleep(self.period)
            if self.callback:
                self.callback(**self.kwargs)
