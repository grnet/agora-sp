DEPLOY_CONFIG = {
    ':root_url': 'https://snf-789670.vm.okeanos.grnet.gr',
}

  # djoser_verifier: agora.utils.djoser_verifier
  # userid_extractor: agora.utils.userid_extractor

APP_CONFIG = {
    '.apimas_app': {},
    ':permission_rules': 'agora.utils.get_rules',
    ':authenticator': 'apimas.auth.DjoserAuthentication',
    ':verifier': 'agora.utils.djoser_verifier',
    ':user_resolver': 'agora.utils.userid_extractor',

    'endpoints': {
        'api/v2': {
            'collections': {
                'users': {
                    '.field.collection.django': {},
                    'model': 'accounts.models.User',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'username': {
                            '.field.string': {}},
                        'email': {
                            '.field.string': {}},
                        'first_name': {
                            '.field.string': {}},
                        'last_name': {
                            '.field.string': {}},
                        'is_staff': {
                            '.field.boolean': {}},
                        'is_active': {
                            '.field.boolean': {}},
                        'date_joined': {
                            '.field.string': {}},
                        'avatar': {
                            '.field.file': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                        }
                },

                'services': {
                    '.field.collection.django': {},
                    'model': 'service.models.Service',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.string': {},
                            '.flag.filterable': {},
                            '.flag.orderable': {}},
                        'short_description': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'description_external': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'description_internal': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'service_area': {
                            '.field.ref': {},
                            'to': '/api/v2/service-areas',
                            '.flag.nullable': {},
                            '.flag.orderable': {},
                            '.flag.filterable': {}},
                        'service_type': {
                            '.field.string': {},
                            '.flag.nullable': {},
                            '.flag.filterable': {}},
                        'service_trl': {
                            '.field.ref': {},
                            'to': '/api/v2/service-trls',
                            '.flag.orderable': {},
                            '.flag.filterable': {},
                            '.flag.nullable': {}},
                        'request_procedures': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'funders_for_service': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'value_to_customer': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'risks': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'competitors': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'id_service_owner': {
                            '.field.ref': {},
                            'to': '/api/v2/service-owners',
                            '.flag.nullable': {}},
                        'id_contact_information': {
                            '.field.ref': {},
                            'to': '/api/v2/contact-information',
                            '.flag.nullable': {}},
                        'id_contact_information_internal': {
                            '.field.ref': {},
                            'to': '/api/v2/contact-information',
                            '.flag.nullable': {}},
                        'logo': {
                            '.field.file': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'service-versions': {
                    '.field.collection.django': {},
                    'model': 'service.models.ServiceDetails',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'id_service': {
                            '.field.ref': {},
                            'to': '/api/v2/services',
                            '.flag.filterable': {}},
                        'status': {
                            '.field.ref': {},
                            'to': '/api/v2/service-status',
                            '.flag.filterable': {},
                            '.flag.nullable': {}},
                        'version': {
                            '.field.string': {}},
                        'features_current': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'features_future': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'usage_policy_has': {
                            '.field.boolean': {}},
                        'usage_policy_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'privacy_policy_has': {
                            '.field.boolean': {}},
                        'privacy_policy_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'user_documentation_has': {
                            '.field.boolean': {}},
                        'user_documentation_url': {
                            '.field.string': {},
                            #'.flag.blankable': {},
                            '.flag.nullable': {}},
                        'operations_documentation_has': {
                            '.field.boolean': {}},
                        'operations_documentation_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'monitoring_has': {
                            '.field.boolean': {}},
                        'monitoring_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'accounting_has': {
                            '.field.boolean': {}},
                        'accounting_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'business_continuity_plan_has': {
                            '.field.boolean': {}},
                        'business_continuity_plan_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'disaster_recovery_plan_has': {
                            '.field.boolean': {}},
                        'disaster_recovery_plan_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'decommissioning_procedure_has': {
                            '.field.boolean': {}},
                        'decommissioning_procedure_url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'cost_to_run': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'cost_to_build': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'use_cases': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'is_in_catalogue': {
                            '.field.boolean': {}},
                        },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'user-customers': {
                    '.field.collection.django': {},
                    'model': 'service.models.UserCustomer',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.ref': {},
                            'to': 'api/v2/user-roles'},
                        'role': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'service_id': {
                            '.field.ref': {},
                            'to': 'api/v2/services'},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    }
                },

                'service_dependsOn_services': {
                    '.field.collection.django': {},
                    'model': 'service.models.Service_DependsOn_Service',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'id_service_one': {
                            '.field.ref': {},
                            'to': '/api/v2/service'},
                        'id_service_two': {
                            '.field.ref': {},
                            'to': '/api/v2/service'},
                    }
                },

                'service_externalServices': {
                    '.field.collection.django': {},
                    'model': 'service.models.Service_ExternalService',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'id_service': {
                            '.field.ref': {},
                            'to': '/api/v2/service'},
                        'id_external_service': {
                            '.field.ref': {},
                            'to': '/api/v2/external_service'},
                    }
                },

                'service-status': {
                    '.field.collection.django': {},
                    'model': 'service.models.ServiceStatus',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'value': {
                            '.field.string': {},
                            '.flag.orderable': {},
                            '.flag.filterable': {}},
                        'order': {
                            '.field.integer': {}},
                        },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                        },
                },

                'service-trls': {
                    '.field.collection.django': {},
                    'model': 'service.models.ServiceTrl',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
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
                    },
                },

                'external_services': {
                    '.field.collection.django': {},
                    'model': 'service.models.ExternalService',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
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
                    },
                },

                'user-roles': {
                    '.field.collection.django': {},
                    'model': 'service.models.UserRole',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.string': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'user_customers': {
                    '.field.collection.django': {},
                    'model': 'service.models.UserCustomer',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.ref': {},
                            'to': '/api/v2/user_role'},
                        'service_id': {
                            '.field.ref': {},
                            'to': '/api/v2/service'},
                        'role': {
                            '.field.string': {}},
                    },
                },

                'service-areas': {
                    '.field.collection.django': {},
                    'model': 'service.models.ServiceArea',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.string': {}},
                        'icon': {
                            '.field.file': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'service-owners': {
                    '.field.collection.django': {},
                    'model': 'owner.models.ServiceOwner',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'first_name': {
                            '.field.string': {}},
                        'last_name': {
                            '.field.string': {}},
                        'email': {
                            '.field.email': {}},
                        'phone': {
                            '.field.string': {}},
                        'id_service_owner': {
                            '.field.ref': {},
                            'to': '/api/v2/institutions'},
                        'id_account': {
                            '.field.ref': {},
                            'to': '/api/v2/custom-users'},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'custom-users': {
                    '.field.collection.django': {},
                    'model': 'accounts.models.User',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'username': {
                            '.field.string': {}},
                        'email': {
                            '.field.string': {}},
                        'first_name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'last_name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'is_staff': {
                            '.field.boolean': {}},
                        'is_active': {
                            '.field.boolean': {}},
                        'date_joined': {
                            '.field.datetime': {}},
                        'avatar': {
                            '.field.file': {}},
                        'shibboleth_id': {
                            '.field.string': {},
                            '.flag.readonly': {},
                            '.flag.nullable': {}},
                        'role': {
                            '.field.string': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },
                'contact-information': {
                    '.field.collection.django': {},
                    'model': 'owner.models.ContactInformation',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'first_name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'last_name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'email': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'phone': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'url': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'institutions': {
                    '.field.collection.django': {},
                    'model': 'owner.models.Institution',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'address': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'country': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'department': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'service-owners': {
                    '.field.collection.django': {},
                    'model': 'owner.models.ServiceOwner',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'first_name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'last_name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'email': {
                            '.field.email': {},
                            '.flag.nullable': {}},
                        'phone': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'id_service_owner': {
                            '.field.ref': {},
                            'to': '/api/v2/institutions'},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    }
                },

                'components': {
                    '.field.collection.django': {},
                    'model': 'component.models.ServiceComponent',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'description': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'logo': {
                            '.field.file': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'component-implementations': {
                    '.field.collection.django': {},
                    'model': 'component.models.ServiceComponentImplementation',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'component_id': {
                            '.field.ref': {},
                            'to': '/api/v2/components',
                            '.flag.filterable': {}},
                        'name': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                        'description': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'component-implementation-details': {
                    '.field.collection.django': {},
                    'model': 'component.models.ServiceComponentImplementationDetail',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'component_id': {
                            '.flag.filterable': {},
                            '.field.ref': {},
                            'to': '/api/v2/components'},
                        'component_implementation_id': {
                            '.flag.filterable': {},
                            '.field.ref': {},
                            'to': '/api/v2/component-implementations'},
                        'version': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },

                'component-implementation-detail-links': {
                    '.field.collection.django': {},
                    'model': 'component.models.ServiceDetailsComponent',
                    'fields': {
                        'id': {
                            '.field.uuid': {},
                            '.flag.readonly': {}},
                        'service_id': {
                            '.flag.filterable': {},
                            '.field.ref': {},
                            'to': '/api/v2/services'},
                        'service_details_id': {
                            '.flag.filterable': {},
                            '.field.ref': {},
                            'to': '/api/v2/service-versions'},
                        'service_component_implementation_detail_id': {
                            '.flag.filterable': {},
                            '.field.ref': {},
                            'to': '/api/v2/component-implementation-details'},
                        'configuration_parameters': {
                            '.field.string': {},
                            '.flag.nullable': {}},
                    },
                    'actions': {
                        '.action-template.django.list': {},
                        '.action-template.django.retrieve': {},
                        '.action-template.django.create': {},
                        '.action-template.django.delete': {},
                        '.action-template.django.update': {},
                    },
                },
            },
        },
    },
}
