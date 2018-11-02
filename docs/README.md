# AGORA Service Portfolio Management Tool (AGORA/SPMT)

The AGORA Service Portfolio Management Tool (AGORA/SPMT) is a tool aimed at facilitating service management in IT service provision, including federated scenarios.
AGORA represents a complete list  of the services managed by a service provider; some of these services are visible to the customers, while others are internal.
The service management system has been designed to be compatible with the FitSM service portfolio management. [fitsm.eu](fitsm.eu)

## Current installations

AGORA is used the in the context of three projects.

- [EOSC-Hub](https://eosc-hub.eu/) service catalogue 
- [EUDAT](https://eudat.eu/) service catalogue
- [VI-SEEM](https://vi-seem.eu/) service catalogue

## Overview/Components

Agora software stack is comprised of the following components:

- [agora-sp](#agora-sp): is the backend/api portfolio management system. Manages the complete list of services. Provides API interface to the database that stores the service portfolio information and makes it available for other management tools.

- [agora-sp-admin](#agora-sp-admin): is the administration interface for the `agora-sp` component. It enables the data entry procedure.  

- [agora-drupal-connector](#agora-drupal-connector): is drupal module that allows to render a service catalogue listing of the services provided bye the `agora-sp` api in the context of a drupal based site.

### Agora-sp
`Agora-sp` manages a complete list  of the services managed by a service provider

#### Features

- Represents a complete list  of the services managed by a service provider; some of these services are visible to the customers, while others are internal.

- Provides interfaces (API) to the database that stores the service portfolio information and makes it available for other management tools. 

- Stores service descriptions in detail, including relevant implementation and configuration details about service components.

- Informs other interested systems within the infrastructure about actual supported software versions and the service component configuration parameters as defined by the service developers.

- The service management system has been designed to be compatible with the FitSM service portfolio management. fitsm.eu

### Source Code

[https://github.com/grnet/agora-sp](https://github.com/grnet/agora-sp)

### Deployments:

- [eosc.agora.grnet.gr](eosc.agora.grnet.gr)
- [sp.eudat.eu](sp.eudat.eu)
- [services.vi-seem.eu](services.vi-seem.eu)


### Agora-sp-admin

Provides an intuitive user interface for the the agora-sp project. It allows users to create/edit/update/delete their services and components. Users can login with credentials provided by the administrator, or use the shibboleth login functionality to login with their academic account.

#### Features

- **Authentication** to AGORA supports federated AAI handled via SAML.
	- support for EGI AAI Check-in Service 
	- support for EUDAT B2ACCESS
	- support for VI-SEEM login

- **Authorization** role-based with the following categories:
	- *Admin*: who can read/modify/delete everything
	- *Service owner*: who can read everything; can modify/delete services that he is owner/manager of
	- *Observer*: who can read everything

### Source Code

[https://github.com/grnet/agora-sp-admin](https://github.com/grnet/agora-sp-admin)

### Deployments:

- [eosc.agora.grnet.gr](eosc.agora.grnet.gr)
- [sp.eudat.eu](sp.eudat.eu)


### Agora-drupal-connector

Is a drupal module that allows the administrator to create multiple agora feeds, choose which fields to render and create pages to render the data feeds. 
The administrator provides a valid Agora API Feed, selects which fields wants to be visible and specifies a new url in order for ReactJS app to render the defined selections.

This module is working with a dependency of [agora-catalogue-react-view](https://github.com/grnet/agora-catalogue-react-view)

### Source Code

[https://github.com/grnet/agora-drupal-connector.git](https://github.com/grnet/agora-drupal-connector.git)

### Deployments:

- [eudat.eu/catalogue](https://eudat.eu/catalogue)
- [eosc-hub.eu/catalogue](https://eosc-hub.eu/catalogue)

## More Information

[User Documentation](https://docs.google.com/document/d/1nLoHAx8w5o1RanERNOf5DlgrSvu4ZJ4fd-mQfBNNf18/edit?usp=sharing )

[Presentations](https://docs.google.com/presentation/d/e/2PACX-1vRSJGpvJyNb5FInJuGNSae-p1Y2AjaXA5FxhYHKTRTtWamH19Fgp91uxxaIrCgoCOjNrJOAUDolSuk0/pub?start=false&loop=false&delayms=3000&slide=id.p3) 
