---
author: mcleanbyron
title: desktop6:BinaryData
description: Specifies binary data for a trigger event of a service.
ms.author: mcleans
ms.date: 03/12/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:BinaryData

## Description

Specifies binary data for a trigger event of a service.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-extension.md">&lt;desktop6:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-service.md">&lt;desktop6:Service&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-triggerevents.md">&lt;desktop6:TriggerEvents&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-triggercustom.md">&lt;desktop6:TriggerCustom&gt;</a></dt>
<dd><b>&lt;desktop6:BinaryData&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```xml
<desktop6:BinaryData File = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >
</desktop6:BinaryData>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| File | The name of the package file that contains the binary data (as an array of bytes). | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", /|, ?, or *. | Yes |


### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [TriggerCustom](element-desktop6-triggercustom.md) | Describes a trigger event for the current service. |  


## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/6</p></td>
</tr>
</tbody>
</table>
