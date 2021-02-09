---
description: Declares an app extensibility point of type windows.contact.
Search.Product: eADQiWindows 10XVcnh
title: Contact
ms.assetid: 28ca2446-b797-4699-bd5a-56f1cfdf5782


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Contact




Declares an app extensibility point of type **windows.contact**.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;Contact&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Contact>

  <!-- Child elements -->
  ContactLaunchActions

</Contact>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-contactlaunchactions.md">ContactLaunchActions</a> </td>
<td><p>Declares actions to take when a contact is launched.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-extension.md">Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For more info about contacts, see [**Windows.ApplicationModel.Contacts**](/uwp/api/Windows.ApplicationModel.Contacts).

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 
