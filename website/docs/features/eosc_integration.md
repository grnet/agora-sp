---
id: eosc_integration
title: EOSC Integration
sidebar_position: 2
---

## EOSC Portal

The EOSC Portal ([eosc-portal.eu](https://eosc-portal.eu/)) will be Europe’s virtual environment for all researchers to store, manage, analyse and re-use data for research, innovation and educational purposes.

EOSC is intended to set off the ground by federating existing scientific data infrastructures and digital infrastructures for data exploitation that are now spread across disciplines and EU member states.

This will make access to scientific data and other scientific outputs easier and more efficient.


## Agora Integration with EOSC API

The EOSC provides a public api to allow regional and thematic catalogues to on-board providers and resources to the EOSC Portal: [providers.eosc-portal.eu](https://providers.eosc-portal.eu/developers).


## Vocabulary

In order to be able to send and receive data with eosc API we had to match our fixtures that we use in agora with the EOSC API Vocabulary.
As a result the field `eosc_id` was added in the fixtures for each entry.
```json
//For example an entry from resource categories you can see the eosc_id in the data model.
{
    "fields": {
        "name": "Data",
        "supercategory": "6c609f4c-22ea-44ae-967f-c8921cbf84b0",
        "eosc_id": "category-sharing_and_discovery-data"
    },
    "model": "service.category",
    "pk": "09148c1e-775a-4925-9e5c-3df2375cb9d8"
}
```


## Profiles 3.0

An important aspect of the integration with the EOSC API are the models of the resources and the Profiles. EOSC API had standardized the models of the resources and providers with profiles 3.0 with mandatory or not fields that someone has to provide to describe a resource/provider.
Find the profiles 3.0 description here: [Profiles 3.0](https://docs.google.com/spreadsheets/d/1o3vhia3Fl1ULbn0CI0nSusZkZ-PDnfvCW_l76c7X4yo/edit#gid=0)


## Publishing a Provider

The flow of the publishing to eosc API follows these steps:
1. The Superadmin creates a new provider
2. The Superadmin assigned the role of the provider admin to a user
3. The Provider admin can edit the provider and publish it to eosc
4. The Portfolio admin can also publish the provider and approve/reject it

| ![published_provider](assets/published_provider.png) |
|:-------------------------------------:|
| *A published provider has an eosc id* |


## Approve a Provider

The Portfolio admin will review the provider and approve it.
![pending_initial_approval](assets/provider_status_approve.png)


## Reject a Provider

The Portfolio admin has the option to reject a provider petition.
![pending_initial_approval](assets/provider_status_reject.png)



## Publishing a Resource

The flow of the resource publishing to eosc API follows these steps:
1. The Provider admin creates a new resource
2. The Provider admin can edit the resource and publish it to eosc.
3. The Portfolio admin can review the resource and approve/reject it.

| ![published_provider](assets/resource.png) |
|:-------------------------------------:|
| *A published resource has an eosc id* |


## Approve a Resource

The Portfolio admin will review the Resource and approve it.
![pending_initial_approval](assets/resource_status_approve.png)


## Reject a Resource

The Portfolio admin has the option to reject a Resource petition.
![pending_initial_approval](assets/resource_status_reject.png)