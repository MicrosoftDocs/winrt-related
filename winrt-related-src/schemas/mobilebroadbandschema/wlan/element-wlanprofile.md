---
Description: Defines the properties and security settings of a subscriber's WLAN connection profile.
Search.Product: eADQiWindows 10XVcnh
title: WLANProfile
ms.assetid: adafca95-23be-417f-8c3f-7c340222ecfd

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# WLANProfile


Defines the properties and security settings of a subscriber's WLAN connection profile. [**WLANProfile**](element-wlanprofile.md) is the unique root element of a wireless profile.

## Element hierarchy

**&lt;WLANProfile&gt;**

## Syntax

``` syntax
<WLANProfile Priority? = Priority : "5" >

  <!-- Child elements -->
  name,
  AssociatedPlan?,
  SSIDConfig,
  MSM?

</WLANProfile>
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
<td><a href="element-associatedplan.md">AssociatedPlan</a> </td>
<td><p>Contains the name of the subscriber's data plan. It must match the <strong>Name</strong> attribute of a <a href="/uwp/schemas/mobilebroadbandschema/plans/element-plan"><strong>Plan</strong></a>  in the same XML document.</p></td>
</tr>
<tr class="even">
<td><a href="element-msm.md">MSM</a> </td>
<td><p>Defines various media-specific module (MSM) settings for this profile on a WLAN.</p></td>
</tr>
<tr class="odd">
<td><a href="element-ssidconfig.md">SSIDConfig</a> </td>
<td><p>Defines one or more service set identifiers (SSID) for a wireless LAN.</p></td>
</tr>
<tr class="even">
<td><a href="element-name.md">name (type: NameType)</a> </td>
<td><p>Defines the case sensitive name of a wireless LAN profile.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 