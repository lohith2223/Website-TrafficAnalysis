import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
import warnings

# Suppress specific seaborn warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, module="seaborn")

def analyze_website(url, api_key):
    if not url.startswith("https://"):
        url = "https://" + url

    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}&strategy=mobile"
    try:
        response = requests.get(api_url)
        data = response.json()
        # Extract relevant metrics
        performance_score = data['lighthouseResult']['categories']['performance']['score'] * 100
        fcp = float(data['lighthouseResult']['audits']['first-contentful-paint']['numericValue']) / 1000
        lcp = float(data['lighthouseResult']['audits']['largest-contentful-paint']['numericValue']) / 1000
        tti = float(data['lighthouseResult']['audits']['interactive']['numericValue']) / 1000
        cls = float(data['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue'])
        return {
            'url': url,
            'Performance Score': performance_score,
            'First Contentful Paint': fcp,
            'Largest Contentful Paint': lcp,
            'Time to Interactive': tti,
            'Cumulative Layout Shift': cls
        }
    except Exception as e:
        print(f"Error analyzing {url}: {str(e)}")
        return None

def visualize_data(data_list):
    if not data_list or all(data is None for data in data_list):
        print("No websites were successfully analyzed. Please check URLs and API key.")
        return

    # Convert data to pandas DataFrame
    website_df = pd.DataFrame(data_list)

    if website_df.empty:
        print("No data available for visualization.")
        return

    # Separate URL column and numerical data
    urls = website_df['url']
    numerical_df = website_df.drop('url', axis=1)

    # Handle cases with less data
    num_metrics = len(numerical_df.columns)
    num_plots = min(num_metrics + 1, 9)  # Maximum of 9 plots in a 3x3 grid

    plt.figure(figsize=(20, 20))
    plt.suptitle('Website Performance Analysis - Multiple Websites', fontsize=18)

    if num_metrics >= 1:
        # Overall Performance Score of Different Websites (Bar Chart)
        plt.subplot(3, 3, 1)
        plt.bar(urls, numerical_df['Performance Score'])
        plt.title('Overall Performance Score of Different Websites')
        plt.xticks(rotation=90, ha='right')
        plt.ylabel('Score')

    if num_metrics >= 2:
        # Performance Score (Pie Chart)
        plt.subplot(3, 3, 2)
        for index, row in numerical_df.iterrows():
            plt.pie([row['Performance Score'], 100 - row['Performance Score']],
                    labels=['Score', 'Remaining'], autopct='%1.1f%%', startangle=90)
            plt.title(f'Performance Score - {urls[index]}')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    if num_metrics >= 3:
        # Distribution of Loading Times for Key Metrics (Boxplot)
        time_metrics = ['First Contentful Paint', 'Largest Contentful Paint', 'Time to Interactive']
        plt.subplot(3, 3, 3)
        numerical_df_melted = numerical_df[time_metrics].melt(var_name='metric', value_name='value')
        sns.boxplot(x='metric', y='value', data=numerical_df_melted)
        plt.title('Distribution of Loading Times for Key Metrics')
        plt.ylabel('Seconds')

    if num_metrics >= 4:
        # Cumulative Layout Shift Scores by Website (Bar Chart)
        plt.subplot(3, 3, 4)
        plt.bar(urls, numerical_df['Cumulative Layout Shift'])
        plt.title('Cumulative Layout Shift Scores by Website')
        plt.xticks(rotation=90, ha='right')
        plt.ylabel('CLS Score')

    if num_metrics >= 5:
        # Correlation Between Performance Metrics (Heatmap)
        plt.subplot(3, 3, 5)
        corr_matrix = numerical_df.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
        plt.title('Correlation Between Performance Metrics')

    if num_metrics >= 6:
        # Relationship Between First and Largest Contentful Paint (Scatter Plot)
        plt.subplot(3, 3, 6)
        plt.scatter(numerical_df['First Contentful Paint'], numerical_df['Largest Contentful Paint'])
        plt.xlabel('First Contentful Paint (s)')
        plt.ylabel('Largest Contentful Paint (s)')
        plt.title('Relationship Between First and Largest Contentful Paint')

    if num_metrics >= 7:
        # Distribution of Overall Performance Scores (Histogram)
        plt.subplot(3, 3, 7)
        plt.hist(numerical_df['Performance Score'], bins=10, edgecolor='black')
        plt.title('Distribution of Overall Performance Scores')
        plt.xlabel('Score')
        plt.ylabel('Frequency')

    if num_metrics >= 8:
        # Impact of Time to Interactive on Overall Performance (Scatter Plot)
        plt.subplot(3, 3, 8)
        plt.scatter(numerical_df['Time to Interactive'], numerical_df['Performance Score'])
        plt.xlabel('Time to Interactive (s)')
        plt.ylabel('Performance Score')
        plt.title('Impact of Time to Interactive on Overall Performance')

    if num_metrics >= 9:
        # Average Values of Key Performance Metrics (Treemap)
        plt.subplot(3, 3, 9)
        sizes = numerical_df[['First Contentful Paint', 'Largest Contentful Paint', 'Time to Interactive', 'Cumulative Layout Shift']].mean()
        if any(size == 0 for size in sizes):
            pass  # Do nothing if sizes contain zero
        else:
            squarify.plot(sizes=sizes, label=sizes.index, alpha=0.8)
            plt.title('Average Values of Key Performance Metrics')
            plt.axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # Interactive Plotly chart for Time Metrics Comparison
    fig = go.Figure()
    for metric in ['First Contentful Paint', 'Largest Contentful Paint', 'Time to Interactive']:
        if metric in numerical_df.columns:
            fig.add_trace(go.Bar(x=urls, y=numerical_df[metric], name=metric))

    fig.update_layout(
        title='Time Metrics Comparison',
        xaxis_title='Website',
        yaxis_title='Time (seconds)',
        barmode='group'
    )
    fig.show()

# Example usage
api_key = "AIzaSyBDU5xPPA-kMe0IlBsRvTQD-gljHC6mPNk"


# Enter website URLs manually
urls = []
num_websites = int(input("Enter the number of websites to analyze: "))
for i in range(num_websites):
    url = input(f"Enter the URL of website {i+1}: ")
    urls.append(url)

data_list = [analyze_website(url, api_key) for url in urls]
visualize_data(data_list)
