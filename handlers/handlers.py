from views.views import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/", IndexHandler),
	(r"/log_display/",Log_displayHandler),
	]
HANDLERS +=[(r"/chart/", ChartHandler)]
