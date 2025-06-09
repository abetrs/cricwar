# The Cricket Project

An open-source cricket analytics platform that aims to democratize advanced cricket statistics by providing sabermetric-style analysis tools to hobbyists, journalists, and cricket enthusiasts.

## Project Vision

This project strives to do for cricket what sabermetrics did for baseball - make advanced statistical analysis accessible to everyone. By processing and analyzing detailed ball-by-ball data from [Cricsheet](https://cricsheet.org/), we're building tools that enable:

- Hobbyist analysts to perform professional-grade cricket analysis
- Journalists to support their stories with advanced metrics
- Cricket enthusiasts to better understand the game through data
- Researchers to conduct reproducible cricket analytics studies

## Project Overview

The project processes detailed ball-by-ball cricket match data to generate advanced analytics and insights. Our focus is on:
- Creating accessible metrics similar to baseball's sabermetrics
- Providing clean, analyzed data ready for further research
- Building open-source tools for cricket analysis
- Democratizing access to advanced cricket statistics



## Project Structure

```
.
├── Tests/              # Test matches analysis
│   ├── tests_json/    # Processed Test match data from Cricsheet
│   └── test_analytics.ipynb  # Analysis notebooks
├── IPL/               # IPL analysis
├── ipl_json/          # Processed IPL match data
├── .gitignore
├── tests_json.zip     # Compressed Test match data
└── ipl_json.zip       # Compressed IPL match data
```

## Data Sources

The project primarily uses data from [Cricsheet](https://cricsheet.org/), a valuable open data initiative that provides detailed ball-by-ball cricket match data. We focus on:
- International Test matches
- Indian Premier League (IPL) matches
- Other major cricket competitions (planned)

## Analysis Capabilities

The project enables analysis of:
- Advanced batting metrics (similar to baseball's WAR, OPS+)
- Bowling effectiveness measures
- Match situation analysis
- Player value assessment
- Historical performance trends
- Game state analysis
- Win probability calculations
- Player comparison tools

## Getting Started

1. Clone the repository
2. Extract the match data from `tests_json.zip` and `ipl_json.zip`
3. Open the Jupyter notebooks to run analyses
4. Contribute your own analysis and metrics

## Current Status

This project is actively under development. We are:

- Processing and cleaning Cricsheet data
- Developing new cricket analytics metrics
- Building analysis tools and visualizations
- Creating documentation and examples
- Welcoming community contributions

## Future Goals

- Implement more advanced metrics
- Add interactive analysis tools
- Create visualization dashboards
- Develop predictive models
- Build an API for data access
- Expand to more cricket formats
- Create educational resources

## Acknowledgments

This project builds on the work of:

- [Cricsheet](https://cricsheet.org/) for providing open cricket data
- The baseball sabermetrics community for inspiring this approach
- Various cricket statisticians and analysts who have contributed to the field
