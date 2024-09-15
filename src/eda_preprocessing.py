import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

def summarize_data(df):
    """
    Summarize data by providing descriptive statistics and data types.
    """
    describe = df.describe()
    dtype = df.dtypes
    buf = io.StringIO()
    df.info(buf=buf)
    info = buf.getvalue()
    # for line in info.splitlines():
    #     return line
    return describe,dtype,info

def assess_data_quality(df):
    """
    Assess data quality by checking for missing values.
    """
    return df.isnull().sum()

def preprocess_data(df):
    numeric_columns=df.select_dtypes(include='number').columns
    categorical_columns=df.select_dtypes(include="object").columns
    df[numeric_columns]=df[numeric_columns].fillna(df[numeric_columns].mean())
    df[categorical_columns]=df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
    return df

def check_skewness(df):
    numeric_columns=df.select_dtypes(include='number')
    skewness=numeric_columns.skew()
    return skewness

def detect_outliers(df):
    """
    Detect outliers using box plots for numerical columns.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    for col in numerical_cols:
        sns.boxplot(x=df[col])
        plt.title(f'Box Plot for {col}')
        plt.show()
        
        # Optionally return the rows with outliers
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
        df=df.drop(outliers.index,axis=0)

    