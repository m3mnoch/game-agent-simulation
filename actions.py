import random


class ActionBundles:
    @staticmethod
    def fetch_actions(name):
        if name == "consumer":
            return [
                {"name": "collect", "target": "apple", "count": 1, "turns": 3},
                {"name": "consume", "target": "apple", "count": 1, "turns": 1}
            ]
        elif name == "collector":
            return [
                {"name": "collect", "target": "banana", "count": 1, "turns": 3},
                {"name": "trade", "target": "banana", "count": 1, "turns": 2}
            ]
        else:
            return []

    def perform_action(self, agent, action):
        if action["name"] == "collect":
            self.collect_item(agent)
        elif action["name"] == "consume":
            self.consume_item(agent)
        elif action["name"] == "trade":
            self.trade_item(agent)

    def collect_item(self, agent):
        item = random.choice(["apple", "banana", "orange"])
        quantity = random.randint(1, 10)

        if item in agent.inventory:
            agent.inventory[item] += quantity
        else:
            agent.inventory[item] = quantity

    def consume_item(self, agent):
        if agent.inventory:
            item = random.choice(list(agent.inventory.keys()))
            quantity = random.randint(1, agent.inventory[item])
            agent.inventory[item] -= quantity

            if agent.inventory[item] == 0:
                del agent.inventory[item]

    def trade_item(self, agent):
        if agent.inventory:
            item = random.choice(list(agent.inventory.keys()))
            quantity = random.randint(1, agent.inventory[item])
            agent.inventory[item] -= quantity

            if agent.inventory[item] == 0:
                del agent.inventory[item]
