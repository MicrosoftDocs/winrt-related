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

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<virtualization:ExcludedKey\>**

## Syntax

``` xml
<virtualization:ExcludedKey>
  This element is a case-insensitive string that must start with "HKEY_CURRENT_USER" or "HKCU" specifying the root of the registry path to the the excluded key. The rest of the string is the relative path to the excluded key. For example, "HKEY_CURRENT_USER\Software\Fabrikam\Shared".
</virtualization:ExcludedKey>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [virtualization:ExcludedKeys](element-virtualization-excludedkeys.md) | Specifies the list of keys that are excluded from registry virtualization.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Item | Value |
|--|--|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
