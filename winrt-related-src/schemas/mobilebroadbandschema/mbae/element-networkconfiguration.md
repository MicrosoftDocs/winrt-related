---
Description: NetworkConfiguration
MS-HAID: MBAE.element\_NetworkConfiguration
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: NetworkConfiguration
ms.assetid: 528097af-092d-4aaf-abcc-cef110f1018e
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# NetworkConfiguration


**Note**  The **NetworkConfiguration** element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase and Internet APN information.

 

Defines the network configuration for the mobile broadband Purchase and Internet profiles to be used for mobile network.

## Element hierarchy

<dl>
<dt><a href="element-mobilebroadbandinfo.md">&lt;MobileBroadbandInfo&gt;</a></dt>
<dd><b>&lt;NetworkConfiguration&gt;</b></dd>
</dl>

## Syntax

``` syntax
<NetworkConfiguration>

  <!-- Child elements -->
  MobileBroadbandProfiles?,
  any element in a non-schema namespace*

</NetworkConfiguration>
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
<td>[MobileBroadbandProfiles](element-mobilebroadbandprofiles.md)</td>
<td><div class="alert">
<strong>Note</strong>  The <strong>MobileBroadbandProfiles</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Internet and Purchase APN information.
</div>
<div>
 
</div>
<p>Defines the mobile broadband Purchase and Internet profiles to be used for the mobile network.</p></td>
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
<td>[MobileBroadbandInfo](element-mobilebroadbandinfo.md)</td>
<td><p>Defines mobile broadband information required for provisioning on the mobile network.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**MobileBroadbandInfo**](element-mobilebroadbandinfo.md)

[MBAE schema](schema-root.md)

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

 

 



