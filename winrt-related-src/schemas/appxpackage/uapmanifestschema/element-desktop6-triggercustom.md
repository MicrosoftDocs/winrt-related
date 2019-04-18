---
author: mcleanbyron
title: desktop6:TriggerCustom
description: Describes a trigger event for the current service.
ms.author: mcleans
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:TriggerCustom

## Description

Describes a trigger event for the current service.

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
<dd><b>&lt;desktop6:TriggerCustom&gt;</b></dd>
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
<desktop6:TriggerCustom    Action   =  The following values are supported: ActionStart, ActionStop  
                           Subtype  =  A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >
    ( desktop6:StringData{0,1000}
      desktop6:BinaryData{0,1000}
      desktop6:LevelData{0,1000}
      desktop6:KeywordAnyData{0,1000}
      desktop6:KeywordAllData{0,1000} )
</desktop6:TriggerCustom>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Action | The action type for the trigger event. | The following values are supported: **ActionStart**, **ActionStop** | Yes |
| Subtype  | A GUID that identifies the trigger event subtype. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  | Yes |


### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop6:StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for the trigger event. |  
| [desktop6:BinaryData](element-desktop6-binarydata.md) | Specifies binary data for the trigger event.  |  
| [desktop6:LevelData](element-desktop6-leveldata.md) | Specifies a byte value for the trigger event. |  
| [desktop6:KeywordAnyData](element-desktop6-keywordanydata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  
| [desktop6:KeywordAllData](element-desktop6-keywordalldata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |  


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
