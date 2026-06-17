---
title: uap10:AllowExternalContent
description: Enables your package manifest to reference content outside the package, in a specific location on disk, for packages with external location.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap10:Package, uap10:Properties, uap10:AllowExternalContent]
---

# uap10:AllowExternalContent

Enables your package manifest to reference content outside the package, in a specific location on disk. See [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:AllowExternalContent>`**  

## Syntax

```xml
<uap10:AllowExternalContent>
    <!-- TODO: Add value description -->
</uap10:AllowExternalContent>
```

## Value

<!-- TODO: Add value description -->

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

The **uap10:AllowExternalContent** element contains a boolean value. For more information about the use of the element, see [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps).

## Examples

<!-- Author content goes here -->
