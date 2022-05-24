---
title: desktop10:EventMessageFiles
description: TBD
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:EventMessageFiles

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
<dd><strong>&lt;desktop10:EventMessageFiles&gt;</strong></dd>
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
<desktop10:EventMessageFiles>
  <!-- Child Elements -->
  desktop10:File

</desktop10:EventMessageFiles>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:File](element-desktop10-file.md) | TBD |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |