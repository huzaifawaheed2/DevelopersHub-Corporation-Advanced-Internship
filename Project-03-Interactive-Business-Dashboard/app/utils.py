def format_currency(value):
    """
    Format numeric value as USD.
    """

    return f"${value:,.2f}"


def format_number(value):
    """
    Format integer with commas.
    """

    return f"{value:,}"


def format_percentage(value):
    """
    Format percentage value.
    """

    return f"{value:.2f}%"