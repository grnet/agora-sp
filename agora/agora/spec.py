  # djoser_verifier: agora.utils.djoser_verifier
  # userid_extractor: agora.utils.userid_extractor

SERVICE_FIELDS_COMMON = {
    'id': {
        '.field.uuid': {},
        '.flag.nowrite': {}},
    'name': {
        '.field.string': {},
        '.flag.filterable': {},
        '.flag.searchable': {},
        '.flag.orderable': {}},
    'url': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'endpoint': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'description': {
        '.field.string': {},
        '.flag.searchable': {},
        'source': 'short_description',
        '.flag.nullable.default': {}},
    'tagline': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'service_type': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'user_value': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'target_customers': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'target_users': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'screenshots_videos': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'languages': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'standards': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'certifications': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'customer_facing': {
        '.flag.filterable': {},
        '.field.boolean': {}},
    'internal': {
        '.flag.filterable': {},
        '.field.boolean': {}},
    'tags': {
        '.field.string': {},
        '.flag.searchable': {},
        '.flag.nullable.default': {}},
    'scientific_fields': {
        '.field.string': {},
        '.flag.searchable': {},
        '.flag.nullable.default': {}},
    'helpdesk': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'order': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'order_type': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'changelog': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'last_update': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {}},
    'created_at': {
        '.field.datetime': {},
        '.flag.nullable': {},
        '.flag.nowrite': {}},
    'updated_at': {
        '.field.datetime': {},
        '.flag.nullable': {},
        '.flag.nowrite': {}},
    'service_categories_names': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'providers_names': {
        '.field.string': {},
        'source': 'organisations_names',
        '.flag.nowrite': {}},
    'other_required_services': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'other_related_services': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'related_platform': {
        '.field.string': {},
        '.flag.nullable.default': {}},
}


SERVICE_FIELDS_INT = {
    'logo': {
        '.field.file': {},
        'default': ''},
    'owner_name': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'owner_contact': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'support_name': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'support_contact': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'security_name': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'security_contact': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'pending_service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'rejected_service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'service_categories': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'service_category',
        'model': 'service.models.Service.service_categories.through',
        'source': 'service_categories',
        'bound': 'service',
        'fields': {
            'service_category': {'.field.ref': {},
                                 'source': 'servicecategory_id',
                                 'to': 'api/v2/service-categories'},
        },
    },
    'providers': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'organisation',
        'model': 'service.models.Service.organisations.through',
        'source': 'organisations',
        'bound': 'service',
        'fields': {
            'organisation': {'.field.ref': {},
                            'source': 'organisation_id',
                            'to': 'api/v2/providers'},
        }
    },
    'adminships': {
        '.field.collection.django': {},
        ':filter_compat': True,
        '.flag.nullable.default': {},
        '.flag.filterable': {},
        'model': 'service.models.ServiceAdminship',
        'source': 'serviceadminships',
        'bound': 'service',
        'fields': {
            'id': {
                '.field.serial': {}},
            'user_id': {
                '.field.integer': {},
                '.flag.nowrite': {},
                '.flag.filterable': {},
                'source': 'admin.pk'},
        }
    },

    'required_services': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'service',
        'model': 'service.models.Service.required_services.through',
        'source': 'required_services',
        'bound': 'from_service',
        'fields': {
            'service': {'.field.ref': {},
                        'source': 'to_service_id',
                        'to': 'api/v2/services'},
        },
    },
    'related_services': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'service',
        'model': 'service.models.Service.related_services.through',
        'source': 'related_services',
        'bound': 'from_service',
        'fields': {
            'service': {'.field.ref': {},
                        'source': 'to_service_id',
                        'to': 'api/v2/services'},
        },
    },
}

SERVICE_FIELDS_EXT = {
    # extended keys
    'logo': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'logo_absolute_path'},
    'related_services_names': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'required_services_names': {
        '.field.string': {},
        '.flag.nowrite': {}},
}

SERVICE_FIELDS_INTERNAL = dict(SERVICE_FIELDS_COMMON, **SERVICE_FIELDS_INT)
SERVICE_FIELDS_EXTERNAL = dict(SERVICE_FIELDS_COMMON, **SERVICE_FIELDS_EXT)

