---
Description: Function
MS-HAID: AppxManifestSchema2013.element\_Function
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Function
ms.assetid: d53133f1-6017-4c20-bbff-f2370c5fc39d
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# Function




Declares the function for the device.

## Element hierarchy

<dl>
<dt><a href="element-devicecapability.md">&lt;DeviceCapability&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-device.md">&lt;Device&gt;</a></dt>
<dd><b>&lt;Function&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Function Type = A string between 1 and 100 characters in length. />
```

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
<td><strong>Type</strong></td>
<td><p>The type of function for the device.</p></td>
<td>A string between 1 and 100 characters in length.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td>[Device](element-device.md)</td>
<td><p>Declares a function for a device that is associated with the [<strong>DeviceCapability</strong>](element-devicecapability.md).</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2013/manifest</p></td>
</tr>
</tbody>
</table>

 

 



