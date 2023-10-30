---
title: uap10:HostRuntime
description: This extension provides a means to deliver translated app resources (in Package/Extensions).
ms.date: 03/05/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:HostRuntime

Defines a package-wide extension that defines the runtime information to be used when activating a [hosted app](/windows/uwp/launch-resume/hosted-apps).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:Extensions\>](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:HostRuntime\>**

## Syntax

```xml
<uap10:HostRuntime
  Id = 'An ASCII string with a value between 1 and 256 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** |  The unique identifier of this specific host app in the package. | An ASCII string with a value between 1 and 256 characters in length. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |
