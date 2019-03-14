# These imports are provided for convenience so you can
# import any service directly from ``services``
#
# ie: ``from services import _users``

from .address import (  # NOQA
    _addresses, _site_addresses, _bs7666_addresses, _external_addresses, _international_addresses
)
from .application import *  # NOQA
from .document import _document_sizes  # NOQA
from .test import _tests  # NOQA
from .unit import _area_units, _linear_units  # NOQA
from .user import _roles, _users, _agents, _applicants  # NOQA
