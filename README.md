# Tecta-Invest
A backend service built with FastAPI that retrieves historical stock market data from Yahoo Finance using the yfinance package, analyzes it and serves the results via a REST API.

# Legal disclaimer

Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.

yfinance is not affiliated, endorsed or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.

# Features

- Retrieve historical stock data for a given ticker symbol with an optional date range.
- Calculate basic statistics (high, low, average and last closing price)
- Data fetched on demand from Yahoo Finance.
- In-memory caching to improve performance for repeated queries.
- Containerized with Docker for easy deployment

# Tech Stack
- Python 3.11
- FastAPI
- yfinance
- Pandas
- Docker

# Installation

Local Development

1. Clone the repository:  
git clone https://github.com/Saurjyadeep/Tecta.git  
cd tecta

2. Create and activate a virtual environment
python -m venv venv  
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the API:    
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

# CI/CD Pipeline Outline using GitHub Actions

1. **Trigger**:
   - Run pipeline on every push to `main`
   - Run on pull requests

2. **Set up environment**:
   - Use Python 3.11
   - Install dependencies from `requirements.txt`

3. **Run automated tests**:
   - Use `pytest` or `unittest`
   - Ensure all tests pass

4. **Build Docker image**:
   - `docker build -t myusername/tecta-invest .`

5. **Push Docker image to registry**:
   - Authenticate with Docker Hub or GitHub Container Registry
   - `docker push myusername/tecta-invest`

6. **Deploy to server**:
   - Pull latest Docker image
   - Restart container on server

