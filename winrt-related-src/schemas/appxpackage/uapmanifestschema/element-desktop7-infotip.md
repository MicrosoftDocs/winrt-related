---

title: desktop7:InfoTip
description: Specifies the Infotip string to show when the mouse hovers over the item’s icon.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:InfoTip

## Description
Specifies the Infotip string to show when the mouse hovers over the item’s icon.

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
<dt><a href="element-desktop7-extension.md">&lt;desktop7:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop7-controlpanelitem.md">&lt;desktop7:ControlPanelItem&gt;</a></dt>
<dd><b>&lt;desktop7:InfoTip&gt;</b></dd>
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
<desktop7:InfoTip ResourceId   = A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters. >
</desktop7:InfoTip>
```


## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ResourceId | The string table ID of the string Infotip string within the resource module. | A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters. | Yes |

### Child Elements

None

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [ControlPanelItem](element-desktop7-controlpanelitem.md) | Registers an extension as a control panel item. |  


## Remarks



## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |