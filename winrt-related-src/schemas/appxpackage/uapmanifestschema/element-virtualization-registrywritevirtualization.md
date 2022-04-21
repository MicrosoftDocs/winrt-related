---
description: Indicates whether virtualization for the registry is enabled for your package.
title: virtualization:RegistryWriteVirtualization


keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/18/2022
ms.custom: 
---

# virtualization:RegistryWriteVirtualization

Indicates whether virtualization for the registry for your package. If disabled, other apps can read or write the same registry entries as your package. 

> [!NOTE]
> This element requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;virtualization:RegistryWriteVirtualization&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<virtualization:RegistryWriteVirtualization>
    virtualization:ExcludedKeys
</virtualization:RegistryWriteVirtualization>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [virtualization:ExcludedKeys](element-virtualization-excludedkeys.md) | Specifies the list of keys that are excluded from registry virtualization. |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).


You can only declare registry locations under the HKEY_CURRENT_USER to be excluded from virtualization. This schema and syntax were introduced in the Windows 10, version 2004. Previously, in the Windows 10, version 1903 release, similar functionality was introduced with the [desktop6:RegistryWriteVirtualization](element-desktop6-registrywritevirtualization.md) element. If an application includes both syntaxes for disabling file system virtualization, the old declaration will be used on pre-2004 OS versions while the new declaration will be used on 2004 and later OS versions.

## Requirements

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |

 

 
