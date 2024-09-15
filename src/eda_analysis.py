import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def univariate_analysis(df):
    """
    Perform univariate analysis by plotting histograms for numerical columns
    and bar charts for categorical columns.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    # Plot histograms for numerical columns
    df[numerical_cols].hist(figsize=(12, 10))
    plt.suptitle('Histograms of Numerical Columns')
    plt.show()
    
    # Plot bar charts for categorical columns
    for col in categorical_cols:
        df[col].value_counts().plot(kind='bar', title=f'Distribution of {col}')
        plt.show()

def bivariate_analysis(df):
    """
    Perform bivariate analysis to explore relationships between variables.
    """
    # Scatter plot and correlation matrix
    sns.scatterplot(data=df, x='TotalPremium', y='TotalClaims', hue='PostalCode')
    plt.title('Scatter Plot of TotalPremium vs TotalClaims')
    plt.show()
    
    correlation_matrix = df[['TotalPremium', 'TotalClaims']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def data_comparison(df):
    """
    Compare data trends over geography.
    """
    df.groupby('PostalCode')['TotalPremium'].mean().plot(kind='bar')
    plt.title('Average TotalPremium by PostalCode')
    plt.show()

def creative_visualizations(df):
    """
    Create three creative plots to capture key insights.
    """
    # Trend over time example (assuming you have a 'Date' column)
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    df.set_index('TransactionMonth')['TotalPremium'].resample('ME').mean().plot()
    plt.title('Monthly Average TotalPremium')
    plt.show()
    
    # Pair plot
    sns.pairplot(df[['TotalPremium', 'TotalClaims', 'PostalCode']])
    plt.title('Pair Plot of TotalPremium, TotalClaims, and PostalCode')
    plt.show()
    
    # Heatmap of correlation matrix
    sns.heatmap(df[['TotalPremium', 'TotalClaims']].corr(), annot=True, cmap='coolwarm')
    plt.title('Heatmap of Correlations')
    plt.show()