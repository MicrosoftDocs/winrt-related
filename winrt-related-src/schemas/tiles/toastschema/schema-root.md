---
description: Toast schema are used to define a toast notification, and specify the template, images, audio, and text that compose the toast content, branding specifics, and language information.
Search.Product: eADQiWindows 10XVcnh
title: Toast schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# Toast schema

These elements and their attributes are manipulated through Document Object Model (DOM) manipulation functions to customize the toast content.

To define the content for a toast, you can use [**ToastNotificationManager.getTemplateContent**](/uwp/api/Windows.UI.Notifications.ToastNotificationManager) to get a toast template that can be modified.

To examine the content of an existing toast, use [**ToastNotification.content**](/uwp/api/Windows.UI.Notifications.ToastNotification) to get the current contents.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-audio.md">audio</a> </td>
<td><p>Specifies a sound to play when a toast notification is displayed. This element also allows you to mute any toast notification audio.</p></td>
</tr>
<tr class="even">
<td><a href="element-binding.md">binding</a> </td>
<td><p>Specifies the toast template. Note that only one binding element can be included in a toast notification.</p></td>
</tr>
<tr class="odd">
<td><a href="element-command.md">command</a> </td>
<td><p>Specifies a scenario-associated button shown in a toast. The scenario is specified in the parent <a href="element-commands.md"><strong>commands</strong></a>  element.</p></td>
</tr>
<tr class="even">
<td><a href="element-commands.md">commands</a> </td>
<td><p>Specifies that the toast notification is being used to indicate an incoming call or an alarm, with appropriate commands associated with each scenario.</p></td>
</tr>
<tr class="odd">
<td><a href="element-image.md">image</a> </td>
<td><p>Specifies an image used in the toast template.</p></td>
</tr>
<tr class="even">
<td><a href="element-text.md">text</a> </td>
<td><p>Specifies text used in the toast template.</p></td>
</tr>
<tr class="odd">
<td><a href="element-toast.md">toast</a> </td>
<td><p>Base toast element, which contains at least a single <a href="element-visual.md"><strong>visual</strong></a>  element.</p></td>
</tr>
<tr class="even">
<td><a href="element-visual.md">visual</a> </td>
<td><p>Contains a single <a href="/uwp/schemas/tiles/tilesschema/element-binding"><strong>binding</strong></a>  element that defines a toast.</p></td>
</tr>
<tr class="odd">
<td><a href="element-header.md">header</a> </td>
<td><p>Specifies a custom header that groups multiple notifications together within Action Center.</p></td>
</tr>
<tr class="even">
<td><a href="element-actions.md">actions</a> </td>
<td><p>Container element for declaring up to five inputs and up to five button actions for the toast notification.</p></td>
</tr>
<tr class="odd">
<td><a href="element-action.md">action</a> </td>
<td><p>Specifies a button shown in a toast.</p></td>
</tr>
<tr class="even">
<td><a href="element-actions.md">actions</a> </td>
<td><p>Container element for declaring up to five inputs and up to five button actions for the toast notification.</p></td>
</tr>
<tr class="odd">
<td><a href="element-progress.md">progress</a> </td>
<td><p>Specifies a progress bar for a toast notification.</p></td>
</tr>
<tr class="even">
<td><a href="element-group.md">group</a> </td>
<td><p>Semantically identifies that the content in the group must either be displayed as a whole, or not displayed if it cannot fit. Groups also allow creating multiple columns.</p></td>
</tr>
<tr class="odd">
<td><a href="element-subgroup.md">subgroup</a> </td>
<td><p>Specifies vertical columns that can contain text and images.</p></td>
</tr>
</tbody>
</table>

 

 

 
