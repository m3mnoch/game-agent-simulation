import random
from actions import ActionBundles


class Agent:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.log = []
        self.bundles = ActionBundles()
        self.actions = self.bundles.fetch_actions(name)

    def tick(self):
        self.log.append({
            "name": "ticking",
            "target": self.name,
            "count": 1,
            "message": f"{self.name} is ticking"
        })

        if self.actions:
            action = self.actions[0]
            action['turns'] -= 1

            if action['turns'] <= 0:
                action = self.actions.pop(0)
                self.log.append({
                    "name": action['name'],
                    "target": action['target'],
                    "count": action['count'],
                    "message": "completed action"
                })
                self.bundles.perform_action(self, action)

                # refresh their actions.
                if len(self.actions) == 0:
                    self.actions = self.bundles.fetch_actions(self.name)

            else:
                self.log.append({
                    "name": action['name'],
                    "target": action['target'],
                    "count": 0,  # we only add it when they succeed.
                    "message": "performing action"
                })

            # print("actions:", self.actions)
            return [action]

        return [{"name": "idle", "target": "self", "count": 1, "turns": 1}]

    def get_metrics(self):
        num_items = sum(self.inventory.values())
        num_unique_items = len(self.inventory)
        return num_items, num_unique_items, self.log
