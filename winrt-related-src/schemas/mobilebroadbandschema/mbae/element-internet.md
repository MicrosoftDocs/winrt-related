---
Description: Defines the mobile broadband Internet profile to be used for the mobile network.
Search.Product: eADQiWindows 10XVcnh
title: Internet
ms.assetid: ddcce350-4ec2-485d-9b78-e159e4161dbf
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Internet

**Note**  The **Internet** element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Internet APN information.

Defines the mobile broadband Internet profile to be used for the mobile network.

## Element hierarchy

<dl>
<dt><a href="element-mobilebroadbandinfo.md">&lt;MobileBroadbandInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-networkconfiguration.md">&lt;NetworkConfiguration&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-mobilebroadbandprofiles.md">&lt;MobileBroadbandProfiles&gt;</a></dt>
<dd><b>&lt;Internet&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Internet>

  FileType

</Internet>
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

 

 



