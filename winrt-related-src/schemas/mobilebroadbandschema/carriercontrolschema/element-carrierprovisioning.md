---
Description: Defines the properties and settings in a subscriber's carrier provisioning file. 
Search.Product: eADQiWindows 10XVcnh
title: CarrierProvisioning
ms.assetid: 5033346d-9e0a-4d9e-a619-de88e2fb0818

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierProvisioning


Defines the properties and settings in a subscriber's carrier provisioning file. [**CarrierProvisioning**](element-carrierprovisioning.md) is the unique root element of the provisioning file.

## Element hierarchy

**&lt;CarrierProvisioning&gt;**

## Syntax

``` syntax
<CarrierProvisioning>

  <!-- Child elements -->
  Global,
  Activation?,
  MBNProfiles?,
  WLANProfiles?,
  Plans?,
  Provisioning?,
  Extensions?,
  Signature?

</CarrierProvisioning>
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
<td><a href="element-activation.md">Activation</a> </td>
<td><p>Defines information for a subscriber's activation method on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td><a href="element-extensions.md">Extensions</a> </td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="odd">
<td><a href="element-global.md">Global</a> </td>
<td><p>Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td><a href="element-mbnprofiles.md">MBNProfiles</a> </td>
<td><p>Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="odd">
<td><a href="element-plans.md">Plans</a> </td>
<td><p>Defines information for a subscriber's connection plans to a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
</tr>
<tr class="odd">
<td><a href="element-signature.md">Signature</a> </td>
<td><p>Defines an instance of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signature"><strong>Signature</strong></a>  element from the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/schema-root"><strong>CarrierControlSignatureSchema</strong></a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-wlanprofiles.md">WLANProfiles</a> </td>
<td><p>Defines information for a subscriber's WLAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 