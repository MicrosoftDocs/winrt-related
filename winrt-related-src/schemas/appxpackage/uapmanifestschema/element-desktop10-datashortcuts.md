---
title: desktop10:DataShortcuts
description: Specifies a list of non-executable shortcuts.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:DataShortcuts

Specifies a list of non-executable shortcuts.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:DataShortcuts\>**

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

### Child elements

| Child element | Description |
|-|-|
| [desktop10:DataShortcut](element-desktop10-datashortcut.md) | Creates a shortcut to a file that is not an executable. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| Minimum OS Version | Windows 11 version 22H2 (Build 22621) |
