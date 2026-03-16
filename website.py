import plotly.express as px
import pandas as pd

df = pd.read_csv("lfay_data.csv")

df["datetimeLocal"] = pd.to_datetime(df["datetimeLocal"])

fg = px.line(
    df,
    x="datetimeLocal",
    y="value",
    color="parameter",
    title="Air pollution",
    labels={
        "datetimeLocal": "Date",
        "value": "µg/m³",
        "parameter": "Pollutant"
    },
    template="plotly_dark"
)

fg.update_layout(
    font_family="IBM Plex Sans",
    hovermode="x unified"
)

fg.update_xaxes(
    nticks=10,
    tickformat="%d %b"
)


fg.add_hline(
    y=15,
    line_dash="dash",
    line_color="red",
    annotation_text="WHO limit"
)

fg.show()


fg.write_html("plot.html", include_plotlyjs="cdn")
