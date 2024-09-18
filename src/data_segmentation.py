import pandas as pd

def segment_data_by_province(df: pd.DataFrame) -> pd.DataFrame:
    """
    Segment the dataset by province.
    
    Parameters:
    df (pd.DataFrame): The original dataset.
    
    Returns:
    pd.DataFrame: The segmented dataset by province.
    """
    return df[['SumInsured', 'TotalPremium', 'TotalClaims', 'Province']].copy()

def segment_data_by_postal_code(df: pd.DataFrame) -> pd.DataFrame:
    """
    Segment the dataset by postal code.
    
    Parameters:
    df (pd.DataFrame): The original dataset.
    
    Returns:
    pd.DataFrame: The segmented dataset by postal code.
    """
    return df[['SumInsured', 'TotalPremium', 'TotalClaims', 'PostalCode']].copy()

def segment_data_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    Segment the dataset by gender.
    
    Parameters:
    df (pd.DataFrame): The original dataset.
    
    Returns:
    pd.DataFrame: The segmented dataset by gender.
    """
    return df[['SumInsured', 'TotalPremium', 'TotalClaims', 'Gender']].copy()

def segment_data_for_profit_margin(df: pd.DataFrame) -> pd.DataFrame:
    """
    Segment the dataset by postal code and prepare for profit margin testing.
    
    Parameters:
    df (pd.DataFrame): The original dataset with profit margin calculated.
    
    Returns:
    pd.DataFrame: The segmented dataset based on postal codes.
    """
    return df[['ProfitMargin', 'PostalCode']].copy()