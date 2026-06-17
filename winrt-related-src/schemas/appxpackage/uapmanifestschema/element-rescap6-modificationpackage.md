---
title: rescap6:ModificationPackage
description: Declares that the current package is a modification package for an enterprise application.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, rescap6:Package, rescap6:Properties, rescap6:ModificationPackage]
---

# rescap6:ModificationPackage

Declares that the current package is a [modification package](/windows/msix/modification-packages) for an enterprise application.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap6:ModificationPackage>`**  

## Syntax

```xml
<rescap6:ModificationPackage>
    <!-- TODO: Add value description -->
</rescap6:ModificationPackage>
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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |

## Remarks

This element represents a restricted property that is only supported in [optional packages](/windows/uwp/packaging/optional-packages). This element is currently intended to be used only for enterprise applications. We don't recommend that you declare this capability in applications that you submit to the Microsoft Store. In most cases, the use of this element won't be approved.

For more information, see [Modification packages](/windows/msix/modification-packages).

## Examples

<!-- Author content goes here -->
