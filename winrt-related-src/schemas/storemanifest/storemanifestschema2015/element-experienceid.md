---
Description: ExperienceId
MS-HAID: StoreManifestSchema2015.element\_ExperienceId
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: ExperienceId
ms.assetid: fb3585cf-8f9c-4ae6-8430-685ccc132a98
author: laurenhughes
ms.author: lahugh
windows 10, uwp, schema, storemanifest
---

# ExperienceId


The ExperienceId element specifies a GUID that links the device metadata to a device app that can be automatically acquired when the device is first connected. Each ExperienceId GUID corresponds to the ExperienceId element of a device metadata package.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-devicecompanionapplication.md">&lt;DeviceCompanionApplication&gt;</a></dt>
<dd><b>&lt;ExperienceId&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ExperienceId>

  ST_GUID

</ExperienceId>
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
<td>[DeviceCompanionApplication](element-devicecompanionapplication.md)</td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Windows Store device app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of the ExperienceId element is a 128-bit Globally Unique Identifier (GUID).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2015/StoreManifest</p></td>
</tr>
</tbody>
</table>

 

 



