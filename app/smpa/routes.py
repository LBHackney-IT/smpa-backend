# -*- coding: utf-8 -*-

"""
    smpa.routes
    ~~~~~~~~~~~~~~~~
    Routing config.
"""
import os
from .resources.swagger import ApiSpecResource

from .resources.material import (  # NOQA
    # Options
    MaterialOptionRoofPost,
    MaterialOptionRoofPatch,
    MaterialOptionWallPost,
    MaterialOptionWallPatch,
    MaterialOptionWindowPost,
    MaterialOptionWindowPatch,
    MaterialOptionDoorPost,
    MaterialOptionDoorPatch,
    # Materials
    MaterialRoofPost,
    MaterialRoofPatch,
    MaterialWallPost,
    MaterialWallPatch,
    MaterialWindowPost,
    MaterialWindowPatch,
    MaterialDoorPost,
    MaterialDoorPatch,
)
from .resources import (  # NOQA
    # Unit resources
    AreaUnitResource, AreaUnitListResource, LinearUnitResource, LinearUnitListResource,
    # User resources
    UserResourcePost, UserResourceList, UserResourcePatch, AgentResource,
    ApplicantResource, AuthResource, UserProfileResourcePatch,
    # Address resources
    AddressPatch, AddressPost, SiteAddressPatch, SiteAddressPost,
    BS7666AddressResource, ExternalAddressResource, InternationalAddressResource,
    # Document resources
    DocumentSizeResource, DocumentFilePostResource, DocumentTypePostResource,
    DocumentTypePatchResource, DocumentFileApplicationResource, DocumentFileDeleteResource,
    # Application resources
    ApplicationResourcePost, ApplicationResourcePatch, ApplicationStatusListResource,
    # Site resources
    SiteAreaPostResource, SiteAreaPatchResource, SiteConstraintsPostResource,
    SiteConstraintsPatchResource,
    # Proposals
    ProposalExtensionPostResource, ProposalExtensionPatchResource,
    ProposalEquipmentPostResource, ProposalEquipmentPatchResource,
    # Work
    WorksLocationPost, WorksLocationPatch, BasementWorksTypePost, BasementWorksTypePatch,
    RoofWorksTypePost, RoofWorksTypePatch, BorderWorksTypePost, BorderWorksTypePatch,
    AccessWorksScopePost, AccessWorksScopePatch, AccessWorksTypePost, AccessWorksTypePatch,
    ParkingWorksScopePost, ParkingWorksScopePatch, EquipmentWorksTypePost, EquipmentWorksTypePatch,
    EquipmentWorksConservationTypePost, EquipmentWorksConservationTypePatch,
    GatesFencesWallsTypePost, GatesFencesWallsTypePatch,
    # Meta
    DeclarationListResource, OwnershipTypeListResource,
    # Payment
    PaymentPostResource, PaymentListResource, PaymentCheckResource
)

EXEMPT_ROUTES = [
    '/auth',
    '/docs',
    '/users/create'
]


def add_route(api, path, resource):
    prefix = '/api/v1'
    api.add_route(f'{prefix}{path}', resource)


