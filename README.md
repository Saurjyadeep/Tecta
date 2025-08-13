Tecta Invest

A backend service built with FastAPI that retrieves historical stock market data from Yahoo Finance using the yfinance package, analyzes it and serves the results via a REST API.


Legal disclaimer

Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.

yfinance is not affiliated, endorsed or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.


Features

Retrieve historical stock data for a given ticker symbol with an optional date range.
Calculate basic statistics (high, low, average and last closing price)
Data fetched on demand from Yahoo Finance.
In-memory caching to improve performance for repeated queries.
Containerized with Docker for easy deployment

Tech Stack
Python 3.11

FastAPI

yfinance

pandas

Docker

Installation

Local Development

Clone the repository:
git clone https://github.com/yourusername/tecta-stock-api.git
cd tecta

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the API:    
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

5. Test in browser
Swagger docs: http://localhost:8000/docs


Running with Docker
1. Build the Docker image
docker build -t tecta-invest .

2. Run the container

docker run -p 8000:8000 tecta-invest

3. Test in browser
Swagger docs: http://localhost:8000/docs