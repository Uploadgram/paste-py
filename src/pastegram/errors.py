class ParseError(Exception):
    """Raised when an error occurred while parsing (from user input and not)"""
    pass

class APIError(Exception):
    """Raised when an error has occurred while fetching/parsing an API response"""
    pass