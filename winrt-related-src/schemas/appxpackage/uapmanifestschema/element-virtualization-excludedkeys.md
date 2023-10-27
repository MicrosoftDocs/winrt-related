---
description: Specifies the list of keys that are excluded from registry virtualization.
title: virtualization:ExcludedKeys
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 
ms.custom: 04/18/2022
---

# virtualization:ExcludedKeys

Specifies the list of keys that are excluded from registry virtualization.

> [!NOTE]
> This element requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<virtualization:FileSystemWriteVirtualization\>](element-virtualization-filesystemwritevirtualization.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<virtualization:ExcludedKeys\>**

## Syntax

``` xml
<virtualization:ExcludedKeys>

    <!-- Child elements -->
    virtualization:ExcludedKey {0,1000}

</virtualization:ExcludedKeys>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [virtualization:ExcludedKey](element-virtualization-excludedkey.md) | Specifies a key that is excluded from registry key virtualization. |

### Parent elements

| Parent element | Description |
|-|-|
| [virtualization:RegistryWriteVirtualization](element-virtualization-registrywritevirtualization.md) | Indicates whether virtualization for the registry for your package.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Item | Value |
|--|--|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| Minimum OS Version | Windows 10 (Build 20348) |
