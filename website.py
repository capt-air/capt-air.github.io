import plotly.express as px
import pandas as pd

df = pd.read_csv("lfay_data.csv")
df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], dayfirst=True)
fg = px.line(df, x="Datetime", y="Value", 
             title="lfay_pollution", 
             labels={"Datetime": "Date", "Value": "PM2.5 (µg/m³)"}, 
             template="plotly_dark")

fg.update_layout(
    font_family="IBM Plex Sans",
    hovermode="x unified"
    )


fg.add_hline(y=15, line_dash="dash", line_color="red", annotation_text="Limite de la WHO")
fg.show()

html_div = fg.to_html(full_html=False, include_plotlyjs='cdn')
print(html_div)