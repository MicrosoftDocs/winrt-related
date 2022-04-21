---
description: Specifies a key that is excluded from registry key virtualization.
title: virtualization:ExcludedKey


keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/18/2022
ms.custom: 
---

# virtualization:ExcludedKey

Specifies a key that is excluded from registry key virtualization. 

> [!NOTE]
> This element requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;desktop6:FileSystemWriteVirtualization&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<virtualization:ExcludedKey>HKEY_CURRENT_USER\[path to registry key]</virtualization:ExcludedKey>
```

## Value

This element is a case-insensitive string that must start with "HKEY_CURRENT_USER" or "HKCU" specifying the root of the registry path to the the excluded key. The rest of the string is the relative path to the excluded key. For example, `HKEY_CURRENT_USER\Software\Fabrikam\Shared`.  

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [virtualization:ExcludedKeys](element-virtualization-excludedkeys.md) | Specifies the list of keys that are excluded from registry virtualization.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |

 

 
