---
title: virtualization:ExcludedDirectories
description: Specifies the list of directories that are excluded from file system virtualization.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, virtualization:Package, virtualization:Properties, virtualization:FileSystemWriteVirtualization, virtualization:ExcludedDirectories]
---

# virtualization:ExcludedDirectories

Specifies the list of directories that are excluded from file system virtualization.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<virtualization:FileSystemWriteVirtualization>`](element-virtualization-filesystemwritevirtualization.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<virtualization:ExcludedDirectories>`**  

## Syntax

```xml
<virtualization:ExcludedDirectories>

  <!-- Child elements -->
  virtualization:ExcludedDirectory{0,1000}

</virtualization:ExcludedDirectories>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [virtualization:ExcludedDirectory](element-virtualization-excludeddirectory.md) | Specifies a directory that is excluded from file system virtualization. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:FileSystemWriteVirtualization](element-desktop6-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for your desktop application. If disabled, other apps can read or write the same file system entries as your application. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
