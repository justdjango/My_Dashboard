import pandas as pd
from pandas_datareader.data import DataReader

import dash
import dash_core_components as dcc
import dash_html_components as html

df_symbol = pd.read_csv('tickers.csv')


def dispatcher(request):

    app = _create_app()

    params = {
        'data': request.body,
        'method': request.method,
        'content_type': request.content_type
    }

    with app.server.test_request_context(request.path, **params):
        app.server.preprocess_request()
        try:
            response = app.server.full_dispatch_request()
        except Exception as e:
            response = app.server.make_response(app.server.handle_exception(e))
        return response.get_data()



def _create_app():

	app = dash.Dash(csrf_protect=False)
	app.layout = html.Div([
			html.Div([
					html.H2('Quandl Finance Explorer',
						style = {
							'display': 'inline',
							'float': 'left',
							'font-size': '2.65em',
                            'margin-left': '7px',
                            'font-weight': 'bolder',
                            'font-family': 'Product Sans',
                            'color': "rgba(117, 117, 117, 0.95)",
                            'margin-top': '20px',
                            'margin-bottom': '0'
						}),
					html.A('Home', href='/home/', style = {
						'color': 'red',
						'display': 'inline',
                		'margin-left': '54%'
						})
					]),
			dcc.Dropdown(
					id='stock-ticker-input',
					options = [{'label': s[0], 'value': s[1]} for s in zip(df_symbol.Company, df_symbol.Symbol)],
					value = ['AAPL', 'TSLA'],
					multi = True
				),
			html.Div(id='graphs')

			@app.callback(
					dash.dependencies.Output('graphs', 'children'),
					[dash.dependencies.Input('stock-ticker-input','value')]
				)


















						)
				])
		])

	return 