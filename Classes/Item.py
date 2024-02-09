import random

class Item:
    # Stats is a dictionary
    def __init__(self, stats):
        self.stats = stats
        self.assignStats()

    def assignStats(self):
        self.name = self.stats["name"]
        self.damage = self.stats["damage"]

        # What % Higher or % Lower from self.damage can possible damages be
        self.damagePercent = self.stats["damagePercent"]

        # In the format 0.%%
        self.critPercent = self.stats["critPercent"]

        # Chance of damage bypassing enemies defense
        self.armorBreakPercent = self.stats["armorBreakPercent"]

        ###### More stats can be added but idk

    # Enemy would be an instance of the enemy class
    def getDamageDealt(self, enemy):
        damageRangeValue = random.uniform( -self.damagePercent, self.damagePercent)
        baseDamageDealt = self.damage * damageRangeValue

        appliedDamage = baseDamageDealt
        if random.random() < self.critPercent:
            appliedDamage *= 2

        # If crit is 
        enemyDefenseReducer = 1
        if random.random() < self.armorBreakPercent:
            enemyDefenseReducer = 0.5

        enemyDefense = enemy.getDefense()

        return appliedDamage - enemyDefense * enemyDefenseReducer

        





