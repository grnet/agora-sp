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
    PAGE_NOT_FOUND: "The requested page was not found"
}


INFO_MESSAGES = {
    SERVICE_OWNER_INSTITUTION: "service owner institution information",
    SERVICE_OWNER_INFORMATION: "service owner information",
    SERVICE_COMPONENTS_INFORMATION: "service components information",
    SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION: "service component implementation information",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS: "service component implementation detail",
    SLA_INFORMATION: "service SLA information",
    SLA_PARAMETER_INFORMATION: "service SLA parameter information",
    SERVICE_OPTIONS: "options for service detail information"
}