---
title: virtualization:ExcludedKeys
description: Specifies the list of keys that are excluded from registry virtualization.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, virtualization:Package, virtualization:Properties, virtualization:RegistryWriteVirtualization, virtualization:ExcludedKeys]
---

# virtualization:ExcludedKeys

Specifies the list of keys that are excluded from registry virtualization.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<virtualization:RegistryWriteVirtualization>`](element-virtualization-registrywritevirtualization.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<virtualization:ExcludedKeys>`**  

## Syntax

```xml
<virtualization:ExcludedKeys>

  <!-- Child elements -->
  virtualization:ExcludedKey{0,1000}

</virtualization:ExcludedKeys>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [virtualization:ExcludedKey](element-virtualization-excludedkey.md) | Specifies a key that is excluded from registry key virtualization. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:RegistryWriteVirtualization](element-desktop6-registrywritevirtualization.md) | Indicates whether virtualization for the registry is enabled for your desktop application. If disabled, other apps can read or write the same registry entries as your application. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
