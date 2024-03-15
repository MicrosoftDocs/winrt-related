---
title: desktop10:SupportedProtocols
description: Specifies the supported URL protocol schemes for the extension.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:SupportedProtocols

Specifies the supported URL protocol schemes for the extension.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:SupportedProtocols\>**

## Syntax

```xml
<desktop10:SupportedProtocols>

  <!-- Child Elements -->
  desktop10:SupportedProtocol{0, 10000}

</desktop10:SupportedProtocols>
```

### Key

`{}` A specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop10:SupportedProtocol](element-desktop10-supportedprotocol.md) | Specifies a URL protocol scheme. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Remarks

The behavior of this element is comparable to setting supported protocols for unpackaged apps in the registry as described in [Application Registration](/windows/win32/shell/app-registration). The attributes and child elements from the desktop10 namespace are only supported on extension instances that specify CompatMode="classic" and are only supported on desktop SKUs.

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |
