import dash
from dash import html, dcc 
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Alles Gute Papa"
server = app.server  # für Deployment später nötig

# Navigation (Navbar oben)
navbar = dbc.NavbarSimple(
    brand="Überraschung 🎁",
    brand_href="/",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Start", href="/")),
        dbc.NavItem(dbc.NavLink("Brettspiel", href="/spiel")),
        dbc.NavItem(dbc.NavLink("Wien-Reise", href="/wien")),
    ]
)

# Seiten-Inhalte
def layout_startseite():
    return dbc.Container([
        html.H1("Willkommen!"),
        html.P("Diese Seite ist eine Überraschung für dich... 🎉"),
    ], className="mt-4")

def layout_spiel():
    return dbc.Container([
        html.H2("🎲 Dein neues Brettspiel"),
        html.P("Hier kannst du bald das Spielbrett, die Regeln und mehr sehen."),
        # html.Img(src='/assets/dein_bild.png', style={"width": "50%"})
    ], className="mt-4")

def layout_wien():
    return dbc.Container([
        html.H2("🌆 Deine Reise nach Wien"),
        html.P("Hier findest du bald die Highlights deiner Reise!"),
    ], className="mt-4")

# App Layout mit Seitenlogik
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    navbar,
    html.Div(id="page-content")
])

# Callback zur Seitenanzeige
@app.callback(
    dash.Output("page-content", "children"),
    dash.Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/spiel":
        return layout_spiel()
    elif pathname == "/wien":
        return layout_wien()
    else:
        return layout_startseite()

if __name__ == "__main__":
    app.run(debug=True)