class When:
    def __init__(self, n):
        self.n = n
        self.it = iter()
        self.dic = {}

    def case(key, value):
        self.dic.setdefault(key, value)

    def when():
        