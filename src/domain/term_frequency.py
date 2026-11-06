from collections import Counter


def get_concordance(document: str) -> dict[str, int]:
    """Converts a string to a dictionary of words frequency."""
    if not isinstance(document, str):
        raise TypeError('The argument must be a string')
    
    return dict(Counter(document.lower().split(' ')))