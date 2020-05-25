from datetime import datetime
def get_sample_timeframe():
    now = datetime.today().date().isoformat()
    return now+"T00:00:00Z/"+now+"T23:59:59Z"