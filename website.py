import plotly.express as px
import pandas as pd

def make_html_from_csv(csv_name,graph_title, theme, color, WHO_limit, output_name):
    df = pd.read_csv(csv_name)
    df["datetimeLocal"] = pd.to_datetime(df["datetimeLocal"])
    fg = px.line(
        df,
        x="datetimeLocal",
        y="value",
        title=graph_title,
        labels={
            "datetimeLocal": "Date",
            "value": "µg/m³",
        },
        template=theme,
        color_discrete_sequence=[color] # Green color for PM2.5
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
        y=WHO_limit,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Limite de l'OMS (moyenne annuelle) à {WHO_limit}"
    )
    fg.update_yaxes(range=[0, 110])
    fg.update_traces(line=dict(width=0))
    fg.write_html(output_name, include_plotlyjs="cdn")

make_html_from_csv( csv_name="ecopark_pm25.csv",
                    graph_title="Pollution PM1",
                    theme="plotly_dark",
                    color="#00CC96",
                    WHO_limit=5,
                    output_name="ecopark_pm1111.html")
