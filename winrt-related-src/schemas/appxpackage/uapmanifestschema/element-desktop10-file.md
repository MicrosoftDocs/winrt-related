---
title: desktop10:File
description: TBD
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:File

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
<dd>
<dl>
<dt><a href="element-desktop10-eventmessagefiles.md">&lt;desktop10:EventMessageFiles&gt;</a></dt>
<dd><strong>&lt;desktop10:File&gt;</strong></dd>
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
<desktop10:File
  Path = A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", |, ?, or *.
  >

</desktop10:File>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| Path | TBD | A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |

### Child Elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |