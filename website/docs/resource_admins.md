---
id: resource_admins
title: Resource Admins Information
---

**Resource admins**:  Resource Admins are users that own and manage one or more resources. A Resource Admin belongs to an Organization and can manage his own resources.  


## The Process

When a user is registered to the service, he is registered as an observer.
In order to be a `Resource Admin` the `Superadmin` or `Provider Admin` should change his role.
The `Superadmin` or `Provider Admin` will make him a `Resource Admin` and assign him to an organization .
By the time the user belongs to an Organization then  via the "Resource Admins" a Resource  can be assigned to him.


## List Resource Admins

To view the list of all Resource Admins, a `Superadmin`, `Provider Admin` or `Resource Admin` user must click to the **Resource Admins** left sidebar menu option.

| ![ResourceAdmins_ListView](assets/resource_admins_list.png) |
|:--------------------:|
| *The Resource Admins page* |


## Resource Admins Details

The user can view all the information from a selected Resource Admin by clicking on the details view ![view_icon](assets/icons_details.png) icon.

| ![Resources_ViewDetails](assets/resource_admins_details.png) |
|:--------------------:|
| *The details from a resource admin* |


## Create a new Resource Admin

To create a new Resource Admin, a `Superadmin` or `Provider Admin` user must click to the **Resource Admins** left sidebar menu option.
When the user clicks to the Resource Admins option, a new page with the list of existing Resource Admins is presented.

From this page a user may create a new resource admin just by clicking the **Create** option on the top right.

| ![Resources_create](assets/resource_admins_create.png) |
|:--------------------------:|
| *Create new Resource Admin * |


| Field Name                | Description           |
| ------------------------- | ----------------------|
| Admin (**required**)			|	The user to whom you want to assign the resource.						|
| Resource (**required**)		|	The reesource	|


A `Resource Admin` can only see the Resource Admins of the provider to which he belongs.

| ![ResourceAdmins_resourceadmin_View](assets/resource_admins_view.png) |
|:---------------------------------------------------------------------------------------------------:|
| *The resource admins page from a resource admin user where his organization has no resource admins* |

To create a new resource the `Superadmin` or `admin` click on "Create" top right.
The new resource admin (and edit resource admin) page provides a way for the `Superadmin` or `Provider Admin` to enter the resource admin details.

* **Admin :** The list of user options that are `Resource Admin` is displayed.
* **Resource :** The list of available resources is displayed.

> **Important note** : The resource and admin must belong to the **same organization**.

| ![ResourceAdmin_create](assets/resource_admins_create.png) |
|:--------------------------------:|
| *Create new Resource Admin page* |


## Edit Resource Admin

By selecting an existing Resource Admin a user can edit his details.


## Delete a Resource Admin.

Only the `Superadmin`, have the permission to delete a Resource Admin.

To delete an existing Resource Admin, the `Superadmin` user should visit the list of Resource Admins. By clicking on the delete ![delete_icon](assets/icons_delete.png) icon near the selected resource admin the user can delete it.

| ![delete_entry](assets/icons_confirm_delete.png) |
|:--------------------------:|
| *The page will show you a confirmation message and if you agree, then this entry will be deleted.* |
