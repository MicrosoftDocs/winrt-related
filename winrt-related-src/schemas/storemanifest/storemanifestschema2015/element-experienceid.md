---
description: The ExperienceId element specifies a GUID that links the device metadata to a device app that can be automatically acquired when the device is first connected.
Search.Product: eADQiWindows 10XVcnh
title: ExperienceId
ms.assetid: fb3585cf-8f9c-4ae6-8430-685ccc132a98


keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-devicecompanionapplication.md">DeviceCompanionApplication</a> </td>
<td><p>The DeviceCompanionApplication element contains all the configuration required to declare your app as a Microsoft Store device app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of the ExperienceId element is a 128-bit Globally Unique Identifier (GUID).

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2015/StoreManifest` |

 

 



