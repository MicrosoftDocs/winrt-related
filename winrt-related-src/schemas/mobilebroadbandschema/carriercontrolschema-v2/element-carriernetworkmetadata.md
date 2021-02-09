---
description: Defines the network properties and settings in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: CarrierNetworkMetadata
ms.assetid: 6b8fa3df-5138-475d-ac95-305c273730fe

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierNetworkMetadata


Defines the network properties and settings in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd><b>&lt;CarrierNetworkMetadata&gt;</b></dd>
</dl>

## Syntax

``` syntax
<CarrierNetworkMetadata>

  <!-- Child elements -->
  NetworkSettings?,
  DataClassFriendlyNames?,
  CustomerSupportPhoneNumber?

</CarrierNetworkMetadata>
```

### Key

`?`   optional (zero or one)

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
<td><a href="element-customersupportphonenumber.md">CustomerSupportPhoneNumber</a> </td>
<td><p>Defines the phone number for customer support in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td><a href="element-dataclassfriendlynames.md">DataClassFriendlyNames</a> </td>
<td><p>Defines class friendly names for the standard or protocol used for mobile network data in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td><a href="element-networksettings.md">NetworkSettings</a> </td>
<td><p>Defines the network settings in a subscriber's carrier provisioning file.</p></td>
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
<td><a href="element-extensions-v2.md">Extensions_v2</a> </td>
<td><p>Defines additional properties and settings in a subscriber's carrier provisioning file. <a href="element-extensions-v2.md"><strong>Extensions_v2</strong></a>  is the unique root element of the <a href="schema-root.md">CarrierControlSchema_v2</a> provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## See also


[CarrierControlSchema schema](../carriercontrolschema/schema-root.md)

[CarrierControlSchema\_v2 schema](schema-root.md)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v2` |

 

 
