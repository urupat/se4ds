import logging
from scipy.stats import linregress
logging.basicConfig(filename="ch05_logs.log",
                    level=logging.DEBUG,
                    filemode="w",                    
                    format='%(asctime)s %(message)s') # ①

def fit_trendline(year_timestamps, data):
    logging.info("Running fit_trendline function")
    result = linregress(year_timestamps, data)
    slope = round(result.slope, 3)
    r_squared = round(result.rvalue**2, 3)
    logging.info(f"Completed analysis. Slope of the trendline is {slope}.")
    return slope, r_squared

women_in_parliament=[9.02, 9.01, 8.84, 8.84, 8.84]
timestamps= [2000, 2001, 2002, 2003, 2004]
fit_trendline(timestamps, women_in_parliament)
