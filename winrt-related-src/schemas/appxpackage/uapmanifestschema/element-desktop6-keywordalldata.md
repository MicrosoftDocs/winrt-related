---
author: mcleanbyron
title: desktop6:KeywordAllData
description: Specifies a 64-bit unsigned integer value for a trigger event of a service.
ms.author: mcleans
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:KeywordAllData

## Description

Specifies a 64-bit unsigned integer value for a trigger event of a service.

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
<dd><b>&lt;desktop6:KeywordAllData&gt;</b></dd>
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
<desktop6:KeywordAllData Value = A 64-bit unsigned integer value. >
</desktop6:KeywordAllData>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Value | The data value for the trigger event. | A 64-bit unsigned integer value. | Yes |


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
