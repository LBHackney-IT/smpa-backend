# These imports are provided for convenience so you can
# import any service directly from ``services``
#
# ie: ``from services import _users``
# Module
from .site import *  # NOQA
from .site import _site_areas, _site_constraints # NOQA
from .test import _tests  # NOQA
from .unit import *  # NOQA
from .unit import _area_units, _linear_units  # NOQA
from .user import *  # NOQA
from .user import _roles, _users, _agents, _applicants, _user_profiles  # NOQA
from .work import *  # NOQA
from .work import (  # NOQA
    _works, _work_trees, _work_equipments, _works_locations, _roof_works_types,
    _access_works_types, _border_works_types, _access_works_scopes, _parking_works_scopes,
    _equipment_works_types, _work_extension_options, _basement_works_types,
    _work_extension_original_houses, _extension_original_house_porchs,
    _work_extension_car_bike_spaces, _work_extension_boundaries,
    _equipment_works_conservation_types, _extension_original_house_basements,
    _extension_original_house_claddings, _extension_original_house_staircases,
    _extension_original_house_roofs, _work_extension_incidental_buildings,
    _extension_outbuildings, _work_extension_means_of_access_to_sites,
    _extension_original_house_balcony_terraces, _extension_original_house_two_storey_extensions,
    _extension_original_house_single_storey_extensions,
    _extension_original_house_add_replacement_windows_doors,
    _extension_original_house_part_single_part_two_storey_extensions
)
from .address import *  # NOQA
from .address import (  # NOQA
    _addresses, _site_addresses, _bs7666_addresses, _external_addresses, _international_addresses
)
from .document import *  # NOQA
from .document import _document_sizes  # NOQA
from .material import *  # NOQA
from .material import (  # NOQA
    _base_materials, _materials_door, _materials_roof, _materials_wall, _other_materials,
    _materials_window, _material_options_door, _material_options_roof, _material_options_wall,
    _material_options_window, _external_building_materials
)
from .application import *  # NOQA
from .application import _applications  # NOQA
from .proposal import *  # NOQA
from .proposal import _proposals_extension, _proposals_equipment  # NOQA
