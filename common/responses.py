from strings import *






ERROR_MESSAGES = {
    OWNER_NOT_FOUND: "The requested service owner was not found",
    SERVICE_NOT_FOUND: "The requested service was not found",
    INVALID_UUID: "An invalid UUID was supplied",
    SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID: "A service component matching the specified service version does not exists",
    SERVICE_COMPONENT_INVALID_UUID: "An invalid service component UUID was supplied",
    SERVICE_DETAILS_NOT_FOUND: "The requested service details were not found",
    SERVICE_COMPONENT_NO_IMPLEMENTATIONS: "There are no implementations for the specified service component",
    SERVICE_COMPONENT_NOT_FOUND: "The requested service component was not found",
    SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID: "An invalid service component implementation UUID was supplied",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND: "The requested service component implementation details do not exist",
    SLA_INVALID_UUID: "An invalid service sla UUID was supplied",
    SLA_NOT_FOUND: "The requested SLA object was not found",
    SLA_SERVICE_DETAILS_MISMATCH: "This SLA object does not belong to the specified service and service details",
    SLA_PARAMETER_INVALID_UUID: "An invalid service sla parameter UUID was supplied",
    SLA_PARAMETER_NOT_FOUND: "The requested SLA parameter does not belong to the specified service",
    SERVICE_DETAILS_OPTIONS_NOT_FOUND: "This service has no service options for the current version",
    PAGE_NOT_FOUND: "The requested page was not found",
    INVALID_QUERY_PARAMETER: "The query parameter is invalid",
    SERVICE_COMPONENT_NAME_NOT_PROVIDED: "Service component name not provided",
    SERVICE_COMPONENT_NAME_EMPTY: "The provided service component name is empty",
    SERVICE_COMPONENT_DESCRIPTION_NOT_PROVIDED: "Service component description not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED: "Service component implementation name not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY: "The provided service component implementation name is empty",
    SERVICE_COMPONENT_IMPLEMENTATION_DESCRIPTION_NOT_PROVIDED: "Service component implementation description not provided",
    SERVICE_COMPONENT_UUID_EXISTS: "A service component object with the provided UUID already exists",
    SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS: "A service component implementation object with the provided UUID already exists",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED: "Service component implementation details version not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_CONFIGURATION_PARAMETERS_NOT_PROVIDED: "Service component implementation details configuration parameters not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY: "The provided service component implementation detail version is empty",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID: "An invalid service component implementation details UUID was supplied",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS: "A service component implementation details object with the provided UUID already exists",
    SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND: "The requested service component implementation was not found"
}


INFO_MESSAGES = {
    SERVICE_OWNER_INSTITUTION: "service owner institution information",
    SERVICE_OWNER_INFORMATION: "service owner information",
    SERVICE_COMPONENTS_INFORMATION: "service components information",
    SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION: "service component implementation information",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS: "service component implementation detail",
    SLA_INFORMATION: "service SLA information",
    SLA_PARAMETER_INFORMATION: "service SLA parameter information",
    SERVICE_OPTIONS: "options for service detail information",
    SERVICE_LIST: "list of services",
    SERVICE_INFORMATION: "service information",
    SERVICE_DETAIL_INFORMATION: "service details information",
    SERVICE_DEPENDENCIES_INFORMATION: "service dependencies information",
    SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION: "service external dependencies information",
    SERVICE_COMPONENT_INSERTED: "service component inserted",
    SERVICE_COMPONENT_IMPLEMENTATION_INSERTED: "service component implementation inserted",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED: "service component implementation details inserted"
}

STATUS_CODES = {
    OK_200: "200 OK",
    NOT_FOUND_404: "404 Not Found",
    NO_CONTENT_204: "204 No Content",
    CREATED_201: "201 Created",
    FORBIDDEN_403: "403 Forbidden",
    REJECTED_405: "405 Rejected",
    CONFLICT_409: "409 Conflict"
}