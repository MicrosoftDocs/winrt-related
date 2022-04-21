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

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-virtualization-registrywritevirtualization.md">&lt;virtualization:RegistryWriteVirtualization&gt;</a></dt>
<dd><b>&lt;virtualization:ExcludedKeys&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<virtualization:ExcludedKeys>
    virtualization:ExcludedKey {0,1000}
</virtualization:ExcludedKeys>
```

### Key 

`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [virtualization:ExcludedKey](element-virtualization-excludedkey.md) | Specifies a key that is excluded from registry key virtualization. |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [virtualization:RegistryWriteVirtualization](element-virtualization-registrywritevirtualization.md) | Indicates whether virtualization for the registry for your package.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |

 

 