USERS = {
    '.collection.django': {},
    'model': 'accounts.models.User',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'username': {
            '.flag.orderable': {},
            '.field.string': {}},
        'email': {
            '.flag.orderable': {},
            '.field.string': {}},
        'first_name': {
            '.field.string': {}},
        'last_name': {
            '.field.string': {}},
        'is_staff': {
            '.field.boolean': {}},
        'is_active': {
            '.flag.orderable': {},
            '.field.boolean': {}},
        'date_joined': {
            '.field.string': {}},
        'avatar': {
            '.field.file': {},
            'default': ''},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    }
}

USER_CUSTOMERS = {
    '.collection.django': {},
    'model': 'service.models.UserCustomer',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.ref': {},
            'source': 'name_id',
            'to': 'api/v2/user-roles'},
        'role': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_id': {
            '.field.ref': {},
            'source': 'service_id_id',
            '.flag.filterable': {},
            'to': 'api/v2/services'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    }
}

SERVICE_DEPENDSON_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service_DependsOn_Service',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service_one': {
            '.field.ref': {},
            'source': 'id_service_one_id',
            'to': '/api/v2/service'},
        'id_service_two': {
            '.field.ref': {},
            'source': 'id_service_two_id',
            'to': '/api/v2/service'},
    }
}

SERVICE_EXTERNAL_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service_ExternalService',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service': {
            '.field.ref': {},
            'source': 'id_service_id',
            'to': '/api/v2/service'},
        'id_external_service': {
            '.field.ref': {},
            'source': 'id_external_service_id',
            'to': '/api/v2/external_service'},
    }
}

SERVICE_STATUS = {
    '.collection.django': {},
    'model': 'service.models.ServiceStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'value': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.filterable': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {},
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

SERVICE_TRLS = {
    '.collection.django': {},
    'model': 'service.models.ServiceTrl',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'value': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'order': {
            '.field.integer': {}},
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

EXTERNAL_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.ExternalService',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {}},
        'description': {
            '.field.string': {}},
        'service': {
            '.field.string': {}},
        'details': {
            '.field.string': {}},
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

USER_ROLES = {
    '.collection.django': {},
    'model': 'service.models.UserRole',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.flag.orderable': {},
            '.field.string': {}},
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

SERVICE_CATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.ServiceCategory',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'icon': {
            '.field.file': {},
            'default': ''},
        'icon_absolute_path': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'description': {
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

SERVICE_OWNERS = {
    '.collection.django': {},
    'model': 'owner.models.ServiceOwner',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'first_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'email': {
            '.field.email': {},
            '.flag.nullable.default': {}},
        'phone': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'id_service_owner': {
            '.field.ref': {},
            'source': 'id_service_owner_id',
            'to': '/api/v2/institutions'},
        'id_account': {
            '.field.ref': {},
            'source': 'id_account_id',
            'to': '/api/v2/custom-users'},
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
        'avatar': {
            '.field.file': {},
            'default': ''},
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


INSTITUTIONS = {
    '.collection.django': {},
    'model': 'owner.models.Institution',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'address': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'country': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'department': {
            '.field.string': {},
            '.flag.orderable': {},
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

COMPONENTS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponent',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'logo': {
            '.field.file': {},
            'default': ''},
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

COMPONENT_IMPLEMENTATIONS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.field.ref': {},
            'source': 'component_id_id',
            'to': '/api/v2/components',
            '.flag.filterable': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
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

COMPONENT_IMPLEMENTATION_DETAILS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementationDetail',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'component_id_id',
            'to': '/api/v2/components'},
        'component_implementation_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'component_implementation_id_id',
            'to': '/api/v2/component-implementations'},
        'version': {
            '.field.string': {},
            '.flag.orderable': {},
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

COMPONENT_IMPLEMENTATION_DETAIL_LINKS = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    ':permissions_namespace': 'agora.checks.CIDL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'service_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_id_id',
            'to': '/api/v2/services'},
        'service_details_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_details_id_id',
            'to': '/api/v2/service-versions'},
        'service_component_implementation_detail_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_component_implementation_detail_id_id',
            'to': '/api/v2/component-implementation-details'},
        'service_type': {
            '.flag.searchable': {},
            '.field.string': {},
            '.flag.nullable.default': {}},
        'configuration_parameters': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {},
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


EXT_COMPONENTS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementationDetail',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_category': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_id.name'},
        'component_category_description': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_id.description'},
        'component_description': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_implementation_id.description'},
        'component_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_implementation_id.name'},
        'component_version': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {},
            'source': 'version'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}


