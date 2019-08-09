describe('sidebar menu', function() {

  it('observer views sidebar menu', () => {
    let location_contains = [ 'services', 'service-versions', 'components', 'component-implementations', 'component-implementation-details', 'component-implementation-detail-links', 'access-policies', 'providers', 'federation-members', 'service-categories', 'service-trls', 'user-roles', 'service-status', 'user-customers' ]

    cy.login('observer', '12345')
    cy.check_menu(location_contains)
  })

  it('service_admin views sidebar menu', () => {
    let location_contains = ['services', 'service-versions', 'my-services', 'components', 'component-implementations', 'component-implementation-details', 'component-implementation-detail-links', 'access-policies', 'providers', 'service-admins', 'federation-members', 'service-categories', 'service-trls', 'user-roles', 'service-status', 'user-customers' ]

    cy.login('service_admin_1', '12345')
    cy.check_menu(location_contains)
  })

  it('admin views sidebar menu', () => {
    let location_contains = ['services', 'service-versions', 'components', 'component-implementations', 'component-implementation-details', 'component-implementation-detail-links', 'access-policies', 'providers', 'service-admins', 'federation-members', 'service-categories', 'service-trls', 'user-roles', 'service-status', 'user-customers', 'custom-users' ]

    cy.login('admin', '12345')
    cy.check_menu(location_contains)
  })

  it('superadmin views sidebar menu', () => {
    let location_contains = [ 'services', 'service-versions', 'components', 'component-implementations', 'component-implementation-details', 'component-implementation-detail-links', 'access-policies', 'providers', 'service-admins', 'federation-members', 'service-categories', 'service-trls', 'user-roles', 'service-status', 'user-customers', 'custom-users' ]

    cy.login('superadmin', '12345')
    cy.check_menu(location_contains)
  })
})
