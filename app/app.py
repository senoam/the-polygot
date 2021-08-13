import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
from bond import make_bond

data = pd.read_csv('df.csv')
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
app = dash.Dash(__name__)

def get_avg():
    return data['Daily Positive Cases'].mean()

app.layout = html.Div(
    children=[
        html.H1(children="Daily Covid Cases in Jakarta",
                style={"fontSize": "48px", "color": "red"}),
        html.P(
            children="Analyze the growth of covid cases in Jakarta in June 2021",
        ),
        html.Div(
            children=[
                html.Div(
                    children="Date Range",
                    className="menu-title"
                    ),
                dcc.DatePickerRange(
                    id="date-range",
                    min_date_allowed=data.Date.min().date(),
                    max_date_allowed=data.Date.max().date(),
                    start_date=data.Date.min().date(),
                    end_date=data.Date.max().date(),
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="daily-positive-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="active-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    [Output("daily-positive-chart", "figure"), Output("active-chart", "figure")],
    [
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)

def update_charts(start_date, end_date):
    mask = (
        (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    positive_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Daily Positive Cases"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Daily Positive Cases",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    active_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Active Cases"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Active Cases", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return positive_figure, active_figure

if __name__ == "__main__":
    app.run_server(debug=True)
    