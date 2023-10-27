---
description: Specifies the list of directories that are excluded from file system virtualization.
title: virtualization:ExcludedDirectories
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/18/2022
ms.custom: 
---

# virtualization:ExcludedDirectories

Specifies the list of directories that are excluded from file system virtualization.

> [!NOTE]
> This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<virtualization:FileSystemWriteVirtualization\>](element-virtualization-filesystemwritevirtualization.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<virtualization:ExcludedDirectories\>**

## Syntax

```xml
<virtualization:ExcludedDirectories>

    <!-- Child elements -->
    ExcludedDirectory {0, 1000}

</virtualization:ExcludedDirectories>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [virtualization:ExcludedDirectory](element-virtualization-excludeddirectory.md) | Specifies a directory that is excluded from file system virtualization. |

### Parent elements

| Parent element | Description |
|-|-|
| [virtualization:FileSystemWriteVirtualization](element-virtualization-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for a package.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Item | Value |
|-|-|
| **virtualization** | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| Minimum OS Version | Windows 10 (Build 20348) |
