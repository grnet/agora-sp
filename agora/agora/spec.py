  # djoser_verifier: agora.utils.djoser_verifier
  # userid_extractor: agora.utils.userid_extractor

CUSTOM_USERS = {
    '.collection.django': {},
    'model': 'accounts.models.User',
    ':permissions_namespace': 'agora.checks.User',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'username': {
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.field.string': {}},
        'email': {
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.field.string': {}},
        'first_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'is_staff': {
            '.field.boolean': {},
            '.flag.nullable.default': {}},
        'is_active': {
            '.flag.orderable': {},
            '.field.boolean': {}},
        'date_joined': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'shibboleth_id': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'role': {
            '.flag.orderable': {},
            '.flag.filterable': {},
            '.field.string': {}},
        'organisation': {
            '.field.ref': {},
            'source': 'organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'organisation_id': {
            '.field.uuid': {},
            'source': 'organisation.id',
            '.flag.nowrite': {}},
        'providers': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'organisation',
            'model': 'accounts.models.User.organisations.through',
            'source': 'organisations',
            'bound': 'user',
            'fields': {
                'organisation': {'.field.ref': {},
                                'source': 'organisation_id',
                                'to': 'api/v2/providers'},
            }
        }

    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


RESOURCE_ADMINS = {
    '.collection.django': {},
    'model': 'service.models.ResourceAdminship',
    ':permissions_namespace': 'agora.checks.ResourceAdminship',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'state': {
            '.field.string': {},
            'default': 'pending',
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'resource': {
            '.field.ref': {},
            'source': 'resource_id',
            'to': '/api/v2/resources',
            '.flag.nullable.default': {},
            '.flag.filterable': {}},
        'resource_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.orderable': {},
            'source': 'resource.erp_bai_1_name'},
        'admin_email': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.orderable': {},
            'source': 'admin.email'},
        'admin_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'admin.first_name'},
        'admin_last_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'admin.last_name'},
        'admin_id': {
            '.field.uuid': {},
            '.flag.nowrite': {},
            'source': 'admin.id'},
        'created_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'updated_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'admin': {
            '.field.ref': {},
            'source': 'admin_id',
            '.flag.filterable': {},
            '.flag.nullable.default': {},
            'to': '/api/v2/custom-users'},

    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
         'create': {
            'processors': {
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateResourceadminship',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                        'request/meta/headers',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',  # declared to ensure chaining
                    )},
                },
            },
        },
       'partial_update': {
           'processors': {
               'custom_post_partial_update': {
                   '.processor': {},
                   'module_path': 'service.models.PostPartialUpdateResourceadminship',
                   'read_keys': {'=': (
                       'backend/raw_response',
                       'auth/user',
                       'request/meta/headers',
                   )},
                   'write_keys': {'=': (
                       'backend/raw_response',  # declared to ensure chaining
                   )},
               },
           },
       },


    },
}

MERIL_DOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.MerilDomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

DOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.Domain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

