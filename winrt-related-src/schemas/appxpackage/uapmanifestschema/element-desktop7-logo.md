---

title: desktop7:Logo
description: A path to a file that contains an image (desktop7).
ms.date: 08/12/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:Logo

## Description
A path to a file that contains an image.

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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-filetypeassociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;desktop7:Logo&gt;</b></dd>
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
<desktop7:Logo ResourceId   = A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters. Allows the following file extensions: ".jpg", ".jpeg", ".png", ".ico".>
</desktop7:Logo>
```


## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ResourceId | The string table ID of the string Infotip string within the resource module. | A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters. Allows the following file extensions: ".jpg", ".jpeg", ".png", ".ico".| Yes |

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