EXT_COMPONENT_CONNECTIONS = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    ':permissions_namespace': 'agora.checks.CIDL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.field.uuid': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.id'},
        'component_version': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.version'},
        'component_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.component_implementation_id.name'},
        'component_category': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.component_implementation_id.component_id.name'},
        'service_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_id.name'},
        'service_id': {
            '.field.uuid': {},
            '.flag.filterable': {},
            'source': 'service_id.id'},
        'service_version': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_details_id.version'},
        'service_type': {
            '.flag.searchable': {},
            '.field.string': {},
            '.flag.nullable.default': {}},
        'configuration_parameters': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_INTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},

        'delete': {
            'processors': {
                'post_delete_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostDeleteMessage',
                    'read_keys': {'=': (
                        'backend/instance',
                        'guards/transaction_commit',
                    )},
                    'write_keys': {'=': (
                        'guards/transaction_commit',
                    )},
                },
            },
        },
        'update': {
            'processors': {
                'post_update_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostUpdateMessage',
                    'read_keys': {'=': (
                        'response/content',
                    )},
                    'write_keys': {'=': (
                        'response/content',
                    )},
                },
            },
        },
        'partial_update': {
            'processors': {
                'post_partial_update_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostUpdateMessage',
                    'read_keys': {'=': (
                        'response/content',
                    )},
                    'write_keys': {'=': (
                        'response/content',
                    )},
                },
            },
        },
        'create': {
            'processors': {
                'post_create_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateMessage',
                    'read_keys': {'=': (
                        'response/content',
                    )},
                    'write_keys': {'=': (
                        'response/content',
                    )},
                },
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateService',
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


EXT_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}


SERVICES_MARKETPLACE = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICES_CATALOGUE = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICE_TYPES_FIELDS = {
    'id': {
        '.field.uuid': {},
        '.flag.nowrite': {}},
    'service_name': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'service_id.name'},
    'service_type': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'in_catalogue': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.is_in_catalogue'},
    'visible_to_marketplace': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.visible_to_marketplace'},
    'external_service': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.customer_facing'},
    'internal_service': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.internal'},
    'service_tagline': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.tagline'},
    'service_description': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.short_description'},
    'service_category': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.service_category.name'},
    'service_version': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.version'},
    'component_name': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_component_implementation_detail_id.component_id.name'},
    'component_version': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_component_implementation_detail_id.version'},
    'service_id': {
        '.field.uuid': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.id'},


}

SERVICE_TYPES = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    'fields': SERVICE_TYPES_FIELDS,
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

SERVICE_VERSIONS = {
    '.collection.django': {},
    'model': 'service.models.ServiceDetails',
    ':permissions_namespace': 'agora.checks.ServiceVersion',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service': {
            '.field.ref': {},
            'source': 'id_service_id',
            'to': '/api/v2/services',
            '.flag.filterable': {}},
        'service_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'status': {
            '.field.ref': {},
            'source': 'status_id',
            'to': '/api/v2/service-status',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'version': {
            '.flag.orderable': {},
            '.field.string': {}},
        'terms_of_use_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'privacy_policy_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'user_manual': {
            '.field.string': {},
            'source': 'user_documentation_url',
            #'.flag.blankable': {},
            '.flag.nullable.default': {}},
        'admin_manual': {
            '.field.string': {},
            'source': 'operations_documentation_url',
            '.flag.nullable.default': {}},
        'monitoring_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'is_in_catalogue': {
            '.flag.filterable': {},
            '.flag.orderable': {},
            '.field.boolean': {},
            'default': False},
        'visible_to_marketplace': {
            '.flag.filterable': {},
            '.flag.orderable': {},
            '.field.boolean': {},
            'default': False},
        'sla_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'training_information': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'maintenance_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_trl': {
            '.field.ref': {},
            'source': 'service_trl_id',
            'to': '/api/v2/service-trls',
            '.flag.orderable': {},
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'created_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'updated_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        # extended fields
        'id_service_ext': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nowrite': {},
            'source': 'id_service.name'},
        'status_ext': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nowrite': {},
            'source': 'status.value'},
        'access_policies': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'access_policy',
            'model': 'service.models.ServiceDetails.access_policies.through',
            'source': 'access_policies',
            'bound': 'servicedetails',
            'fields': {
                'access_policy': {'.field.ref': {},
                                'source': 'accesspolicy_id',
                                'to': 'api/v2/access-policies'},
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
            'source': 'resource.rd_bai_1_name'},
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
         'contact': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'logo': {
            '.field.file': {},
            'default': ''},
        'pd_bai_3_legal_entity': {
          '.field.boolean': {},
          'default': False},
        'pd_bai_0_id': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_bai_1_name': {
          '.field.string': {},
          '.flag.filterable': {},
          '.flag.searchable': {},
        },
        'pd_bai_2_abbreviation': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_bai_3_legal_status': {
          '.field.string': {}},
        'pd_bai_4_website': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_loi_1_street_name_and_number': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_loi_2_postal_code': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_loi_3_city': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_loi_4_region': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_loi_5_country_or_territory': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_mri_1_description': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_mri_2_logo': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_mri_3_multimedia': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
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
        'pd_coi_1_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.first_name',
          '.flag.nullable.default': {}},
        'pd_coi_2_last_name': {
          '.field.string': {},
          'source': 'main_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'pd_coi_3_email': {
          '.field.string': {},
          'source': 'main_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'pd_coi_4_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.phone',
          '.flag.nullable.default': {}},
        'pd_coi_5_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.position',
          '.flag.nullable.default': {}},
        'pd_coi_6_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.first_name',
          '.flag.nullable.default': {}},
        'pd_coi_7_last_name': {
          '.field.string': {},
          'source': 'public_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'pd_coi_8_email': {
          '.field.string': {},
          'source': 'public_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'pd_coi_9_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.phone',
          '.flag.nullable.default': {}},
        'pd_coi_10_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.position',
          '.flag.nullable.default': {}},
        'pd_mti_1_life_cycle_status': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'pd_mti_2_certifications': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'pd_oth_1_hosting_legal_entity': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'pd_oth_2_participating_countries': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'pd_oth_3_affiliations': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'affiliation',
            'model': 'accounts.models.Organisation.pd_oth_3_affiliations.through',
            'source': 'pd_oth_3_affiliations',
            'bound': 'organisation',
            'fields': {
                'affiliation': {'.field.ref': {},
                                'source': 'affiliation_id',
                                'to': 'api/v2/affiliations'},
            }},
        'affiliation_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'pd_oth_4_networks': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'network',
            'model': 'accounts.models.Organisation.pd_oth_4_networks.through',
            'source': 'pd_oth_4_networks',
            'bound': 'organisation',
            'fields': {
                'network': {'.field.ref': {},
                                'source': 'network_id',
                                'to': 'api/v2/networks'},
            }},
        'network_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'pd_oth_5_structure_type': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'structure',
            'model': 'accounts.models.Organisation.pd_oth_5_structure_type.through',
            'source': 'pd_oth_5_structure_type',
            'bound': 'organisation',
            'fields': {
                'structure': {'.field.ref': {},
                                'source': 'structure_id',
                                'to': 'api/v2/structures'},
            }},
        'structure_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'pd_oth_6_esfri_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'esfridomain',
            'model': 'accounts.models.Organisation.pd_oth_6_esfri_domain.through',
            'source': 'pd_oth_6_esfri_domain',
            'bound': 'organisation',
            'fields': {
                'esfridomain': {'.field.ref': {},
                                'source': 'esfridomain_id',
                                'to': 'api/v2/esfridomains'},
            }},
        'esfridomain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'pd_oth_7_esfri_type': {
            '.field.ref': {},
            'source': 'pd_oth_7_esfri_type_id',
            'to': '/api/v2/esfritypes',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},

        'pd_oth_8_areas_of_activity': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'activity',
            'model': 'accounts.models.Organisation.pd_oth_8_areas_of_activity.through',
            'source': 'pd_oth_8_areas_of_activity',
            'bound': 'organisation',
            'fields': {
                'activity': {'.field.ref': {},
                                'source': 'activity_id',
                                'to': 'api/v2/activities'},
            }},
        'activity_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'pd_oth_9_societal_grand_challenges': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'challenge',
            'model': 'accounts.models.Organisation.pd_oth_9_societal_grand_challenges.through',
            'source': 'pd_oth_9_societal_grand_challenges',
            'bound': 'organisation',
            'fields': {
                'challenge': {'.field.ref': {},
                                'source': 'challenge_id',
                                'to': 'api/v2/challenges'},
            }},
        'challenge_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'pd_oth_10_national_roadmaps': {
          '.field.string': {},
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
    },
}


