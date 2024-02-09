class Character:
    # Stats is a dict
    def __init__(self, name, stats):
        self.name = name
        self.inventory = []
        self.stats = stats

    # Add to the inventory an instance of an item
    def addItem(self, item):
        self.inventory.append( item )

    # Upgrade stats by stat and amount
    def upgradeStats(self, stat, amount):
        self.stats[stat] += amount

    