import requests, pandas as pd, io, datetime, os

today_date = datetime.date.today().strftime("%Y-%m-%d")

urls = [
    ['Type1', 'https://www.nseindia.com/api/live-analysis-oi-spurts-underlyings?type=underlying&csv=true&partialFileName=By-Underlying'],
    ['Type2', 'https://www.nseindia.com/api/live-analysis-oi-spurts-contracts?type=Rise-in-OI-Rise&csv=true&partialFileName=Rise-in-OI-and-Rise-in-Price'],
    ['Type3', 'https://www.nseindia.com/api/live-analysis-oi-spurts-contracts?type=Rise-in-OI-Slide&csv=true&partialFileName=Rise-in-OI-and-Slide-in-Price'],
    ['Type4', 'https://www.nseindia.com/api/live-analysis-oi-spurts-contracts?type=Slide-in-OI-Slide&csv=true&partialFileName=Slide-in-OI-and-Slide-in-Price'],
    ['Type5', 'https://www.nseindia.com/api/live-analysis-oi-spurts-contracts?type=Slide-in-OI-Rise&csv=true&partialFileName=Slide-in-OI-and-Rise-in-Price']
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://google.com",
    "DNT": "1", # Do Not Track
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

dfs = []

os.makedirs('data', exist_ok=True)
path = os.path.join(os.getcwd(), 'data')


for type_i, url in urls:
  res = requests.get(url, headers=headers, timeout=10)
  df = pd.read_csv(io.StringIO(res.text))
  df.columns = ["Symbol"] + list(df.columns[1:])
  df.to_csv(os.path.join(path, f"{type_i}_{today_date}.csv"), index=False)
