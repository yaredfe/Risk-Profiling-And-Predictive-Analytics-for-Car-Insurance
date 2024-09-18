import pandas as pd
from scipy import stats

def perform_anova_test(df: pd.DataFrame, kpi_column: str, group_column: str) -> float:
    """
    Perform ANOVA test to compare the mean of a KPI across different groups.
    
    Parameters:
    df (pd.DataFrame): The dataset.
    kpi_column (str): The KPI column to test.
    group_column (str): The grouping column (e.g., Province, PostalCode).
    
    Returns:
    float: p-value from the ANOVA test.
    """
    groups = [group[kpi_column].dropna() for name, group in df.groupby(group_column)]
    f_stat, p_value = stats.f_oneway(*groups)
    return p_value

def perform_t_test(df: pd.DataFrame, kpi_column: str) -> float:
    """
    Perform independent t-test to compare the mean of a KPI between two groups (e.g., male vs female).
    
    Parameters:
    df (pd.DataFrame): The dataset.
    kpi_column (str): The KPI column to test.
    
    Returns:
    float: p-value from the t-test.
    """
    group_a = df[df['Gender'] == 'Male'][kpi_column].dropna()
    group_b = df[df['Gender'] == 'Female'][kpi_column].dropna()
    t_stat, p_value = stats.ttest_ind(group_a, group_b)
    return p_value