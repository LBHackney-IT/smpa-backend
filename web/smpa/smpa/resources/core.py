from molten import field
from typing import Optional

from arrow.arrow import Arrow

from smpa.helpers.database import MyUUID


class BaseResource:
    id: Optional[MyUUID] = field(response_only=True)
    created_at: Optional[Arrow]
    updated_at: Optional[Arrow]
