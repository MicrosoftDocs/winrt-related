---
title: desktop10:EventMessageFiles
description: Defines 1 or more DLL files containing the language strings describing the events.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:EventMessageFiles

## Description

Defines 1 or more DLL files containing the language strings describing the events.

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
  desktop10:File{0,10000}

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
| [desktop10:File](element-desktop10-file.md) | Specifies an event log DLL within the package. |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Defines an event source within a custom event log. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |