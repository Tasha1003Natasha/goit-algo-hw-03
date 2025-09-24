from datetime import datetime

def get_days_from_today(date_string: str) -> int:
    """
    Calculate how many days separate the given date string from today.
    """
    formats = ("%Y-%m-%d", "%Y.%m.%d")

    parsed_date = None  
    for f in formats:
        try:
            parsed_date = datetime.strptime(date_string, f).date()
            break
        except ValueError:
            continue 
          

    if parsed_date is None:
        print(f"⚠️ Invalid date: '{date_string}'")
        return None
      

    now = datetime.today().date()
    delta = now - parsed_date
    return delta.days



