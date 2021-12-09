---
id: authenticate
title: Authentication / Authorization
---

## SPMT/AGORA

The Service Portfolio Management Tool (AGORA) is a tool aimed at facilitating service management in IT service provision, including federated scenarios.
SPMT represents a complete list of the services managed by a service provider; some of these services are visible to the customers, while others are internal.
The service management system has been designed to be compatible with the FitSM service portfolio management. [fitsm.eu](https://fitsm.eu)

## Authentication 

Users can login with credentials provided by the administrator, or use the shibboleth login functionality to login with their academic account.
Authentication in SPMT supports federated AAI handled via SAML from the following providers:
 - EGI AAI Check-in Service
 - EUDAT B2ACCESS
 - NI4OS Login service
 - VI-SEEM login


## Authorization 

The authorization in SPMT/AGORA follows the role-based access control. Role-based access control (RBAC) refers to the idea of assigning permissions to users based on their role within an organization. It provides fine-grained control and offers a simple, manageable approach to access management that is less prone to error than assigning permissions to users individually.


### User Roles

It supports the following roles:

 - **Super Admin**: The one that administers the whole system.
 - **Portfolio Admin**: The one responsible for the portfolio and validating Resources and Providers.
 - **Provider Admin**: Who administates the users and services belonging to his Provider.
 - **Resource Admin**: Who can read everything; can modify/delete services that he is owner/manager of.
 - **Observer**: Who can read everything.

A new user who has just registered in SPMT/AGORA, acquires only the right of access to the service as an observer. That is why it automatically enters the category of observer users. To grant more permissions, these it must be assigned by a `Superadmin` user. See below the categories of users that exist as well as their respective rights.

