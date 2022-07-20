---
title: desktop10:SupportedProtocols
description: Specifies the supported URL protocol schemes for a given key.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:SupportedProtocols

## Description

Specifies the supported URL protocol schemes for a given key.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd><strong>&lt;desktop10:SupportedProtocols&gt;</strong></dd>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

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

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:SupportedProtocol](element-desktop10-supportedprotocol.md) | Specifies a URL protocol scheme. |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |