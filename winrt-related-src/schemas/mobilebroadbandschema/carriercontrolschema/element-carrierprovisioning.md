---
Description: CarrierProvisioning
MS-HAID: CarrierControlSchema.element\_CarrierProvisioning
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: CarrierProvisioning
ms.assetid: 5033346d-9e0a-4d9e-a619-de88e2fb0818
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
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
<td>[Activation](element-activation.md)</td>
<td><p>Defines information for a subscriber's activation method on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td>[Extensions](element-extensions.md)</td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="odd">
<td>[Global](element-global.md)</td>
<td><p>Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td>[MBNProfiles](element-mbnprofiles.md)</td>
<td><p>Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="odd">
<td>[Plans](element-plans.md)</td>
<td><p>Defines information for a subscriber's connection plans to a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td>[Provisioning](element-provisioning.md)</td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
</tr>
<tr class="odd">
<td>[Signature](element-signature.md)</td>
<td><p>Defines an instance of the [<strong>Signature</strong>](https://msdn.microsoft.com/library/windows/apps/hh868330) element from the [<strong>CarrierControlSignatureSchema</strong>](https://msdn.microsoft.com/library/windows/apps/hh868341).</p></td>
</tr>
<tr class="even">
<td>[WLANProfiles](element-wlanprofiles.md)</td>
<td><p>Defines information for a subscriber's WLAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v1</p></td>
</tr>
</tbody>
</table>

 

 



