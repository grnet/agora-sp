describe('/login', function() {

  beforeEach(() => {
    cy.visit('/')
    cy.contains('Login').click()
    cy.get('input').clear()
  })

  it('links to /auth/login', ()  => {
    cy.location('pathname').should('eq', '/ui/auth/login')
  })

  it('password is required client-side', () => {
    cy.get('input[name="password"]').type('superadmin')
    cy.get('form')
      .contains('form', 'login')
      .submit()
    cy.get('md-input-container')
      .should('have.class', 'md-input-invalid')
  })

  it('username is required client-side', () => {
    cy.get('input[name="identification"]').type('superadmin')
    cy.get('form')
      .contains('form', 'login')
      .submit()
    cy.get('md-input-container')
      .should('have.class', 'md-input-invalid')
  })

  it('requires valid username/password', () => {
    cy.get('input[name="identification"]').type('alice')
    cy.get('input[name="password"]').type('malicious')
    cy.get('form')
      .contains('form', 'login')
      .submit()
    cy.contains('Unable To Login With Provided Credentials')

  })

  it('superadmin successfully logs in', function() {
    cy.login('superadmin', '12345')
    cy.location('pathname').should('contains', 'services')
  })

})
