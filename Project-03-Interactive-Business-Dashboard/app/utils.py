def format_currency(value):
    """
    Format a number as US Dollar currency.
    """
    
    return f"${value:,.2f}"

def format_number(value):
    """
    Format a number with comma separator.
    """
    
    return f"{value:,}"

def format_percentage(value):
    """
    Format a decimal value as percentage.
    """
    
    return f"{value:,.2f}%"