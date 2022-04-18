---
description: Specifies a directory that is excluded from file system virtualization.
title: desktop6:FileSystemWriteVirtualization


keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/18/2022
ms.custom: 
---

# desktop6:FileSystemWriteVirtualization

Specifies a directory that is excluded from file system virtualization. 

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
<dd>
<dl>
<dt><a href="element-virtualization-exludeddirectories.md">&lt;virtualization:ExcludedDirectories&gt;</a></dt>
<dd><b>&lt;virtualization:ExcludedDirectory&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` xml
<desktop6:FileSystemWriteVirtualization>disabled</desktop6:FileSystemWriteVirtualization>
```

## Value

This element is a case-insensitive string that must start with "KnownFolder:&lt;folder name&gt;" where *folder name* specifies one of the known folders under the AppData directory. The rest of the string is the relative path to the excluded directory. For example, `KnownFolder:LocalAppData)\Fabrikam\Shared`. 

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [virtualization:ExcludedDirectories](element-virtualization-excludeddirectories.md) | Specifies the list of directories that are excluded from file system virtualization.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| virtualization | `http://schemas.microsoft.com/appx/manifest/virtualization/windows10` |

 

 