MERIL_SUBDOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.MerilSubdomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'domain': {
            '.field.ref': {},
            'source': 'domain_id',
            'to': '/api/v2/merildomains',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SUBDOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.Subdomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'domain': {
            '.field.ref': {},
            'source': 'domain_id',
            'to': '/api/v2/domains',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SUPERCATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.Supercategory',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

CATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.Category',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'supercategory': {
            '.field.ref': {},
            'source': 'supercategory_id',
            'to': '/api/v2/supercategories',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SUBCATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.Subcategory',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'category': {
            '.field.ref': {},
            'source': 'category_id',
            'to': '/api/v2/categories',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

LEGAL_STATUSES = {
    '.collection.django': {},
    'model': 'accounts.models.LegalStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

NETWORKS = {
    '.collection.django': {},
    'model': 'accounts.models.Network',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'abbreviation': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

STRUCTURES = {
    '.collection.django': {},
    'model': 'accounts.models.Structure',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

AFFILIATIONS = {
    '.collection.django': {},
    'model': 'accounts.models.Affiliation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ESFRI_DOMAINS= {
    '.collection.django': {},
    'model': 'accounts.models.EsfriDomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ESFRI_TYPES= {
    '.collection.django': {},
    'model': 'accounts.models.EsfriType',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ACTIVITIES= {
    '.collection.django': {},
    'model': 'accounts.models.Activity',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

FUNDING_BODIES= {
    '.collection.django': {},
    'model': 'service.models.FundingBody',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

FUNDING_PROGRAMS = {
    '.collection.django': {},
    'model': 'service.models.FundingProgram',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ORDER_TYPES= {
    '.collection.django': {},
    'model': 'service.models.OrderType',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}
MULTIMEDIA= {
    '.collection.django': {},
    'model': 'accounts.models.Multimedia',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ACCESS_TYPES= {
    '.collection.django': {},
    'model': 'service.models.AccessType',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ACCESS_MODES= {
    '.collection.django': {},
    'model': 'service.models.AccessMode',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

TRLS= {
    '.collection.django': {},
    'model': 'service.models.TRL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

RESOURCE_LIFECYCLE_STATUSES= {
    '.collection.django': {},
    'model': 'service.models.LifeCycleStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

CHALLENGES= {
    '.collection.django': {},
    'model': 'accounts.models.Challenge',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


ORGANISATIONS = {
    '.collection.django': {},
    'model': 'accounts.models.Organisation',
    ':permissions_namespace': 'agora.checks.Organisation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
            '.flag.orderable': {},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
        'created_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'published_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'epp_bai_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_abbreviation': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_website': {
            '.field.string': {},
            '.flag.nullable.default': {},
        },
        'epp_bai_legal_entity': {
            '.field.boolean': {},
            'default': False
        },
        'epp_bai_legal_status': {
            '.field.ref': {},
            'source': 'epp_bai_legal_status_id',
            'to': '/api/v2/legalstatuses',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},

        'epp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'domain',
            'model': 'accounts.models.Organisation.epp_cli_1_scientific_domain.through',
            'source': 'epp_cli_1_scientific_domain',
            'bound': 'organisation',
            'fields': {
                'domain': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/domains'},
            }},
        'epp_cli_1_scientific_domain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_cli_2_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'subdomain',
            'model': 'accounts.models.Organisation.epp_cli_2_scientific_subdomain.through',
            'source': 'epp_cli_2_scientific_subdomain',
            'bound': 'organisation',
            'fields': {
                'subdomain': {'.field.ref': {},
                                'source': 'subdomain_id',
                                'to': 'api/v2/subdomains'},
            }},
        'epp_cli_2_scientific_subdomain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_cli_3_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'epp_oth_affiliations_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_loi_1_street_name_and_number': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_2_postal_code': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_3_city': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_4_region': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_5_country_or_territory': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_description': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_logo': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        # 'epp_mri_multimedia': {
        #     '.field.collection.django': {},
        #     '.flag.nullable.default': {},
        #     ':filter_compat': True,
        #     'flat': True,
        #     'id_field': 'id',
        #     'model': 'accounts.models.Organisation.epp_oth_multimedia',
        #     'source': 'epp_oth_multimedia',
        #     'bound': 'organisation',
        #     'fields': {
        #         'multimedia': {'.field.ref': {},
        #                         'source': 'id',
        #                         'to': 'api/v2/multimedia'},
        #     }
        # },
        'main_contact': {
          '.field.ref': {},
          'source': 'main_contact_id',
          'to': '/api/v2/contact-information',
          '.flag.nullable.default': {}},
        'public_contact': {
          '.field.ref': {},
          'source': 'public_contact_id',
          'to': '/api/v2/contact-information',
          '.flag.nullable.default': {}},
        'epp_coi_1_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.first_name',
          '.flag.nullable.default': {}},
        'epp_coi_2_last_name': {
          '.field.string': {},
          'source': 'main_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_3_email': {
          '.field.string': {},
          'source': 'main_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_4_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.phone',
          '.flag.nullable.default': {}},
        'epp_coi_5_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.position',
          '.flag.nullable.default': {}},
        'epp_coi_6_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.first_name',
          '.flag.nullable.default': {}},
        'epp_coi_7_last_name': {
          '.field.string': {},
          'source': 'public_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_8_email': {
          '.field.string': {},
          'source': 'public_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_9_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.phone',
          '.flag.nullable.default': {}},
        'epp_coi_10_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.position',
          '.flag.nullable.default': {}},
        'epp_mti_1_life_cycle_status': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mti_2_certifications': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_bai_hosting_legal_entity': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_participating_countries': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_affiliations': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'affiliation',
            'model': 'accounts.models.Organisation.epp_oth_affiliations.through',
            'source': 'epp_oth_affiliations',
            'bound': 'organisation',
            'fields': {
                'affiliation': {'.field.ref': {},
                                'source': 'affiliation_id',
                                'to': 'api/v2/affiliations'},
            }},
        'epp_oth_affiliations_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_networks': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'network',
            'model': 'accounts.models.Organisation.epp_oth_networks.through',
            'source': 'epp_oth_networks',
            'bound': 'organisation',
            'fields': {
                'network': {'.field.ref': {},
                                'source': 'network_id',
                                'to': 'api/v2/networks'},
            }},
        'epp_oth_networks_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_structure_type': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'structure',
            'model': 'accounts.models.Organisation.epp_oth_structure_type.through',
            'source': 'epp_oth_structure_type',
            'bound': 'organisation',
            'fields': {
                'structure': {'.field.ref': {},
                                'source': 'structure_id',
                                'to': 'api/v2/structures'},
            }},
        'epp_oth_structure_type_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_esfri_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'esfridomain',
            'model': 'accounts.models.Organisation.epp_oth_esfri_domain.through',
            'source': 'epp_oth_esfri_domain',
            'bound': 'organisation',
            'fields': {
                'esfridomain': {'.field.ref': {},
                                'source': 'esfridomain_id',
                                'to': 'api/v2/esfridomains'},
            }},
        'epp_oth_esfri_domain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_esfri_type': {
            '.field.ref': {},
            'source': 'epp_oth_esfri_type_id',
            'to': '/api/v2/esfritypes',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'epp_oth_esfri_type_verbose': {
            '.field.string': {},
            'source': 'epp_oth_esfri_type.name',
            '.flag.nowrite': {}},

        'epp_oth_meril_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'merildomain',
            'model': 'accounts.models.Organisation.epp_oth_meril_scientific_domain.through',
            'source': 'epp_oth_meril_scientific_domain',
            'bound': 'organisation',
            'fields': {
                'merildomain': {'.field.ref': {},
                                'source': 'merildomain_id',
                                'to': 'api/v2/merildomains'},
            }},
        'epp_oth_meril_scientific_domain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_oth_meril_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'merilsubdomain',
            'model': 'accounts.models.Organisation.epp_oth_meril_scientific_subdomain.through',
            'source': 'epp_oth_meril_scientific_subdomain',
            'bound': 'organisation',
            'fields': {
                'merilsubdomain': {'.field.ref': {},
                                'source': 'merilsubdomain_id',
                                'to': 'api/v2/merilsubdomains'},
            }},
        'epp_oth_meril_scientific_subdomain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_areas_of_activity': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'activity',
            'model': 'accounts.models.Organisation.epp_oth_areas_of_activity.through',
            'source': 'epp_oth_areas_of_activity',
            'bound': 'organisation',
            'fields': {
                'activity': {'.field.ref': {},
                                'source': 'activity_id',
                                'to': 'api/v2/activities'},
            }},
        'epp_oth_areas_of_activity_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_societal_grand_challenges': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'challenge',
            'model': 'accounts.models.Organisation.epp_oth_societal_grand_challenges.through',
            'source': 'epp_oth_societal_grand_challenges',
            'bound': 'organisation',
            'fields': {
                'challenge': {'.field.ref': {},
                                'source': 'challenge_id',
                                'to': 'api/v2/challenges'},
            }},
        'epp_oth_societal_grand_challenges_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_national_roadmaps': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'state': {
            '.field.string': {},
            'default': 'draft',
            '.flag.filterable': {},
        },
        'eosc_published_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'eosc_updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'eosc_state': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.nullable.default': {},
        },
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
        'publish-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/publish-eosc/',
            ':custom_update_handler': 'agora.actions.provider_publish_eosc',
        },
        'update-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/update-eosc/',
            ':custom_update_handler': 'agora.actions.provider_update_eosc',
        },
        'approve-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/approve-eosc/',
            ':custom_update_handler': 'agora.actions.provider_approve_eosc',
        },
        'reject-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/reject-eosc/',
            ':custom_update_handler': 'agora.actions.provider_reject_eosc',
        },
        'partial_update': {
            'processors': {
                'custom_post_update': {
                    '.processor': {},
                    'module_path': 'accounts.models.PostUpdateProvider',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',
                    )},
                },
            },
        },
    },
}


