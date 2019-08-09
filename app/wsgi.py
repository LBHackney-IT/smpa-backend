
from waitress import serve
from smpa.app import api
from smpa.helpers.console import console


console.log('Starting')


serve(api, listen='*:5000')
