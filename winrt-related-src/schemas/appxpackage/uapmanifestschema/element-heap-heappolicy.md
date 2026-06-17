---
title: heap:HeapPolicy
description: Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, schema, package manifest
no-loc: [Package, Extensions, heap:Package, heap:Properties, heap:HeapPolicy]
---

# heap:HeapPolicy

Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<heap:HeapPolicy>`**  

## Syntax

```xml
<heap:HeapPolicy>
    <!-- A string value: "win32Compatible" or "default" -->
</heap:HeapPolicy>
```

## Value

Specifies the requested heap type. The value can be one of the following strings: "win32Compatible" or "default".

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/heap/windows10` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

The segment heap is the recommend heap implementation on Windows and has, by default, backed all process heaps for packaged apps since its inception. Now that MSIX now supports several different app types, including desktop apps, a mechanism has been provided by which packages can request legacy heap behavior for their apps. Setting the value of the **type** attribute to "win32Compatible" requests for the heap for the app to be initialized with legacy behavior and performance. This serves only as a hint to the heap initialization code which may decide on alternate settings based on internal criteria.

## Examples

<!-- Author content goes here -->
