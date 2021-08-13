import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input

# Reference: https://realpython.com/python-dash/#how-to-set-up-your-local-environment

data = pd.read_csv('./app/df.csv')
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def get_avg():
    return data['Daily Positive Cases'].mean()

app.layout = html.Div(
    children=[
        html.H1(children="Daily Covid Cases in Jakarta",
                className="header-title"),
        html.P(
            children="Daily positive cases, active cases, recoveries and deaths in June 2021",
            className='header-description',
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
            ],
            className="wrapper"
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
                html.Div(
                    children=dcc.Graph(
                        id="recoveries-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="deaths-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    [Output("daily-positive-chart", "figure"), Output("active-chart", "figure"), Output("recoveries-chart", "figure"), Output("deaths-chart", "figure")],
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

    recoveries_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Daily Recoveries"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Recovery Cases", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    deaths_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Deaths"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Deaths", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return positive_figure, active_figure, recoveries_figure, deaths_figure

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050",debug=True)
    