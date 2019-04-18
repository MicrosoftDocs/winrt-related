---
author: mcleanbyron
title: desktop6:DataItem
description: Specifies one or more string data values for a trigger event of a service.
ms.author: mcleans
ms.date: 03/12/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:DataItem

## Description

Specifies a string value for a trigger event of a service.

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
<dd>
<dl>
<dt><a href="element-desktop6-stringdata.md">&lt;desktop6:StringData&gt;</a></dt>
<dd><b>&lt;desktop6:DataItem&gt;</b></dd>
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
</dd>
</dl>


## Syntax
```xml
<desktop6:DataItem Value = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
</desktop6:DataItem>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Value | The value of the string. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |


### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for a trigger event of a service. |  


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
