// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
 Cypress.Commands.add("login", (username, password) => {
    cy.visit('/')
    cy.contains('Login').click()
    cy.get('input[name="identification"]').type(username)
    cy.get('input[name="password"]').type(password)
    cy.get('form')
      .contains('form', 'login')
      .submit()
 })

 Cypress.Commands.add("check_menu", (location_contains) => {

    // expand all expandable sidebar menu items
    cy.get('.menu-link[href=""]').click({ multiple: true })

    // visit all menu items that are note expandable
    cy.get('.menu-link[href!=""]')
      .should('have.length', location_contains.length)
      .each(($el, i, $list) => {
        cy.wrap($el).should('have.attr', 'href').and('include', location_contains[i])
      })

 })
//
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This is will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })
