---
Description: Defines a purchase connection profile used by a subscriber to connect to a MNO.
Search.Product: eADQiWindows 10XVcnh
title: PurchaseProfile
ms.assetid: 66b0d844-5469-4e94-b364-72638ac4212a
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
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
<td>[AssociatedPlan](element-1-associatedplan.md)</td>
<td><p>Contains the name of the subscriber's data plan. It must match the <strong>Name</strong> attribute of a [<strong>Plan</strong>](https://msdn.microsoft.com/library/windows/apps/hh868373) in the same XML document.</p></td>
</tr>
<tr class="even">
<td>[Context](element-1-context.md)</td>
<td><p>Defines the parameters required to setup a data connection.</p></td>
</tr>
<tr class="odd">
<td>[DataRoamingPartners](element-1-dataroamingpartners.md)</td>
<td><p>Defines the list of preferred network providers for roaming.</p></td>
</tr>
<tr class="even">
<td>[Description](element-1-description.md)</td>
<td><p>Defines a brief description of the profile.</p></td>
</tr>
<tr class="odd">
<td>[Extensions](element-1-extensions.md)</td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="even">
<td>[HomeProviderName](element-1-homeprovidername.md)</td>
<td><p>Defines the name of the Home Provider for a given SIM/Device.</p></td>
</tr>
<tr class="odd">
<td>[Name (type: NameType)](element-2-name.md)</td>
<td><p>Defines the profile name. Must be 64 characters or less.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



