import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    file = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        x=file["Year"],
        y=file["CSIRO Adjusted Sea Level"],
        color="blue",
        alpha=0.5
    )


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(file["Year"], file["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = slope * x_pred + intercept
    plt.plot(
        x_pred, 
        y_pred, 
        color="red", 
        label="Best Fit Line (1880-2050)"
        )

    # Create second line of best fit
    recent = file[file["Year"] >= 2000] 
    slope, intercept, r_value, p_value, std_err = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series(range(2000, 2051))
    y_pred = slope * x_pred + intercept
    plt.plot(
        x_pred, 
        y_pred, 
        color="green", 
        label="Best Fit Line (2000-2050)"
        )


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()