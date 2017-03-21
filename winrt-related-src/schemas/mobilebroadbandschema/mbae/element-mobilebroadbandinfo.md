---
Description: Defines mobile broadband information required for provisioning on the mobile network.
Search.Product: eADQiWindows 10XVcnh
title: MobileBroadbandInfo
ms.assetid: 4ebe0295-8b90-46ba-bc07-bfbae287c9b9
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# MobileBroadbandInfo


Defines mobile broadband information required for provisioning on the mobile network.

## Element hierarchy

**&lt;MobileBroadbandInfo&gt;**

## Syntax

``` syntax
<MobileBroadbandInfo>

  <!-- Child elements -->
  NetworkConfiguration?,
  ProvisioningEngine?,
  any element in a non-schema namespace*

</MobileBroadbandInfo>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td>[NetworkConfiguration](element-networkconfiguration.md)</td>
<td><div class="alert">
<strong>Note</strong>  The <strong>NetworkConfiguration</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase and Internet APN information.
</div>
<div>
 
</div>
<p>Defines the network configuration for the mobile broadband Purchase and Internet profiles to be used for mobile network.</p></td>
</tr>
<tr class="even">
<td>[ProvisioningEngine](element-provisioningengine.md)</td>
<td><p>Defines the trusted certificate values for Subject Name and Issuer Name required for provisioning on the mobile network.</p></td>
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
<td><p>http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo</p></td>
</tr>
</tbody>
</table>

 

 