def init_routes(api, config):
    # Documentation routes
    api.add_route("/apispec", ApiSpecResource())
    api.add_static_route("/redoc", os.path.join(
        os.path.dirname(__file__), "static", "redoc"))
    api.add_static_route("/swagger", os.path.join(
        os.path.dirname(__file__), "static", "swagger"))

    # Resources
    auth = AuthResource()

    # API resources
    addresses_patch = AddressPatch()
    addresses_post = AddressPost()
    siteaddresses_patch = SiteAddressPatch()
    siteaddresses_post = SiteAddressPost()
    site_area_post = SiteAreaPostResource()
    site_area_patch = SiteAreaPatchResource()
    site_constraints_post = SiteConstraintsPostResource()
    site_constraints_patch = SiteConstraintsPatchResource()
    proposal_extension_post = ProposalExtensionPostResource()
    proposal_extension_patch = ProposalExtensionPatchResource()
    proposal_equipment_post = ProposalEquipmentPostResource()
    proposal_equipment_patch = ProposalEquipmentPatchResource()
    works_location_post = WorksLocationPost()
    works_location_patch = WorksLocationPatch()
    basement_works_type_post = BasementWorksTypePost()
    roof_works_type_post = RoofWorksTypePost()
    border_works_type_post = BorderWorksTypePost()
    access_works_scope_post = AccessWorksScopePost()
    access_works_type_post = AccessWorksTypePost()
    parking_works_scope_post = ParkingWorksScopePost()
    equipment_works_type_post = EquipmentWorksTypePost()
    equipment_works_conservation_type_post = EquipmentWorksConservationTypePost()
    gates_fences_walls_type_post = GatesFencesWallsTypePost()
    applications_post = ApplicationResourcePost()
    applications_patch = ApplicationResourcePatch()
    application_status_list = ApplicationStatusListResource()
    users_post = UserResourcePost()
    users_list = UserResourceList()
    users_patch = UserResourcePatch()
    user_profiles_patch = UserProfileResourcePatch()
    document_file_delete = DocumentFileDeleteResource()
    document_file_post = DocumentFilePostResource()
    document_file_application = DocumentFileApplicationResource()
    document_type_post = DocumentTypePostResource()
    document_type_patch = DocumentTypePatchResource()
    declarations_list = DeclarationListResource()
    ownership_types_list = OwnershipTypeListResource()
    payment_post = PaymentPostResource()
    payment_list = PaymentListResource()
    payment_check = PaymentCheckResource()

    # To fix
    area_units = AreaUnitResource()
    area_units_list = AreaUnitListResource()
    linear_units = LinearUnitResource()
    linear_units_list = LinearUnitListResource()
    agents = AgentResource()
    # applicants = ApplicantResource()
    documentsizes = DocumentSizeResource()

    # Material Options
    material_option_roof_post = MaterialOptionRoofPost()
    material_option_wall_post = MaterialOptionWallPost()
    material_option_door_post = MaterialOptionDoorPost()
    material_option_window_post = MaterialOptionWindowPost()

    # Submitted Materials
    material_roof_post = MaterialRoofPost()
    material_roof_patch = MaterialRoofPatch()
    material_wall_post = MaterialWallPost()
    material_wall_patch = MaterialWallPatch()
    material_window_post = MaterialWindowPost()
    material_window_patch = MaterialWindowPatch()
    material_door_post = MaterialDoorPost()
    material_door_patch = MaterialDoorPatch()

    ########################################
    # FUTURE ROUTES FOR AN ADMIN INTERFACE #
    ########################################
    # material_option_roof_patch = MaterialOptionRoofPatch()
    # material_option_wall_patch = MaterialOptionWallPatch()
    # material_option_door_patch = MaterialOptionDoorPatch()
    # material_option_window_patch = MaterialOptionWindowPatch()
    # basement_works_type_patch = BasementWorksTypePatch()
    # roof_works_type_patch = RoofWorksTypePatch()
    # border_works_type_patch = BorderWorksTypePatch()
    # access_works_scope_patch = AccessWorksScopePatch()
    # access_works_type_patch = AccessWorksTypePatch()
    # parking_works_scope_patch = ParkingWorksScopePatch()
    # equipment_works_type_patch = EquipmentWorksTypePatch()
    # equipment_works_conservation_type_patch = EquipmentWorksConservationTypePatch()
    # gates_fences_walls_type_patch = GatesFencesWallsTypePatch()

    # Routes
    add_route(api, '/auth', auth)

    add_route(api, '/access-works-scopes', access_works_scope_post)
    add_route(api, '/addresses', addresses_post)
    add_route(api, '/addresses/{id}', addresses_patch)
    add_route(api, '/basement-works-types', basement_works_type_post)
    add_route(api, '/equipment-proposals', proposal_equipment_post)
    add_route(api, '/equipment-proposals/{id}', proposal_equipment_patch)
    add_route(api, '/equipment-works-conservation-types', equipment_works_conservation_type_post)
    add_route(api, '/equipment-works-types', equipment_works_type_post)
    add_route(api, '/extension-proposals', proposal_extension_post)
    add_route(api, '/extension-proposals/{id}', proposal_extension_patch)
    add_route(api, '/gate-fences-walls-types', gates_fences_walls_type_post)
    add_route(api, '/roof-works-types', roof_works_type_post)
    add_route(api, '/site-addresses', siteaddresses_post)
    add_route(api, '/site-addresses/{id}', siteaddresses_patch)
    add_route(api, '/site-areas', site_area_post)
    add_route(api, '/site-areas/{id}', site_area_patch)
    add_route(api, '/site-constraints', site_constraints_post)
    add_route(api, '/site-constraints/{id}', site_constraints_patch)
    add_route(api, '/works-locations', works_location_post)
    add_route(api, '/works-locations/{id}', works_location_patch)
    add_route(api, '/user-profiles/{id}', user_profiles_patch)

    # Working on
    add_route(api, '/materials/options/roof', material_option_roof_post)
    add_route(api, '/materials/options/wall', material_option_wall_post)
    add_route(api, '/materials/options/door', material_option_door_post)
    add_route(api, '/materials/options/window', material_option_window_post)

    add_route(api, '/materials/roof', material_roof_post)
    add_route(api, '/materials/roof/{id}', material_roof_patch)
    add_route(api, '/materials/wall', material_wall_post)
    add_route(api, '/materials/wall/{id}', material_wall_patch)
    add_route(api, '/materials/wind', material_window_post)
    add_route(api, '/materials/wind/{id}', material_window_patch)
    add_route(api, '/materials/door', material_door_post)
    add_route(api, '/materials/door/{id}', material_door_patch)

    # To document
    add_route(api, '/border-works-types', border_works_type_post)
    add_route(api, '/access-works-types', access_works_type_post)
    add_route(api, '/parking-works-scopes', parking_works_scope_post)

    add_route(api, '/area-units', area_units_list)
    add_route(api, '/area-units/{id}', area_units)

    add_route(api, '/linear-units', linear_units_list)
    add_route(api, '/linear-units/{id}', linear_units)

    add_route(api, '/applications', applications_post)
    add_route(api, '/applications/{id}', applications_patch)
    add_route(api, '/applications/{id}/documents', document_file_application)
    add_route(api, '/applications/{id}/payments', payment_post)
    add_route(api, '/application-statuses', application_status_list)
    add_route(api, '/payments', payment_list)
    add_route(api, '/payments/{id}/check', payment_check)
    add_route(api, '/documents', document_file_post)
    add_route(api, '/documents/{id}', document_file_delete)
    add_route(api, '/declarations', declarations_list)
    add_route(api, '/ownership-types', ownership_types_list)

    add_route(api, '/users/create', users_post)
    add_route(api, '/users', users_list)
    add_route(api, '/users/{id}', users_patch)

    add_route(api, '/agents', agents)
    add_route(api, '/agents/{id}', agents)

    # add_route(api, '/applicants', applicants)
    # add_route(api, '/applicants/{id}', applicants)

    add_route(api, '/document-sizes', documentsizes)
    add_route(api, '/document-sizes/{id}', documentsizes)

    add_route(api, '/document-types', document_type_post)
    add_route(api, '/document-types/{id}', document_type_patch)

    ########################################
    # FUTURE ROUTES FOR AN ADMIN INTERFACE #
    ########################################

    # add_route(api, '/access-works-scopes/{id}', access_works_scope_patch)
    # add_route(api, '/basement-works-types/{id}', basement_works_type_patch)  # QA
    # add_route(
    #     api, '/equipment-works-conservation-types/{id}', equipment_works_conservation_type_patch)
    # add_route(api, '/equipment-works-types/{id}', equipment_works_type_patch)
    # add_route(api, '/gate-fences-walls-types/{id}', gates_fences_walls_type_patch)
    # add_route(api, '/roof-works-types/{id}', roof_works_type_patch)
    # add_route(api, '/materials/options/roof/{id}', material_option_roof_patch)
    # add_route(api, '/materials/options/wall/{id}', material_option_wall_patch)
    # add_route(api, '/materials/options/door/{id}', material_option_door_patch)
    # add_route(api, '/materials/options/window/{id}', material_option_window_patch)
    # add_route(api, '/border-works-types/{id}', border_works_type_patch)
    # add_route(api, '/access-works-types/{id}', access_works_type_patch)
    # add_route(api, '/parking-works-scopes/{id}', parking_works_scope_patch)

    config.resources = [
        addresses_post,
        addresses_patch,
        siteaddresses_post,
        siteaddresses_patch,
        site_area_post,
        site_area_patch,
        site_constraints_post,
        site_constraints_patch,
        works_location_post,
        works_location_patch,
        basement_works_type_post,
        roof_works_type_post,
        border_works_type_post,
        access_works_scope_post,
        access_works_type_post,
        parking_works_scope_post,
        equipment_works_type_post,
        equipment_works_conservation_type_post,
        gates_fences_walls_type_post,
        user_profiles_patch,
        application_status_list,
        # Materials
        material_option_roof_post,
        material_option_wall_post,
        material_option_door_post,
        material_option_window_post,
        material_roof_post,
        material_roof_patch,
        material_wall_post,
        material_wall_patch,
        material_window_post,
        material_window_patch,
        material_door_post,
        material_door_patch,
        #
        users_patch,
        users_post,
        users_list,
        applications_post,
        applications_patch,
        document_type_post,
        document_type_patch,
        document_file_application,
        document_file_delete,
        declarations_list,
        ownership_types_list,
        payment_post,
        payment_list,
        payment_check,

        ########################################
        # FUTURE ROUTES FOR AN ADMIN INTERFACE #
        ########################################
        # material_option_roof_patch,
        # material_option_wall_patch,
        # material_option_door_patch,
        # material_option_window_patch,
        # basement_works_type_patch,
        # roof_works_type_patch,
        # border_works_type_patch,
        # access_works_scope_patch,
        # access_works_type_patch,
        # parking_works_scope_patch,
        # equipment_works_type_patch,
        # equipment_works_conservation_type_patch,
        # gates_fences_walls_type_patch,


        # To fix
        area_units,
        area_units_list,
        linear_units_list,
        linear_units,
        agents,
        # applicants,
        documentsizes,
        auth,
    ]
