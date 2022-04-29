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
> This element requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-virtualization-filesystemwritevirtualization.md">&lt;virtualization:FileSystemWriteVirtualization&gt;</a></dt>
<dd><b>&lt;virtualization:ExcludedDirectories&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<virtualization:ExcludedDirectories>
    ExcludedDirectory {0, 1000}
</virtualization:ExcludedDirectories>
```



### Key 

`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [virtualization:ExcludedDirectory](element-virtualization-excludeddirectory.md) | Specifies a directory that is excluded from file system virtualization. |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [virtualization:FileSystemWriteVirtualization](element-virtualization-filesystemwritevirtualization.md) | Indicates whether virtualization for the file system is enabled for a package.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |

 

 
