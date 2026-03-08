import streamlit as st

from datetime import date
from main import Calculate

# API_URL = "http://localhost:8000/billing"

st.set_page_config(
    page_title="Jai Maa Vaisano Jwellers",
    page_icon="💎",
    layout="centered"
)

# ---------- Custom Styling ----------
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
}

.title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    background: linear-gradient(90deg,#FFD700,#FFA500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle{
    text-align:center;
    color:#cbd5f5;
}

.bill-card{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    border:2px solid gold;
    margin-top:20px;
}

.bill-row{
    display:flex;
    justify-content:space-between;
    padding:8px 0;
    border-bottom:1px solid #334155;
}

.total{
    font-size:22px;
    color:gold;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<p class="title">💎 Jai Maa Vaisano Jwellers</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle"> ~ Namsate 🙏 ~ </p>', unsafe_allow_html=True)

st.divider()

# ---------- Input Form ----------
with st.form("billing_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        date_obj = st.date_input("Deal Date")
        

    with col2:
        multiplier = st.number_input(
            "Interest Multiplier",
            min_value=0.0,
            step=0.1
        )
    
    with col3:
        interest_rate = st.selectbox(
            "Interest Rate (%)",
            ["2%", "2.5%", "3%", "4%", "5%"]
        )
        
        
    if interest_rate == "2%":
        rate = 0.02
    elif interest_rate == "2.5%":
        rate = 0.025
    elif interest_rate == "3%":
        rate = 0.03
    elif interest_rate == "4%":
        rate = 0.04
    elif interest_rate == "5%":
        rate = 0.05

    submit = st.form_submit_button("Calculate Billing")

# ---------- API Request ----------
if submit:



    with st.spinner("Calculating..."):

        
            obj = Calculate(date_obj , multiplier, rate)
            data = obj.billing()


            st.markdown(
                f"""
                <div class="bill-card">

                <div class="bill-row">
                <span>Today's Date</span>
                <span>{data["Today"]}</span>
                </div>

                <div class="bill-row">
                <span>Deal Date</span>
                <span>{data["Deal_date"]}</span>
                </div>
                
                <div class="bill-row">
                <span>Mul</span>
                <span>{data["mul"]}</span>
                </div>
                
                <div class="bill-row">
                <span>Rate</span>
                <span>{interest_rate}</span>
                </div>
                
                <div class="bill-row">
                <span>Duration</span>
                <span>{data["duration"]} days</span>
                </div>

                <div class="bill-row">
                <span>Total Interest</span>
                <span>₹ {data["total_intrest"]}</span>
                </div>

                <div class="bill-row total">
                <span>Total Amount</span>
                <span>₹ {data["total_amount"]}</span>
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    