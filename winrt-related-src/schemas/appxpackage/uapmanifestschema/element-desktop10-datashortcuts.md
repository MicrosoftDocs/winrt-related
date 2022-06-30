---
title: desktop10:DataShortcuts
description: Specifies a list of non-executable shortcuts.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:DataShortcuts

## Description

Specifies a list of non-executable shortcuts. 

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd><strong>&lt;desktop10:DataShortcuts&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:DataShortcuts>
  <!-- Child Elements -->
  desktop10:DataShortcut

</desktop10:DataShortcuts>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:DataShortcut](element-desktop10-datashortcut.md) | Creates a shortcut to a file that is not an executable. |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |