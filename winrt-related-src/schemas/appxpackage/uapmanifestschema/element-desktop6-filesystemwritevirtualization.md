---
description: Indicates whether virtualization for the file system is enabled for your desktop application.
title: desktop6:FileSystemWriteVirtualization


keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/19/2019
ms.custom: 19H1
---

# desktop6:FileSystemWriteVirtualization

Indicates whether virtualization for the file system is enabled for your desktop application. If disabled, other apps can read or write the same file system entries as your application. 

> [!NOTE]
> This element is currently intended to be used only by certain types of desktop PC games that are published by Microsoft and our partners. It requires the  **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

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
<desktop6:FileSystemWriteVirtualization>disabled</desktop6:FileSystemWriteVirtualization>
```

## Value

This element can have the value **enabled** or **disabled**. The default is **enabled**. 

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users.  |

## Remarks

This element requires the **unvirtualizedResources** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |

 

 