TARGET_USERS = {
    '.collection.django': {},
    'model': 'service.models.TargetUser',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'user': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

CONTACT_INFORMATION = {
    '.collection.django': {},
    'model': 'owner.models.ContactInformation',
    ':permissions_namespace': 'agora.checks.ContactInformation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'created_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'first_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'last_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'email': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'phone': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'position': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'organisation': {
            '.field.ref': {},
            'source': 'organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'organisation_id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

RESOURCES = {
    '.collection.django': {},
    'model': 'service.models.Resource',
    ':permissions_namespace': 'agora.checks.Resource',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'created_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'published_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'erp_bai_0_id': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_1_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_2_service_organisation': {
            '.field.ref': {},
            'source': 'erp_bai_2_organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_bai_4_webpage': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_bai_3_service_providers': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'organisation',
            'model': 'service.models.Resource.erp_bai_3_providers.through',
            'source': 'erp_bai_3_providers',
            'bound': 'resource',
            'fields': {
                'organisation': {'.field.ref': {},
                                'source': 'organisation_id',
                                'to': 'api/v2/providers'},
            }},
        'erp_bai_3_providers_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_mri_1_description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_mri_2_tagline': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_mri_3_logo': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mri_4_mulitimedia': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_cli_5_target_users': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'target_user',
            'model': 'service.models.Resource.erp_cli_5_target_users.through',
            'source': 'erp_cli_5_target_users',
            'bound': 'resource',
            'fields': {
                'target_user': {'.field.ref': {},
                                'source': 'targetuser_id',
                                'to': 'api/v2/target-users'},
            }},
        'erp_cli_5_target_users_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_mri_5_use_cases': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'domain',
            'model': 'service.models.Resource.erp_cli_1_scientific_domain.through',
            'source': 'erp_cli_1_scientific_domain',
            'bound': 'resource',
            'fields': {
                'domain': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/domains'},
            }},
        'erp_cli_1_scientific_domain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_cli_2_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'subdomain',
            'model': 'service.models.Resource.erp_cli_2_scientific_subdomain.through',
            'source': 'erp_cli_2_scientific_subdomain',
            'bound': 'resource',
            'fields': {
                'subdomain': {'.field.ref': {},
                                'source': 'subdomain_id',
                                'to': 'api/v2/subdomains'},
            }},
        'erp_cli_2_scientific_subdomain_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_cli_3_category': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'category',
            'model': 'service.models.Resource.erp_cli_3_category.through',
            'source': 'erp_cli_3_category',
            'bound': 'resource',
            'fields': {
                'category': {'.field.ref': {},
                                'source': 'category_id',
                                'to': 'api/v2/categories'},
            }},
        'erp_cli_3_category_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_cli_4_subcategory': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'subcategory',
            'model': 'service.models.Resource.erp_cli_4_subcategory.through',
            'source': 'erp_cli_4_subcategory',
            'bound': 'resource',
            'fields': {
                'subcategory': {'.field.ref': {},
                                'source': 'subcategory_id',
                                'to': 'api/v2/subcategories'},
            }},
        'erp_cli_4_subcategory_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'erp_cli_6_access_type': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'access_type',
            'model': 'service.models.Resource.erp_cli_6_access_type.through',
            'source': 'erp_cli_6_access_type',
            'bound': 'resource',
            'fields': {
                'access_type': {'.field.ref': {},
                                'source': 'accesstype_id',
                                'to': 'api/v2/access-types'},
            }
        },
        'erp_cli_7_access_mode': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'access_mode',
            'model': 'service.models.Resource.erp_cli_7_access_mode.through',
            'source': 'erp_cli_7_access_mode',
            'bound': 'resource',
            'fields': {
                'access_mode': {'.field.ref': {},
                                'source': 'accessmode_id',
                                'to': 'api/v2/access-modes'},
            }
        },
        'erp_cli_8_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},

        'erp_mgi_1_helpdesk_webpage': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_2_user_manual': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_3_terms_of_use': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_4_privacy_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_5_access_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_6_sla_specification': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_7_training_information': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_8_status_monitoring': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_9_maintenance': {
          '.field.string': {},
          '.flag.nullable.default': {}},

        'erp_gla_1_geographical_availability': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_gla_2_language': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_rli_1_geographic_location': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'main_contact': {
            '.field.ref': {},
            'source': 'main_contact_id',
            'to': '/api/v2/contact-information',
            '.flag.nullable.default': {}},
        'public_contact': {
            '.field.ref': {},
            'source': 'public_contact_id',
            'to': '/api/v2/contact-information',
            '.flag.nullable.default': {}},
        'erp_coi_1_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.first_name',
            '.flag.nullable.default': {}},
        'erp_coi_2_last_name': {
            '.field.string': {},
            'source': 'main_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_3_email': {
            '.field.string': {},
            'source': 'main_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_4_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.phone',
            '.flag.nullable.default': {}},
        'erp_coi_5_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.position',
            '.flag.nullable.default': {}},
        'erp_coi_6_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.organisation.epp_bai_name',
            '.flag.nullable.default': {}},

        'erp_coi_7_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.first_name',
            '.flag.nullable.default': {}},
        'erp_coi_8_last_name': {
            '.field.string': {},
            'source': 'public_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_9_email': {
            '.field.string': {},
            'source': 'public_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_10_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.phone',
            '.flag.nullable.default': {}},
        'erp_coi_11_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.position',
            '.flag.nullable.default': {}},
        'erp_coi_12_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.organisation.epp_bai_name',
            '.flag.nullable.default': {}},
        'erp_coi_13_helpdesk_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_coi_14_security_contact_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mti_1_technology_readiness_level': {
            '.field.ref': {},
            'source': 'erp_mti_1_technology_readiness_level_id',
            'to': '/api/v2/trls',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_mti_2_life_cycle_status': {
            '.field.ref': {},
            'source': 'erp_mti_2_life_cycle_status_id',
            'to': '/api/v2/resource-lifecycle-statuses',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_mti_3_certifications': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_4_standards': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_5_open_source_technologies': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_6_version': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_7_last_update': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_8_changelog': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_aoi_1_order_type': {
            '.field.ref': {},
            'source': 'erp_aoi_1_order_type_id',
            'to': '/api/v2/order-types',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_aoi_2_order': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_fni_1_payment_model': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_fni_2_pricing': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'resource_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'pending_resource_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'rejected_resource_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {}},


        'adminships': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            '.flag.filterable': {},
            'model': 'service.models.ResourceAdminship',
            'source': 'resourceadminships',
            'bound': 'resource',
            'fields': {
                'id': {
                    '.field.serial': {}},
                'state': {
                    '.field.string': {},
                    '.flag.filterable': {},
                    '.flag.nowrite': {}},
                'admin_id': {
                    '.field.integer': {},
                    '.flag.nowrite': {},
                    '.flag.filterable': {}},
            }
        },
        'required_resources': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'resource',
            'model': 'service.models.Resource.required_resources.through',
            'source': 'required_resources',
            'bound': 'from_resource',
            'fields': {
                'resource': {'.field.ref': {},
                            'source': 'to_resource_id',
                            'to': 'api/v2/resources'},
            },
        },
        'related_resources': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'resource',
            'model': 'service.models.Resource.related_resources.through',
            'source': 'related_resources',
            'bound': 'from_resource',
            'fields': {
                'resource': {'.field.ref': {},
                            'source': 'to_resource_id',
                            'to': 'api/v2/resources'},
            },
        },
        'erp_dei_1_required_resources': {
            '.field.string': {},
            'source': 'required_resources_ids',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_dei_2_related_resources': {
            '.field.string': {},
            'source': 'related_resources_ids',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_dei_3_related_platforms': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_ati_1_funding_body': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'funding_body',
            'model': 'service.models.Resource.erp_ati_1_funding_body.through',
            'source': 'erp_ati_1_funding_body',
            'bound': 'resource',
            'fields': {
                'funding_body': {'.field.ref': {},
                                'source': 'fundingbody_id',
                                'to': 'api/v2/funding-bodies'},
            }
        },
        'erp_ati_2_funding_program': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'funding_program',
            'model': 'service.models.Resource.erp_ati_2_funding_program.through',
            'source': 'erp_ati_2_funding_program',
            'bound': 'resource',
            'fields': {
                'funding_program': {'.field.ref': {},
                                'source': 'fundingprogram_id',
                                'to': 'api/v2/funding-programs'},
            }
        },
        'erp_ati_3_grant_project_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'state': {
            '.field.string': {},
            'default': 'draft',
            '.flag.filterable': {},
        },
        'eosc_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
        'eosc_published_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'eosc_updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'eosc_state': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
        'create': {
            'processors': {
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateResource',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',
                    )},
                },
            },
        },
        'partial_update': {
            'processors': {
                'custom_post_update': {
                    '.processor': {},
                    'module_path': 'service.models.PostUpdateResource',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',
                    )},
                },
            },
        },
        'publish-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/publish-eosc/',
            ':custom_update_handler': 'agora.actions.resource_publish_eosc',
        },
        'update-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/update-eosc/',
            ':custom_update_handler': 'agora.actions.resource_update_eosc',
        },
        'approve-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/approve-eosc/',
            ':custom_update_handler': 'agora.actions.resource_approve_eosc',
        },
        'reject-eosc': {
            '.action.django.recipe.partial_update': {},
            'method': 'POST',
            'status_code': 200,
            'url': '/*/reject-eosc/',
            ':custom_update_handler': 'agora.actions.resource_reject_eosc',
        },
    },
}

# PUBLIC ENTITIES

PUBLIC_ORGANISATIONS = {
    '.collection.django': {},
    'model': 'accounts.models.Organisation',
    ':permissions_namespace': 'agora.checks.Organisation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
            '.flag.orderable': {},
        'created_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'published_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'epp_bai_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_abbreviation': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_website': {
            '.field.string': {},
            '.flag.nullable.default': {},
        },
        'epp_bai_legal_entity': {
            '.field.boolean': {},
            'default': False
        },
        'epp_bai_legal_status': {
            '.field.struct': {},
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/legalstatuses'},
                'id': { '.field.uuid': {}},
                'name': { '.field.string': {}},
            }},
        'epp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_cli_1_scientific_domain.through',
            'source': 'epp_cli_1_scientific_domain',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/public/domains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'domain_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'domain.name'},
            }},
        'epp_cli_2_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_cli_2_scientific_subdomain.through',
            'source': 'epp_cli_2_scientific_subdomain',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'subdomain_id',
                                'to': 'api/v2/public/subdomains'},
                'domain': {'.field.ref': {},
                                'source': 'subdomain.domain_id',
                                'to': 'api/v2/public/domains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'subdomain_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'subdomain.name'},
            }},
        'epp_cli_3_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'epp_loi_1_street_name_and_number': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_2_postal_code': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_3_city': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_4_region': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_5_country_or_territory': {
          'source': 'epp_loi_5_country_or_territory_capitalize',
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_description': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_logo': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_multimedia': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_coi_6_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.first_name',
          '.flag.nullable.default': {}},
        'epp_coi_7_last_name': {
          '.field.string': {},
          'source': 'public_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_8_email': {
          '.field.string': {},
          'source': 'public_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_9_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.phone',
          '.flag.nullable.default': {}},
        'epp_coi_10_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.position',
          '.flag.nullable.default': {}},
        'epp_mti_1_life_cycle_status': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mti_2_certifications': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_bai_hosting_legal_entity': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_participating_countries': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_affiliations': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_affiliations.through',
            'source': 'epp_oth_affiliations',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'affiliation_id',
                                'to': 'api/v2/public/affiliations'},
                'id': {
                  '.field.uuid': {},
                  'source': 'affiliation_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'affiliation.name'},
            }},
        'epp_oth_networks': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_networks.through',
            'source': 'epp_oth_networks',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'network_id',
                                'to': 'api/v2/public/networks'},
                'id': {
                  '.field.uuid': {},
                  'source': 'network_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'network.name'},
                'abbreviation': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'network.abbreviation'},
            }},
        'epp_oth_structure_type': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_structure_type.through',
            'source': 'epp_oth_structure_type',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'structure_id',
                                'to': 'api/v2/public/structures'},
                'id': {
                  '.field.uuid': {},
                  'source': 'structure_id'},
                'description': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'structure.description'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'structure.name'},
            }},
        'epp_oth_esfri_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_esfri_domain.through',
            'source': 'epp_oth_esfri_domain',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'esfridomain_id',
                                'to': 'api/v2/public/esfridomains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'esfridomain_id'},
                'description': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'esfridomain.description'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'esfridomain.name'},
            }},
        'epp_oth_esfri_type': {
            '.field.struct': {},
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/esfritypes'},
                'id': { '.field.uuid': {}},
                'name': { '.field.string': {}},
            }},
        'epp_oth_meril_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_meril_scientific_domain.through',
            'source': 'epp_oth_meril_scientific_domain',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'merildomain_id',
                                'to': 'api/v2/public/merildomains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'merildomain_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'merildomain.name'},
            }},
        'epp_oth_meril_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_meril_scientific_subdomain.through',
            'source': 'epp_oth_meril_scientific_subdomain',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'merilsubdomain_id',
                                'to': 'api/v2/public/merilsubdomains'},
                'domain': {'.field.ref': {},
                                'source': 'merilsubdomain.domain_id',
                                'to': 'api/v2/public/merildomains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'merilsubdomain_id'},
                'description': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'merilsubdomain.description'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'merilsubdomain.name'},
            }},
        'epp_oth_areas_of_activity': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_areas_of_activity.through',
            'source': 'epp_oth_areas_of_activity',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'activity_id',
                                'to': 'api/v2/public/activities'},
                'id': {
                  '.field.uuid': {},
                  'source': 'activity_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'activity.name'},
            }},
        'epp_oth_societal_grand_challenges': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'accounts.models.Organisation.epp_oth_societal_grand_challenges.through',
            'source': 'epp_oth_societal_grand_challenges',
            'bound': 'organisation',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'challenge_id',
                                'to': 'api/v2/public/challenges'},
                'id': {
                  '.field.uuid': {},
                  'source': 'challenge_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'challenge.name'},
            }},
        'epp_oth_national_roadmaps': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}


PUBLIC_RESOURCES = {
    '.collection.django': {},
    'model': 'service.models.Resource',
    ':permissions_namespace': 'agora.checks.Resource',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'created_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'updated_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'published_at': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'erp_bai_0_id': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_1_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_2_organisation': {
            '.field.ref': {},
            'to': '/api/v2/public/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {},
            '.flag.noread': {}},
        'erp_bai_2_organisation_public': {
            '.field.ref': {},
            'to': '/api/v2/public/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_bai_3_providers_public': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
             'id_field': 'href',
            'model': 'service.models.Organisation',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/providers'},
                'id': {
                  '.field.uuid': {}},
                'epp_bai_id': {
                  '.field.string': {}},
                'epp_bai_name': {
                  '.field.string': {}},
            },
        },
        'erp_bai_4_webpage': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mri_1_description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_mri_2_tagline': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_mri_3_logo': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mri_4_mulitimedia': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_cli_5_target_users': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_5_target_users.through',
            'source': 'erp_cli_5_target_users',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'targetuser_id',
                                'to': 'api/v2/public/target-users'},
                'id': {
                  '.field.uuid': {},
                  'source': 'targetuser_id'},
                'user': {
                  '.field.string': {},
                  'source': 'targetuser.user'},
                'description': {
                  '.field.string': {},
                  'source': 'targetuser.description'},
            }},
        'erp_mri_5_use_cases': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_1_scientific_domain.through',
            'source': 'erp_cli_1_scientific_domain',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/public/domains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'domain_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'domain.name'},
            }},
        'erp_cli_2_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_2_scientific_subdomain.through',
            'source': 'erp_cli_2_scientific_subdomain',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'subdomain_id',
                                'to': 'api/v2/public/subdomains'},
                'domain': {'.field.ref': {},
                                'source': 'subdomain.domain_id',
                                'to': 'api/v2/public/domains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'subdomain_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'subdomain.name'},
            }},
        'erp_cli_3_category': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_3_category.through',
            'source': 'erp_cli_3_category',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'category_id',
                                'to': 'api/v2/public/categories'},
                'id': {
                  '.field.uuid': {},
                  'source': 'category_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'category.name'},
                'supercategory': {'.field.ref': {},
                                'source': 'category.supercategory_id',
                                'to': 'api/v2/public/supercategories'},
            }},
        'erp_cli_4_subcategory': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_4_subcategory.through',
            'source': 'erp_cli_4_subcategory',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'subcategory_id',
                                'to': 'api/v2/public/subcategories'},
                'id': {
                  '.field.uuid': {},
                  'source': 'subcategory_id'},
                'name': {
                  '.field.string': {},
                  'source': 'subcategory.name'},
                'category': {'.field.ref': {},
                                'source': 'subcategory.category_id',
                                'to': 'api/v2/public/categories'},
            }},
        'erp_cli_6_access_type': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_6_access_type.through',
            'source': 'erp_cli_6_access_type',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'accesstype_id',
                                'to': 'api/v2/public/access-types'},
                'id': {
                  '.field.uuid': {},
                  'source': 'accesstype_id'},
                'name': {
                  '.field.string': {},
                  'source': 'accesstype.name'},
                'description': {
                  '.field.string': {},
                  'source': 'accesstype.description'},
            }
        },
        'erp_cli_7_access_mode': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_7_access_mode.through',
            'source': 'erp_cli_7_access_mode',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'accessmode_id',
                                'to': 'api/v2/public/access-modes'},
                'id': {
                  '.field.uuid': {},
                  'source': 'accessmode_id'},
                'name': {
                  '.field.string': {},
                  'source': 'accessmode.name'},
                'description': {
                  '.field.string': {},
                  'source': 'accessmode.description'},
            }
        },
        'erp_cli_8_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},

        'erp_mgi_1_helpdesk_webpage': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_2_user_manual': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_3_terms_of_use': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_4_privacy_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_5_access_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_6_sla_specification': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_7_training_information': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_8_status_monitoring': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_9_maintenance': {
          '.field.string': {},
          '.flag.nullable.default': {}},

        'erp_gla_1_geographical_availability': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_gla_2_language': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_rli_1_geographic_location': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_coi_7_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.first_name',
            '.flag.nullable.default': {}},
        'erp_coi_8_last_name': {
            '.field.string': {},
            'source': 'public_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_9_email': {
            '.field.string': {},
            'source': 'public_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_10_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.phone',
            '.flag.nullable.default': {}},
        'erp_coi_11_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.position',
            '.flag.nullable.default': {}},
        'erp_coi_12_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.organisation.epp_bai_name',
            '.flag.nullable.default': {}},
        'erp_coi_13_helpdesk_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_coi_14_security_contact_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mti_1_technology_readiness_level': {
            '.field.struct': {},
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/trls'},
                'id': { '.field.uuid': {}},
                'name': { '.field.string': {}},
                'description': { '.field.string': {}},
            }},
        'erp_mti_2_life_cycle_status': {
            '.field.ref': {},
            'source': 'erp_mti_2_life_cycle_status_id',
            'to': '/api/v2/resource-lifecycle-statuses',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_mti_3_certifications': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_4_standards': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_5_open_source_technologies': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_6_version': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_7_last_update': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_8_changelog': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_aoi_1_order_type': {
            '.field.struct': {},
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/order-types'},
                'id': { '.field.uuid': {}},
                'name': { '.field.string': {}},
                'description': { '.field.string': {}},
            }},
        'erp_aoi_2_order': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_fni_1_payment_model': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_fni_2_pricing': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_dei_1_required_resources_public': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
             'id_field': 'href',
            'model': 'service.models.Organisation',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/resources'},
                'id': {
                  '.field.uuid': {},
                },
                'erp_bai_0_id': {
                  '.field.string': {}},
                'erp_bai_1_name': {
                  '.field.string': {}},
            }
        },
        'erp_dei_2_related_resources_public': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
             'id_field': 'href',
            'model': 'service.models.Organisation',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'id',
                                'to': 'api/v2/public/resources'},
                'id': {
                  '.field.uuid': {},
                },
                'erp_bai_0_id': {
                  '.field.string': {}},
                'erp_bai_1_name': {
                  '.field.string': {}},
            }
        },
        'erp_dei_3_related_platforms': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_ati_1_funding_body': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'id_field': 'id',
            'model': 'service.models.Resource.erp_ati_1_funding_body.through',
            'source': 'erp_ati_1_funding_body',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'fundingbody_id',
                                'to': 'api/v2/public/funding-bodies'},
                'id': {
                  '.field.uuid': {},
                  'source': 'fundingbody_id'},
                'name': {
                  '.field.string': {},
                  'source': 'fundingbody.name'},

            }
        },
        'erp_ati_2_funding_program': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'id_field': 'id',
            'model': 'service.models.Resource.erp_ati_2_funding_program.through',
            'source': 'erp_ati_2_funding_program',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'fundingprogram_id',
                                'to': 'api/v2/public/funding-programs'},
                'id': {
                  '.field.uuid': {},
                  'source': 'fundingprogram_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'fundingprogram.name'},
            }
        },
        'erp_ati_3_grant_project_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

