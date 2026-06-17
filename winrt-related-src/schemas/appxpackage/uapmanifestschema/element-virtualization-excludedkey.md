---
title: virtualization:ExcludedKey
description: Specifies a key that is excluded from registry key virtualization.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, virtualization:Package, virtualization:Properties, virtualization:RegistryWriteVirtualization, virtualization:ExcludedKeys, virtualization:ExcludedKey]
---

# virtualization:ExcludedKey

Specifies a key that is excluded from registry key virtualization.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<virtualization:RegistryWriteVirtualization>`](element-virtualization-registrywritevirtualization.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<virtualization:ExcludedKeys>`](element-virtualization-excludedkeys.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<virtualization:ExcludedKey>`**  

## Syntax

```xml
<virtualization:ExcludedKey>
  This element is a case-insensitive string that must start with "HKEY_CURRENT_USER" or "HKCU" specifying the root of the registry path to the the excluded key. The rest of the string is the relative path to the excluded key. For example, "HKEY_CURRENT_USER\Software\Fabrikam\Shared".
</virtualization:ExcludedKey>
```

## Value

This element is a case-insensitive string that must start with "HKEY_CURRENT_USER" or "HKCU" specifying the root of the registry path to the the excluded key. The rest of the string is the relative path to the excluded key. For example, "HKEY_CURRENT_USER\Software\Fabrikam\Shared".

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [virtualization:ExcludedKeys](element-virtualization-excludedkeys.md) | Specifies the list of keys that are excluded from registry virtualization. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
