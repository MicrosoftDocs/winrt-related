---
title: virtualization:RegistryWriteVirtualization
description: Indicates whether virtualization for the registry is enabled for your package.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, virtualization:Package, virtualization:Properties, virtualization:RegistryWriteVirtualization]
---

# virtualization:RegistryWriteVirtualization

Specifies a list of keys for which registry virtualization is disabled for a package. Disabling virtualization enables your app to access the global registry (or file system) locations seen by other apps, rather than the virtualized registry (or file system) that is created for your app. Any data written to these unvirtualized locations will persist after your app is uninstalled.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<virtualization:RegistryWriteVirtualization>`**  

## Syntax

```xml
<virtualization:RegistryWriteVirtualization>

  <!-- Child elements -->
  virtualization:ExcludedKeys

</virtualization:RegistryWriteVirtualization>
```

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [virtualization:ExcludedKeys](element-virtualization-excludedkeys.md) | Specifies the list of keys that are excluded from registry virtualization. |

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

You can only declare registry locations under the `HKEY_CURRENT_USER` to be excluded from virtualization. This schema and syntax were introduced in the Windows 10, version 2004. Previously, in the Windows 10, version 1903 release, similar functionality was introduced with the [desktop6:RegistryWriteVirtualization](element-desktop6-registrywritevirtualization.md) element. If an application includes both syntaxes for disabling file system virtualization, the old declaration will be used on pre-2004 OS versions while the new declaration will be used on 2004 and later OS versions.

## Examples

<!-- Author content goes here -->
