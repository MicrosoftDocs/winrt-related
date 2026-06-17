---
title: desktop4:ContentUriSource
description: Registration of a Windows Shell BannersHandler for cloud based placeholder files (desktop4:ContentUriSource).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop4:Extension, desktop4:CloudFiles, desktop4:ContentUriSource]
---

# desktop4:ContentUriSource

Registration of a Windows Shell ContentUriSource enabling cloud storage providers to provide a file ID for a given local path.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:Extension>`](element-desktop4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:CloudFiles>`](element-desktop3-cloudfiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop4:ContentUriSource>`**

## Syntax

```xml
<desktop4:ContentUriSource
  Clsid = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | The class ID of the app that implements the ContentUriSource. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop3:CloudFiles](element-desktop3-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also

[Creating Shell Extension Handlers](/windows/win32/shell/handlers)