PUBLIC_ORGANISATIONS_LITE = {
    '.collection.django': {},
    'model': 'accounts.models.Organisation',
    ':permissions_namespace': 'agora.checks.Organisation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
            '.flag.orderable': {},
        'epp_bai_id': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_abbreviation': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
        },
        'epp_bai_website': {
            '.field.string': {},
            '.flag.nullable.default': {},
        },
        'epp_cli_3_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'epp_loi_1_street_name_and_number': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_2_postal_code': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_3_city': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_5_country_or_territory': {
          'source': 'epp_loi_5_country_or_territory_capitalize',
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_logo': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_bai_hosting_legal_entity': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_oth_participating_countries': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

PUBLIC_RESOURCES_LITE = {
    '.collection.django': {},
    'model': 'service.models.Resource',
    ':permissions_namespace': 'agora.checks.Resource',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'erp_bai_0_id': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_1_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_mri_2_tagline': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_bai_2_organisation': {
            '.field.ref': {},
            'to': '/api/v2/public/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {},
            '.flag.noread': {}},
        'erp_mri_3_logo': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_1_scientific_domain.through',
            'source': 'erp_cli_1_scientific_domain',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/public/domains'},
                'id': {
                  '.field.uuid': {},
                  'source': 'domain_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'domain.name'},
            }},
        'erp_cli_3_category': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'id_field': 'id',
            'model': 'service.models.Resource.erp_cli_3_category.through',
            'source': 'erp_cli_3_category',
            'bound': 'resource',
            'fields': {
                'href': {'.field.ref': {},
                                'source': 'category_id',
                                'to': 'api/v2/public/categories'},
                'id': {
                  '.field.uuid': {},
                  'source': 'category_id'},
                'name': {
                  '.field.string': {},
                  '.flag.nowrite': {},
                  'source': 'category.name'},
                'supercategory': {'.field.ref': {},
                                'source': 'category.supercategory_id',
                                'to': 'api/v2/public/supercategories'},
            }
        }},
        'erp_cli_8_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

