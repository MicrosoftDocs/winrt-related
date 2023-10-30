---
description: Indicates whether virtualization for the file system is enabled for a package.
title: virtualization:FileSystemWriteVirtualization
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/18/2022
ms.custom: 
---

# virtualization:FileSystemWriteVirtualization

Indicates whether virtualization for the file system is enabled for a package. Disabling virtualization enables your app to access the global file system (or registry) locations seen by other apps, rather than the virtualized file system (or registry) that is created for your app. Any data written to these unvirtualized locations will persist after your app is uninstalled.

> [!NOTE]
> This element requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<virtualization:FileSystemWriteVirtualization\>**

## Syntax

```xml
<virtualization:FileSystemWriteVirtualization>

    <!-- Child elements -->
    virtualization:ExcludedDirectories

</virtualization:FileSystemWriteVirtualization>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [virtualization:ExcludedDirectories](element-virtualization-excludeddirectories.md) | Specifies the list of directories that are excluded from file system virtualization. |

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

Only file system locations under the `%USERPROFILE%\AppData` directory support virtualization, and therefore these are the only locations that can be specified to be excluded from virtualization.

This schema and syntax were introduced in the Windows 10, version 2004. Previously, in the Windows 10, version 1903 release, similar functionality was introduced with the [desktop6:FileSystemWriteVirtualization](element-desktop6-filesystemwritevirtualization.md) element. If an application includes both syntaxes for disabling file system virtualization, the old declaration will be used on pre-2004 OS versions while the new declaration will be used on 2004 and later OS versions.

## Requirements

| Item | Value |
|--|--|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
