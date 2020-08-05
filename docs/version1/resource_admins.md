---
id: resource_admins
title: Resource Admins Information
---

> If a user is registered as an observer, then `superadmin` or `admin` should change his role and make him a `ResourceAdmin` and assign it to an organization.

> And then go to Resource Admins and assign it to a Resource.


## Resource Admins List.

To view the list of all Resource Admins, a `superadmin`, `admin` or `Service Admin` user must click to the **Resource Admins** left sidebar menu option.

| ![ResourceAdmins_ListView](assets/resource_admins/list.png) |
|:--------------------:|
| *The Resource Admins page* |



## Resource Admins Details.

The user can view all the information from a selected esource admin by clicking on the details view ![view_icon](assets/icons/details.png) icon.

| ![Resources_ViewDetails](assets/resource_admins/details.png) |
|:--------------------:|
| *The details from a resource admin* |



## Create a new resource admin.

To create a new Resource Admin, a `superadmin` or `admin` user must click to the **Resource Admins** left sidebar menu option.
When the user clicks to the Resource Admins option, a new page with the list of existing Resource Admins is presented.

From this page a user may create a new resource admin just by clicking the **Create** option on the top right.

| ![Resources_create](assets/resource_admins/create.png) |
|:--------------------------:|
| *Create new resource admin page* |


| Field Name                | Description           |
| ------------------------- | ----------------------|
| Admin (**required**)			|	The user to whom you want to assign the resource.						|
| Resource (**required**)		|	The reesource	|



On the other hand, an `Resource Admin` can only see the Resource Admins of the provider to which it belongs. A `Observer` user, doesn't have access to this menu.

| ![ResourceAdmins_resourceadmin_View](assets/resource_admins/resource_admin_view.png) |
|:---------------------------------------------------------------------------------------------------:|
| *The resource admins page from a resource admin user where his organization has no resource admins* |


By selecting an existing resource admin one can edit the details of such a resource admin.
To create a new resource the `superadmin` or `admin` click on "Create" top right.

| ![ResourceAdmin_create](assets/resource_admins/create.png) |
|:--------------------------------:|
| *Create new Resource Admin page* |

The new resource admin (and edit resource admin) page provides a way for the `superadmin` or `admin` to enter the resource admin details.

* **Admin :** The list of user options that are `Resource Admin` is displayed.
* **Resource :** The list of available resources is displayed.

> **Important note** : The resource and admin must belong to the **same organization**.


## Delete a resource admin.

Only the `superadmin`, have the permission to delete a resource admin.

To delete an existing resource admin, the `superadmin` user should visit the list of Resource Admins. By clicking on the delete ![delete_icon](assets/icons/delete.png) icon near the selected resource admin the user can delete it.

| ![delete_entry](assets/icons/confirm_delete.png) |
|:--------------------------:|
| *The page will show you a confirmation message and if you agree, then this entry will be deleted.* |