MY_ORGANISATIONS = {
    '.collection.django': {},
    'model': 'service.models.Organisation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    ':permissions_namespace': 'agora.checks.Organisation',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

ACCESS_POLICIES = {
    '.collection.django': {},
    'model': 'service.models.AccessPolicy',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'access_mode': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'payment_model': {
            '.field.string': {},
            '.flag.nullable.default': {}},
       'pricing': {
            '.field.string': {},
            '.flag.nullable.default': {}},
       'conditions': {
            '.field.string': {},
            '.flag.nullable.default': {}},
       'geo_availability': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
       'access_policy_url': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
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


FEDERATION_MEMBERS = {
    '.collection.django': {},
    'model': 'service.models.FederationMember',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'webpage': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'logo': {
            '.field.file': {},
            'default': ''},
        'country': {
            '.field.string': {},
            '.flag.orderable': {},
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
            '.flag.orderable': {}},
        'description': {
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


CONTACT_INFORMATION = {
    '.collection.django': {},
    'model': 'owner.models.ContactInformation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
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
            '.flag.searchable': {}},
        'position': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'organisation': {
            '.field.ref': {},
            'source': 'organisation_id',
            'to': '/api/v2/providers',
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
        'rd_bai_0_id': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'rd_bai_1_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'rd_bai_2_service_organisation': {
            '.field.ref': {},
            'source': 'rd_bai_2_organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'rd_bai_4_webpage': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'rd_bai_3_service_providers': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'organisation',
            'model': 'service.models.Resource.rd_bai_3_providers.through',
            'source': 'rd_bai_3_providers',
            'bound': 'resource',
            'fields': {
                'organisation': {'.field.ref': {},
                                'source': 'organisation_id',
                                'to': 'api/v2/providers'},
            }},
        'providers_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'rd_mri_1_description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'rd_mri_2_tagline': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'rd_mri_3_logo': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'rd_mri_4_mulitimedia': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'rd_mri_5_target_users': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'target_user',
            'model': 'service.models.Resource.rd_mri_5_target_users.through',
            'source': 'rd_mri_5_target_users',
            'bound': 'resource',
            'fields': {
                'target_user': {'.field.ref': {},
                                'source': 'targetuser_id',
                                'to': 'api/v2/target-users'},
            }},
        'rd_mri_5_target_users_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'rd_mri_6_target_customer_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'rd_mri_7_use_cases': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},

        'rd_mgi_1_helpdesk_webpage': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_2_helpdesk_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_3_user_manual': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_4_terms_of_use': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_5_privacy_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_6_sla_specification': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_7_training_information': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_8_status_monitoring': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'rd_mgi_9_maintenance': {
          '.field.string': {},
          '.flag.nullable.default': {}},

        'rd_gla_1_geographical_availability': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'rd_gla_2_language': {
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
        'rd_coi_1_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.first_name',
            '.flag.nullable.default': {}},
        'rd_coi_2_last_name': {
            '.field.string': {},
            'source': 'main_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'rd_coi_3_email': {
            '.field.string': {},
            'source': 'main_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'rd_coi_4_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.phone',
            '.flag.nullable.default': {}},
        'rd_coi_5_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.position',
            '.flag.nullable.default': {}},
        'rd_coi_6_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.organisation.name',
            '.flag.nullable.default': {}},

        'rd_coi_7_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.first_name',
            '.flag.nullable.default': {}},
        'rd_coi_8_last_name': {
            '.field.string': {},
            'source': 'public_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'rd_coi_9_email': {
            '.field.string': {},
            'source': 'public_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'rd_coi_10_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.phone',
            '.flag.nullable.default': {}},
        'rd_coi_11_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.position',
            '.flag.nullable.default': {}},
        'rd_coi_12_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.organisation.name',
            '.flag.nullable.default': {}},
        'resource_admins_ids': {
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
                'user_id': {
                    '.field.integer': {},
                    '.flag.nowrite': {},
                    '.flag.filterable': {},
                    'source': 'admin.pk'},
            }
        },
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
        'api': {
            'prefix': 'api/v2',
            'collections': {
                'resource-admins': RESOURCE_ADMINS,
                'custom-users': CUSTOM_USERS,
                'providers': ORGANISATIONS,
                'resources': RESOURCES,
                'target-users': TARGET_USERS,
                'contact-information': CONTACT_INFORMATION,
                'affiliations': AFFILIATIONS,
                'networks': NETWORKS,
                'structures': STRUCTURES,
                'esfridomains': ESFRI_DOMAINS,
                'esfritypes': ESFRI_TYPES,
                'activities': ACTIVITIES,
                'challenges': CHALLENGES,
                'domains': DOMAINS,
                'subdomains': SUBDOMAINS,
            },
        },
    },
}
