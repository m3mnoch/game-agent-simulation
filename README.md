# Game Agent Simulation

This is a simple agent simulation program that simulates the behavior of multiple agents performing actions.

## Getting Started

To run the agent simulation, follow these steps:

1. Clone the repository: `git clone https://github.com/m3mnoch/agent-simulation.git`
2. Navigate to the project directory: `cd agent-simulation`
3. Run the simulation: `python simulation.py`

## Usage

The agent simulation program consists of the following components:

- `Agent` class: Represents an agent with a name, inventory, and log of actions performed.
- `ActionBundles` class: Provides a mechanism to fetch actions for agents and perform actions.
- `print_report` function: Prints a report of the simulation results, including the number of agents, actions completed, and total number of items.

To customize the demonstration simulation, you can modify the following parameters in the `simulation.py` file:

- `ticks`: How many ticks/turns you want to simulate.
- `max_agents`: The maximum number of agents to simulate.
- `add_agents_interval`: How often to add agents.
- `num_agents_to_add`: How many agents to add at each interval.

However, it will be far more useful to modify the `actions.py` file to customize it with the specific actions you want your agents to take.

NOTE:  The agents are basically multi-threaded, so feel free to dump in as many as your system can handle.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](vscode-webview://0l5om06qsts4u5mli8s59cr08vvokmj53010pb30r3l486vgifbe/LICENSE) file for more information.

## Acknowledgements

This agent simulation program is inspired by various agent-based modeling and simulation techniques.

## Contact

For any questions or inquiries, please contact [chris@m3mnoch.com].

Thank you for using the agent simulation program!
