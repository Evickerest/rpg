class Enemy:
    # Stats is a dict
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def getDefense(self):
        return self.stats["defense"]

    