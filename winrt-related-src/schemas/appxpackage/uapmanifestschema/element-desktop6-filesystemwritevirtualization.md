---
title: desktop6:FileSystemWriteVirtualization
description: Indicates whether virtualization for the file system is enabled for your desktop application.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, desktop6:Package, desktop6:Properties, desktop6:FileSystemWriteVirtualization]
---

# desktop6:FileSystemWriteVirtualization

Indicates whether virtualization for the file system is enabled for your desktop application. If disabled, other apps can read or write the same file system entries as your application. 

> [!NOTE]
> This element is currently intended to be used only by certain types of desktop PC games that are published by Microsoft and our partners. It requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:FileSystemWriteVirtualization>`**

## Syntax

```xml
<desktop6:FileSystemWriteVirtualization>
    <!-- TODO: Add value description -->
</desktop6:FileSystemWriteVirtualization>
```

## Value

This element can have the value **enabled** or **disabled**. The default is **enabled**.

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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
