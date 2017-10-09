.meta:
  root_url: http://localhost:8080
  get_rules: agora.utils.get_rules
api/v2:
  .endpoint: {}
  users:
    .collection:
      model: accounts.models.User
    '*':
      id:
        .uuid: {}
        .readonly: {}
      username:
        .string: {}
      email:
        .string: {}
    .actions=:
      .list: {}
  services:
    .collection:
      model: service.models.Service
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
        .filterable: {}
        .sortable: {}
      short_description:
        .string: {}
        .nullable: {}
      description_external:
        .string: {}
        .nullable: {}
      description_internal:
        .string: {}
        .nullable: {}
      service_area:
        .string: {}
        .nullable: {}
        .filterable: {}
      service_type:
        .string: {}
        .nullable: {}
        .filterable: {}
      service_trl:
        .ref:
          to: /api/v2/service-trls
      request_procedures:
        .string: {}
        .nullable: {}
      funders_for_service:
        .string: {}
        .nullable: {}
      value_to_customer:
        .string: {}
        .nullable: {}
      risks:
        .string: {}
        .nullable: {}
      competitors:
        .string: {}
        .nullable: {}
      id_service_owner:
        .ref:
          to: /api/v2/service-owners
      id_contact_information:
        .ref:
          to: /api/v2/contact-information
      id_contact_information_internal:
        .ref:
          to: /api/v2/contact-information
      logo:
        .file: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  service-versions:
    .collection:
      model: service.models.ServiceDetails
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .ref:
          to: /api/v2/service
      status:
        .ref:
          to: /api/v2/service-status
      version:
        .string: {}
      features_current:
        .string: {}
        .nullable: {}
      usage_policy_has:
        .boolean: {}
      usage_policy_url:
        .string: {}
        .nullable: {}
      privacy_policy_has:
        .boolean: {}
      privacy_policy_url:
        .string: {}
        .nullable: {}
      user_documentation_has:
        .boolean: {}
      user_documentation_url:
        .blankable: {}
        .nullable: {}
        .string: {}
      operations_documentation_has:
        .boolean: {}
      operations_documentation_url:
        .string: {}
        .nullable: {}
      monitoring_has:
        .boolean: {}
      monitoring_url:
        .string: {}
        .nullable: {}
      accounting_has:
        .boolean: {}
      accounting_url:
        .string: {}
        .nullable: {}
      business_continuity_plan_has:
        .boolean: {}
      business_continuity_plan_url:
        .string: {}
        .nullable: {}
      disaster_recovery_plan_has:
        .boolean: {}
      disaster_recovery_plan_url:
        .string: {}
        .nullable: {}
      decommissioning_procedure_has:
        .boolean: {}
      decommissioning_procedure_url:
        .string: {}
        .nullable: {}
      cost_to_run:
        .string: {}
        .nullable: {}
      cost_to_build:
        .string: {}
        .nullable: {}
      use_cases:
        .string: {}
      is_in_catalogue:
        .boolean: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  service_dependsOn_services:
    .collection:
      model: service.models.Service_DependsOn_Service
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service_one:
        .ref: {'to': '/api/v2/service'}
      id_service_two:
        .ref: {'to': '/api/v2/service'}
  service_externalServices:
    .collection:
      model: service.models.Service_ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .ref: {'to': '/api/v2/service'}
      id_external_service:
        .ref: {'to': '/api/v2/external_service'}
  service-status:
    .collection:
      model: service.models.ServiceStatus
    '*':
      id:
        .uuid: {}
        .readonly: {}
      value:
        .string: {}
        .sortable: {}
        .filterable: {}
      order:
        .integer: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  service-trls:
    .collection:
      model: service.models.ServiceTrl
    '*':
      id:
        .uuid: {}
        .readonly: {}
      value:
        .string: {}
        .filterable: {}
        .sortable: {}
      order:
        .integer: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  external_services:
    .collection:
      model: service.models.ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      description:
        .string: {}
      service:
        .string: {}
      details:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  user_roles:
    .collection:
      model: service.models.UserRole
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  user_customers:
    .collection:
      model: service.models.UserCustomer
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .ref: {'to': '/api/v2/user_role'}
      service_id:
        .ref: {'to': '/api/v2/service'}
      role:
        .string: {}
  service_areas:
    .collection:
      model: service.models.ServiceArea
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      icon:
        .file: {}
      .actions=:
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  service-owners:
    .collection:
      model: owner.models.ServiceOwner
    '*':
      id:
        .uuid: {}
        .readonly: {}
      first_name:
        .string: {}
      last_name:
        .string: {}
      email:
        .email: {}
      phone:
        .string: {}
      id_service_owner:
        .ref:
          to: /api/v2/institutions
      id_account:
        .ref:
          to: /api/v2/custom-users
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  custom-users:
    .collection:
      model: accounts.models.User
    '*':
      username:
        .string: {}
      email:
        .email: {}
      first_name:
        .string: {}
      last_name:
        .string: {}
      is_staff:
        .boolean: {}
      is_active:
        .boolean: {}
      date_joined:
        .datetime: {format: ['%Y-%m-%dT%H:%M']}
      avatar:
        .file: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  contact-information:
    .collection:
      model: owner.models.ContactInformation
    '*':
      id:
        .uuid: {}
        .readonly: {}
      first_name:
        .string: {}
        .nullable: {}
      last_name:
        .string: {}
        .nullable: {}
      email:
        .email: {}
        .nullable: {}
      phone:
        .string: {}
        .nullable: {}
      url:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  institutions:
    .collection:
      model: owner.models.Institution
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
        .nullable: {}
      address:
        .string: {}
        .nullable: {}
      country:
        .string: {}
        .nullable: {}
      department:
        .string: {}
        .nullable: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  service-owners:
    .collection:
      model: owner.models.ServiceOwner
    '*':
      id:
        .uuid: {}
        .readonly: {}
      first_name:
        .string: {}
        .nullable: {}
      last_name:
        .string: {}
        .nullable: {}
      email:
        .email: {}
        .nullable: {}
      phone:
        .string: {}
        .nullable: {}
      id_service_owner:
        .ref: {'to': '/api/v2/institutions'}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
