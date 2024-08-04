# Website Performance Analysis Tool
## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation and Usage](#installation-and-usage)
5. [Code Explanation](#code-explanation)
6. [Visualizations](#visualizations)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Overview
This tool analyzes and visualizes website performance metrics using Google's PageSpeed Insights API. It provides insights into various performance aspects of multiple websites, allowing for easy comparison and analysis.

## Features
- Analyzes multiple websites using Google PageSpeed Insights API
- Extracts key performance metrics:
  - Overall Performance Score
  - First Contentful Paint (FCP)
  - Largest Contentful Paint (LCP)
  - Time to Interactive (TTI)
  - Cumulative Layout Shift (CLS)
- Generates various visualizations for easy comparison

## Prerequisites
- Python 3.x
- pip (Python package installer)
- Google PageSpeed Insights API key

## Installation and Usage
1. Clone the repository:
git clone [repository-url]

2. Navigate to the project directory:
cd website-performance-analysis-tool

3. Install required packages:
pip install requests matplotlib seaborn pandas plotly
4. Open the `website_analysis.py` file and replace the `api_key` variable with your Google PageSpeed Insights API key.

5. Run the script:

6. Follow the prompts to enter the number of websites and their URLs.

7. The script will analyze the websites and display various visualizations.

## Code Explanation
The main components of the code are:

1. `analyze_website(url, api_key)`: 
- Analyzes a single website using the PageSpeed Insights API
- Returns a dictionary of performance metrics

2. `visualize_data(data_list)`:
- Creates various visualizations based on the analyzed data
- Uses matplotlib, seaborn, and plotly for generating charts

3. Main execution:
- Prompts user for number of websites and URLs
- Calls `analyze_website()` for each URL
- Passes results to `visualize_data()` for visualization

## Visualizations
The tool generates the following visualizations:

1. Overall Performance Score of Different Websites (Bar Chart)
2. Performance Score (Pie Chart)
3. Distribution of Loading Times for Key Metrics (Boxplot)
4. Cumulative Layout Shift Scores by Website (Bar Chart)
5. Correlation Between Performance Metrics (Heatmap)
6. Relationship Between First and Largest Contentful Paint (Scatter Plot)
7. Distribution of Overall Performance Scores (Histogram)
8. Impact of Time to Interactive on Overall Performance (Scatter Plot)
9. Interactive Time Metrics Comparison (Plotly Bar Chart)

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

## License
[MIT]

## Contact
M. Lohith - mlohith1338@gmail.com

