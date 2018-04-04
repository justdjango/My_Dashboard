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

	return 