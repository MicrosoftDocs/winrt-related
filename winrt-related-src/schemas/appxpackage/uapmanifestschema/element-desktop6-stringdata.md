---

title: desktop6:StringData
description: Specifies one or more string data values for a trigger event of a service (desktop6:StringData).

ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:StringData

## Description

Specifies one or more string data values for a trigger event of a service.

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
<dd><b>&lt;desktop6:StringData&gt;</b></dd>
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
<desktop6:StringData>
    desktop6:DataItem{1,1000}
</desktop6:StringData>
```

## Attributes and Elements

### Attributes

None.


### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop6:DataItem](element-desktop6-dataitem.md) | Specifies a string value for the trigger event. |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [TriggerCustom](element-desktop6-triggercustom.md) | Describes a trigger event for the current service. |  


## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).


## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |