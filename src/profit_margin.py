import pandas as pd

def calculate_profit_margin(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the profit margin from TotalPremium and TotalClaims.
    
    Parameters:
    df (pd.DataFrame): The original dataset.
    
    Returns:
    pd.DataFrame: The dataset with a new column 'ProfitMargin'.
    """
    df['ProfitMargin'] = df['TotalPremium'] - df['TotalClaims']
    return df