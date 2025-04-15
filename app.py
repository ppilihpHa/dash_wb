import dash
from dash import html, dcc 
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Alles Gute Papa"
server = app.server  

# Navigation (Navbar oben)
navbar = dbc.NavbarSimple(
    brand="Überraschung 🎁",
    brand_href="/",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Start", href="/")),
        dbc.NavItem(dbc.NavLink("Spiel", href="/spiel")),
        dbc.NavItem(dbc.NavLink("Wien-Reise", href="/wien")),
    ]
)

# Seiten-Inhalte
def layout_startseite():
    return dbc.Container([
        html.H1("Alles Gute zum 50. Geburtstag 🎉"),
        html.P(["Du hast zwar schon so viel erreicht aber dennoch wünschen wir dir auch in den nächsten Jahren viel ", 
                html.B("Glück"),", ", html.B("Erfolg"),", ", "und vor allem ", html.B("Spaß"), ". Auf das du noch lange gesund bleibst und weitere Abenteuer mit uns erleben kannst"]),
        html.Br(),
        html.P("Vielen Dank für alles was du uns ermöglichst, wir sind sehr dankbar und stolz auf dich! ♥️ "),
        html.Img(src="/assets/Fam1.jpg", style={"width": "50%"})
    ], className="mt-4")

def layout_spiel():
    return dbc.Container([
        html.H2(["🎲 Damit du schonmal in Stimmung für unsere Reise kommst, haben wir einen klassischen " , html.B("Spieleabend"), " für dich vorbereitet!"]),
        html.P("Am Sontag nach dem Essen brauchen wir dein schlaues Köpfchen, um herauszufinden was mit Emilia Horvath in Wien passiert ist"),
        html.A("unser Spiel: Soko Unvergessen", href="https://www.storiesbyxenia.at/wien-spielt"),
        html.Br(),
        html.Div([
            html.Img(src='/assets/spiel1.jpg', style={"width": "50%"}),
            html.Img(src='/assets/spiel2.jpg', style={"width": "50%"})
            ], style={"display": "flex", "flex-direction": "row", "justify-content": "center"})
    ], className="mt-4")

# Do 25.09 - 27.09

def layout_wien():
    return dbc.Container([
        html.H2("🌆 Eine Reise nach Wien"),
        html.P("Wir werden am Donnerstag den 25.09 nach Wien runter fahren"),
        html.Img(src="/assets/wien1.jpg", style={"width": "50%"}),
        
        html.Div(style={"height": "30px"}),
        html.P(["wir verbringen unsere Nächte in einem schönen ", html.B("3-Schlafzimmer AirBnB"), " mitten in Wien."]),
        html.Div([
            html.Img(src='/assets/airbnb1.jpg', style={"width": "50%"}),
            html.Img(src='/assets/airbnb2.jpg', style={"width": "50%"})
            ], style={"display": "flex", "flex-direction": "row", "justify-content": "center"}),
        
        html.Div(style={"height": "30px"}),
        html.P(["Am Abend gehts dann ins Raimund Theater zu ", html.B("Phantom der Oper")]),
        html.Img(src="/assets/wien2.jpg", style={"width": "50%"}),
        
        html.Div(style={"height": "30px"}),
        html.P(["dann am Freitag steht eine tolle ", html.B("Weintour"), ", samt Verpflegung, durch die schönen Ecken Wiens auf dem Plan. Am Abend gehen wir dann noch lecker essen 😋"]),
        html.Div([
            html.Img(src='/assets/weintour1.jpg', style={"width": "50%"}),
            html.Img(src='/assets/weintour2.jpg', style={"width": "50%"})
            ], style={"display": "flex", "flex-direction": "row", "justify-content": "center"}),
    
        html.Div(style={"height": "30px"}),
        html.P(["damit dir die ganze Reise auch gut tut, haben wir für Samstag noch eine tolle Route zum ", html.B("Laufen"), " rausgesucht"]),
        html.Img(src="/assets/wien3.jpg", style={"width": "50%"})

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