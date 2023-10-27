---
ms.assetid: 4230de7d-5e70-4f11-a8c4-19c94394b7a4
title: desktop2:FilterExtension
description: Specifies the file type to be registered by the app.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:FilterExtension

Specifies the file type to be registered by the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:SearchFilterHandler\>](element-desktop2-searchfilterhandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:FilterExtension\>**

## Syntax

```xml
<desktop2:FilterExtension
  Name = 'A string with a value between 1 and 64 characters in length that must begin with a period ("."), cannot have additional periods, and cannot contain these characters: <, >, :, ", /, \, |, ?, or *.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| Name | A file extension. | A string between 1 and 64 characters in length that must begin with a period (`.`), cannot have additional periods (`.`), and cannot contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:SearchFilterHandler](element-desktop2-searchfilterhandler.md) | Enables Windows Desktop Bridge apps to register IFilters to extract file properties for searching. |

## Requirements

| Item | Value |
|-|-|
|**Namespace**|`http://schemas.microsoft.com/appx/manifest/desktop/windows10/2`|
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
