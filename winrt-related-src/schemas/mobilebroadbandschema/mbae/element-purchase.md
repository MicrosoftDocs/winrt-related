---
Description: Purchase
MS-HAID: MBAE.element\_Purchase
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Purchase
ms.assetid: 44162498-f0ee-415b-9b7d-19d7997f40b6
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# Purchase


**Note**  The **Purchase** element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase APN information.

 

Defines the mobile broadband Purchase profile to be used for the mobile network.

## Element hierarchy

<dl>
<dt><a href="element-mobilebroadbandinfo.md">&lt;MobileBroadbandInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-networkconfiguration.md">&lt;NetworkConfiguration&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-mobilebroadbandprofiles.md">&lt;MobileBroadbandProfiles&gt;</a></dt>
<dd><b>&lt;Purchase&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Purchase>

  FileType

</Purchase>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

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

 

## See also


[**MobileBroadbandInfo**](element-mobilebroadbandinfo.md)

[**MobileBroadbandProfiles**](element-mobilebroadbandprofiles.md)

[**NetworkConfiguration**](element-networkconfiguration.md)

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

 

 