APP_CONFIG = {
    '.apimas_app': {},
    ':permission_rules': 'agora.permissions.get_rules',
    ':authenticator': 'apimas.auth.DjoserAuthentication',
    ':verifier': 'agora.utils.djoser_verifier',
    ':user_resolver': 'agora.utils.userid_extractor',
    ':permissions_namespace': 'agora.checks',
    ':filter_compat': True,
    ':ordering_compat': True,

    'endpoints': {
        'public_api': {
          'prefix': 'api/v2/public',
          'collections': {
            'resources': PUBLIC_RESOURCES,
            'resources-lite': PUBLIC_RESOURCES_LITE,
            'providers': PUBLIC_ORGANISATIONS,
            'providers-lite': PUBLIC_ORGANISATIONS_LITE,
            'legalstatuses': LEGAL_STATUSES,
            'affiliations': AFFILIATIONS,
            'networks': NETWORKS,
            'structures': STRUCTURES,
            'esfridomains': ESFRI_DOMAINS,
            'esfritypes': ESFRI_TYPES,
            'activities': ACTIVITIES,
            'order-types': ORDER_TYPES,
            'challenges': CHALLENGES,
            'domains': DOMAINS,
            'subdomains': SUBDOMAINS,
            'supercategories': SUPERCATEGORIES,
            'categories': CATEGORIES,
            'subcategories': SUBCATEGORIES,
            'funding-programs': FUNDING_PROGRAMS,
            'funding-bodies': FUNDING_BODIES,
            'access-types': ACCESS_TYPES,
            'access-modes': ACCESS_MODES,
            'trls': TRLS,
            'resource-lifecycle-statuses': RESOURCE_LIFECYCLE_STATUSES,
            'merildomains': MERIL_DOMAINS,
            'merilsubdomains': MERIL_SUBDOMAINS,
            'target-users': TARGET_USERS,
          }
        },
        'api': {
            'prefix': 'api/v2',
            'collections': {
                'resource-admins': RESOURCE_ADMINS,
                'custom-users': CUSTOM_USERS,
                'providers': ORGANISATIONS,
                'resources': RESOURCES,
                'multimedia': MULTIMEDIA,
                'target-users': TARGET_USERS,
                'contact-information': CONTACT_INFORMATION,
                'legalstatuses': LEGAL_STATUSES,
                'affiliations': AFFILIATIONS,
                'networks': NETWORKS,
                'structures': STRUCTURES,
                'esfridomains': ESFRI_DOMAINS,
                'esfritypes': ESFRI_TYPES,
                'activities': ACTIVITIES,
                'order-types': ORDER_TYPES,
                'challenges': CHALLENGES,
                'domains': DOMAINS,
                'subdomains': SUBDOMAINS,
                'supercategories': SUPERCATEGORIES,
                'categories': CATEGORIES,
                'subcategories': SUBCATEGORIES,
                'funding-programs': FUNDING_PROGRAMS,
                'funding-bodies': FUNDING_BODIES,
                'access-types': ACCESS_TYPES,
                'access-modes': ACCESS_MODES,
                'trls': TRLS,
                'resource-lifecycle-statuses': RESOURCE_LIFECYCLE_STATUSES,
                'merildomains': MERIL_DOMAINS,
                'merilsubdomains': MERIL_SUBDOMAINS,
            },
        },
    },
}
