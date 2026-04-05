import plotly.express as px
import pandas as pd

df_pm25 = pd.read_csv("nguyen_van_cuu_pm25.csv")
df_pm10 = pd.read_csv("nguyen_van_cuu_pm10.csv")

df_pm25["datetimeLocal"] = pd.to_datetime(df_pm25["datetimeLocal"])
df_pm10["datetimeLocal"] = pd.to_datetime(df_pm10["datetimeLocal"])

# Plot for PM2.5
fg_pm25 = px.line(
    df_pm25,
    x="datetimeLocal",
    y="value",
    title="Pollution PM2.5 de l'air à Nguyen Van Cuu (partie est de Hanoï, environ 70km de notre Capt-Air)",
    labels={
        "datetimeLocal": "Date",
        "value": "µg/m³",
    },
    template="plotly_dark",
    color_discrete_sequence=["#00CC96"]  # Green color for PM2.5
)

fg_pm25.update_layout(
    font_family="IBM Plex Sans",
    hovermode="x unified"
)

fg_pm25.update_xaxes(
    nticks=10,
    tickformat="%d %b"
)

fg_pm25.add_hline(
    y=5,
    line_dash="dash",
    line_color="red",
    annotation_text="Limite de l'OMS (moyenne annuelle) à 5"
)
fg_pm25.update_yaxes(range=[0, 110])
fg_pm25.write_html("plot_pm25.html", include_plotlyjs="cdn")

# Plot for PM10
# Plot for PM10
fg_pm10 = px.line(
    df_pm10,
    x="datetimeLocal",
    y="value",
    title="Pollution PM10 de l'air à Nguyen Van Cuu (partie est de Hanoï, environ 70km de notre Capt-Air)",
    labels={
        "datetimeLocal": "Date",
        "value": "µg/m³",
    },
    template="plotly_dark",
    color_discrete_sequence=["#EF553B"]
)

fg_pm10.update_layout(
    font_family="IBM Plex Sans",
    hovermode="x unified"
)

fg_pm10.update_xaxes(
    nticks=10,
    tickformat="%d %b"
)

fg_pm10.update_yaxes(range=[0, None])  

fg_pm10.add_hline(
    y=15,
    line_dash="dash",
    line_color="red",
    annotation_text="Limite de l'OMS (moyenne annuelle) à 15"
)
fg_pm10.update_yaxes(range=[0, 110])
fg_pm10.write_html("plot_pm10.html", include_plotlyjs="cdn")
print("Generated: plot_pm25.html and plot_pm10.html")