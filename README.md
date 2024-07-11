# sys-resource-visualizer
This repository hosts a Python project designed to monitor and visualize disk usage and package counts over time on a system.
Disk Usage and Package Counts Monitor

This repository hosts a Python project designed to monitor and visualize disk usage and package counts over time on a system. The project collects data using system commands, stores the information in text files (memory.txt and packages.txt), and generates insightful plots using matplotlib. The visualizations provide clear insights into the system's disk capacity, usage patterns, and package installation trends, helping users understand resource allocation and software management over different time intervals.

Key Features:
Disk Usage Monitoring: Tracks disk capacity, used space, and free space changes.
Package Counts Analysis: Displays trends in installed package counts over time.
Automated Data Collection: Utilizes shell commands (df for disk usage and dpkg for package counts) to collect data at specified intervals.
Visualization: Generates plots using matplotlib for intuitive data interpretation.
Customization: Easily adaptable for different system configurations and visualization preferences.
Usage:
Clone the repository, install dependencies (matplotlib), and run the main script (main.py) to generate plots.
