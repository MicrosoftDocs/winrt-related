---
Description: The abstract device capability choice element for the XSD substitution group. 
Search.Product: eADQiWindows 10XVcnh
title: DeviceCapabilityChoice
ms.assetid: 44d764bb-041e-455d-862e-23fb95eec9e9
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# DeviceCapabilityChoice




The abstract device capability choice element for the XSD substitution group. This can't be declared in the XML.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;DeviceCapabilityChoice&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DeviceCapabilityChoice>

  xs:anyType

</DeviceCapabilityChoice>
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
<td>[Capabilities](element-capabilities.md)</td>
<td><p>Declares the access to protected user resources that the package requires.</p></td>
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
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



