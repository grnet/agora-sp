.meta:
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
      description_external:
        .string: {}
      description_internal:
        .string: {}
      service_area:
        .string: {}
        .filterable: {}
      service_type:
        .string: {}
        .filterable: {}
      service_trl:
        .ref: {'to': '/api/v2/service-trls'}
      request_procedures:
        .string: {}
      funders_for_service:
        .string: {}
      value_to_customer:
        .string: {}
      risks:
        .string: {}
      competitors:
        .string: {}
      id_contact_information:
        .ref: {'to': '/api/v2/contact_information'}
      id_contact_information_internal:
        .ref: {'to': '/api/v2/contact_information'}
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
  service_versions:
    .collection:
      model: service.models.ServiceDetails
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .ref: {'to': '/api/v2/service'}
      status:
        .ref: {'to': '/api/v2/service_status'}
      version:
        .string: {}
      features_current:
        .string: {}
      usage_policy_has:
        .boolean: {}
      usage_policy_url:
        .string: {}
      privacy_policy_has:
        .boolean: {}
      privacy_policy_url:
        .string: {}
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
      monitoring_has:
        .boolean: {}
      monitoring_url:
        .string: {}
      accounting_has:
        .boolean: {}
      accounting_url:
        .string: {}
      business_continuity_plan_has:
        .boolean: {}
      business_continuity_plan_url:
        .string: {}
      disaster_recovery_plan_has:
        .boolean: {}
      disaster_recovery_plan_url:
        .string: {}
      decommissioning_procedure_has:
        .boolean: {}
      decommissioning_procedure_url:
        .string: {}
      cost_to_run:
        .string: {}
      cost_to_build:
        .string: {}
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
  service_dependsOn_service:
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
  service_externalService:
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
  service_status:
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
  external_service:
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
  external_service:
    .collection:
      model: service.models.ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
  user_role:
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
  user_customer:
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
  service_area:
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
  service_owner:
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
        .ref: {'to': '/api/v2/institution'}
      id_account:
      .ref: {'to': '/api/v2/custom_user'}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  institution:
    .collection:
      model: owner.models.Institution
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      address:
        .string: {}
      country:
        .string: {}
      department:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
  custom_user:
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
  contact_information:
    .collection:
      model: owner.models.ContactInformation
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
      url:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
    .actions=:
      .list: {}
      .create: {}
      .delete: {}
      .update: {}
