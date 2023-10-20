import threading
import random
import time
from agent import Agent


def tick_agents(agents, actions_summary):
    for agent in agents:
        actions = agent.tick()  # Assuming tick() returns a list of actions taken by the agent
        for action in actions:
            if action["name"] in actions_summary:
                actions_summary[action["name"]] += 1
            else:
                actions_summary[action["name"]] = 1


def print_report(agents):
    # Print report after ticking is finished
    print("")
    print("=================================")
    print("---------------------------------")
    print("Report:")

    # Group agents by name
    agents_by_name = {}
    for agent in agents:
        agent_name = agent.name
        if agent_name in agents_by_name:
            agents_by_name[agent_name].append(agent)
        else:
            agents_by_name[agent_name] = [agent]

    # Print report for each agent name
    for agent_name, agent_list in agents_by_name.items():
        print(f"Agent Name: {agent_name}")
        print(f"- Number of Agents: {len(agent_list)}")

        # Aggregate log data
        actions_completed = {}
        total_num_items = 0
        total_num_unique_items = 0
        for agent in agent_list:
            num_items, num_unique_items, log = agent.get_metrics()
            total_num_items += num_items
            total_num_unique_items += num_unique_items
            for entry in log:
                action_name = entry['name']
                action_count = entry['count']
                if action_name in actions_completed:
                    actions_completed[action_name] += action_count
                else:
                    actions_completed[action_name] = action_count

        # Print aggregated log data
        print("- Actions Completed:")
        for action_name, action_count in actions_completed.items():
            print(f"  - {action_name}: {action_count} times")

        # Print total number of items
        print(f"- Inventory Count: {total_num_items}")
        print(f"- Unique Inventory Items: {total_num_unique_items}")
        print()

    print("=================================")


if __name__ == "__main__":

    # agents = [Agent("consumer")]
    agent_names = ["consumer", "collector", "observer"]
    agents = []
    num_agents = len(agents)
    ticks = 25
    max_agents = 1
    add_agents_interval = 1
    num_agents_to_add = 3

    threads = []
    for tick in range(ticks):
        print(f"Tick {tick+1}")
        actions_summary = {}
        tick_agents(agents, actions_summary)

        if len(agents) < num_agents_to_add:
            if (tick+1) % add_agents_interval == 0:
                for _ in range(num_agents_to_add):
                    agent_name = random.choice(agent_names)
                    new_agent = Agent(agent_name)
                    agents.append(new_agent)
                    num_agents += 1
                    thread = threading.Thread(target=new_agent.tick)
                    threads.append(thread)
                    thread.start()

        print("Agent Action Count Summary:")
        for action, count in actions_summary.items():
            print(f"-- {action}: {count}")

        time.sleep(0.2)

    for thread in threads:
        thread.join()

    print_report(agents)
