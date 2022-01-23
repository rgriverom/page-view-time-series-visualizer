import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])

# Clean data
top_percet_25 = (df['value'] >= df['value'].quantile(0.025))
bottom_percent_25 = (df['value'] <= df['value'].quantile(0.975))
df = df[top_percet_25 & bottom_percent_25]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    sns.lineplot(data=df, legend=False, palette=['r'])


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month_name()
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().reset_index(name="avg")
    # Draw bar plot
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    
    ax = sns.barplot(x="year", y="avg", data=df_bar, hue="month", ci="sd", hue_order=months, palette="tab10")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", loc="upper left")
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(32, 10), dpi=100)
    ax = sns.boxplot(x="year", y="value", data=df_box, ax=axs[0])
    ax.set_title("Year-wise Box Plot (Trend)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Page Views") 
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    ax = sns.boxplot(data=df_box, x="month", y="value", order=months, ax=axs[1])
    ax.set_title("Month-wise Box Plot (Seasonality)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Page Views") 
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
