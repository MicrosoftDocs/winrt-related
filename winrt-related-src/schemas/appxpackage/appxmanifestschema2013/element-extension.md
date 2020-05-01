---
Description: Declares an extensibility point for the app.
Search.Product: eADQiWindows 10XVcnh
title: Extension
ms.assetid: 72f0d1ae-15a4-4eba-a3ca-990f4de2b697


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Extension

Declares an extensibility point for the app.

## Element hierarchy

**&lt;Extension&gt;**

## Syntax

``` syntax
<Extension Category = "windows.lockScreenCall" | "windows.contact" | "windows.appointmentsProvider" | "windows.alarm" >

  <!-- Child elements -->
  ( Contact
  | AppointmentsProvider
  )?

</Extension>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Category</strong></td>
<td><p>The type of app extensibility point.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>windows.lockScreenCall</li>
<li>windows.contact</li>
<li>windows.appointmentsProvider</li>
<li>windows.alarm</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-appointmentsprovider.md">AppointmentsProvider</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.appointmentsProvider</strong>.</p></td>
</tr>
<tr class="even">
<td><a href="element-contact.md">Contact</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.contact</strong>.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

For more info, see [**Extension**](https://msdn.microsoft.com/library/windows/apps/dn423270).

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2013/manifest` |

 

 



