
from waitress import serve
from smpa.app import api

serve(api, listen='*:5000')
