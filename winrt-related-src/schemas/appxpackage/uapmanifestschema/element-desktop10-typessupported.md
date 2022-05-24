---
title: desktop10:TypesSupported
description: TBD
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:TypesSupported

## Description

TBD

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-customdesktopeventlog.md">&lt;desktop10:CustomDesktopEventLog&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-customeventsource.md">&lt;desktop10:CustomEventSource&gt;</a></dt>
<dd><strong>&lt;desktop10:TypesSupported&gt;</strong></dd>
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
<desktop10:TypesSupported>
  <!-- Child Elements -->
  desktop10:TypeSupported

</desktop10:TypesSupported>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:TypeSupported](element-desktop10-typesupported.md) | TBD |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |