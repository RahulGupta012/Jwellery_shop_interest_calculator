import datetime

class Calculate:
    def __init__(self , date , mul, rate):
        self.date = date
        self.mul = mul 
        self.rate = rate 
        
    def duration(self):
        #today = datetime.datetime.now().strftime("%Y-%m-%d")
        today = datetime.datetime.now().date()
        #date_obj = datetime.datetime.strptime(self.date,  "%Y-%m-%d")
        date_obj = self.date
        duration = (today - date_obj).days
        return duration 
    
    def billing(self):
        duration = self.duration()
        intrest_per_day = (self.mul * self.rate) / 30
        total_intrest = duration * intrest_per_day
        total_amount = self.mul + total_intrest
        
        return {
            "Today": datetime.datetime.now().date(),
            "mul" : self.mul,
            "Deal_date": self.date,
            "duration": duration,
            "rate": self.rate,
            "total_intrest": round(total_intrest, 2),
            "total_amount": round(total_amount, 2)
        }