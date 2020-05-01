---
Description: Defines a purchase connection profile used by a subscriber to connect to a MNO.
Search.Product: eADQiWindows 10XVcnh
title: PurchaseProfile
ms.assetid: 66b0d844-5469-4e94-b364-72638ac4212a

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# PurchaseProfile


Defines a purchase connection profile used by a subscriber to connect to a MNO.

## Element hierarchy

**&lt;PurchaseProfile&gt;**

## Syntax

``` syntax
<PurchaseProfile Priority? = Priority : "5" >

  <!-- Child elements -->
  Name,
  Description?,
  AssociatedPlan?,
  HomeProviderName?,
  Context?,
  DataRoamingPartners?,
  Extensions?

</PurchaseProfile>
```

### Key

`?`   optional (zero or one)
`:`   default value
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
<td><strong>Priority</strong></td>
<td><p>Defines the priority of a wireless profile.</p></td>
<td>Priority</td>
<td>No</td>
<td>5</td>
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
<td><a href="element-1-associatedplan.md">AssociatedPlan</a> </td>
<td><p>Contains the name of the subscriber's data plan. It must match the <strong>Name</strong> attribute of a <a href="https://msdn.microsoft.com/library/windows/apps/hh868373"><strong>Plan</strong></a>  in the same XML document.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-context.md">Context</a> </td>
<td><p>Defines the parameters required to setup a data connection.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-dataroamingpartners.md">DataRoamingPartners</a> </td>
<td><p>Defines the list of preferred network providers for roaming.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-description.md">Description</a> </td>
<td><p>Defines a brief description of the profile.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-extensions.md">Extensions</a> </td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-homeprovidername.md">HomeProviderName</a> </td>
<td><p>Defines the name of the Home Provider for a given SIM/Device.</p></td>
</tr>
<tr class="odd">
<td><a href="element-2-name.md">Name (type: NameType)</a> </td>
<td><p>Defines the profile name. Must be 64 characters or less.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



