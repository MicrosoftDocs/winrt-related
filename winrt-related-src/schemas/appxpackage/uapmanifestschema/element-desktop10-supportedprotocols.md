---
title: desktop10:SupportedProtocols
description: Specifies the supported URL protocol schemes for a given key.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:SupportedProtocols

Specifies the supported URL protocol schemes for a given key.

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

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| Minimum OS Version | Windows 11 version 22H2 (Build 22621) |
