import fastapi
from main import Calculate

app = fastapi.FastAPI()


@app.get("/billing")
def billing(date: str, mul: float):
    calculate = Calculate(date, mul)
    return calculate.billing()
    
    