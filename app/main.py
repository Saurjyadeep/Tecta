from fastapi import FastAPI, Query, HTTPException
from app.stocks import get_stocks_data
from typing import Optional

app = FastAPI(title="Tecta Invest")

@app.get("/api/stats")

def stats(

    ticker: str = Query(..., min_length=1, description= "Stock Ticker Symbol"),
    start: Optional[str] = Query(None, description="Start date YYYY-MM-DD"),
    end: Optional[str] = Query(None, description="End date YYYY-MM-DD"),
):
    
    try:
        result = get_stocks_data(ticker=ticker, start=start, end=end)
        return result
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"server error: {e}")
    
    
