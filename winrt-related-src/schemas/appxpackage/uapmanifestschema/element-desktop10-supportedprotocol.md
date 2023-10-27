---
title: desktop10:SupportedProtocol
description: Specifies a URL protocol scheme.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:SupportedProtocol

Specifies a URL protocol scheme.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:SupportedProtocols\>](element-desktop10-supportedprotocols.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:SupportedProtocol\>**

## Syntax

```xml
<desktop10:SupportedProtocol>
  A string with a value between 2 and 2048 characters in length.
</desktop10:SupportedProtocol>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:SupportedProtocols](element-desktop10-supportedprotocols.md) | Specifies the supported URL protocol schemes for a given key. |

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |
