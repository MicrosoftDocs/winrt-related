---
title: uap10:HostRuntime
description: This extension provides a means to deliver translated app resources (in Package/Extensions).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap10:Extension, uap10:HostRuntime]
---

# uap10:HostRuntime

Defines a package-wide extension that defines the runtime information to be used when activating a [hosted app](/windows/uwp/launch-resume/hosted-apps).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:Extension>`](element-uap10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:HostRuntime>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:Extension>`](element-uap10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:HostRuntime>`**  

## Syntax

```xml
<uap10:HostRuntime
  Id = 'A required alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The unique identifier of this specific host app in the package. | A alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
