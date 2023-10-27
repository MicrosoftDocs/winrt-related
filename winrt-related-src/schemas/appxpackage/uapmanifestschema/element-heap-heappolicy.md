---
description: Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap.
title: heap:HeapPolicy
keywords: windows 10, schema, package manifest
ms.topic: reference
ms.date: 09/06/2022
ms.custom: 
---

# heap:HeapPolicy

Allows packaged apps to request a heap profile that has performance and behavior characteristics consistent with that of the legacy NT heap.


&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

## Element hierarchy

[\<Package\>](element-package.md)


&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<heap:HeapPolicy\>**

## Syntax


``` xml
<heap:HeapPolicy  type = "win32Compatible" | "default" >
</heap:HeapPolicy>
```

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| type | Specifies the requested heap type. | A string value that can be one of the following: "win32Compatible", "default" | No |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users  |

## Remarks

The segment heap is the recommend heap implementation on Windows and has, by default, backed all process heaps for packaged apps since its inception. Now that MSIX now supports several different app types, including desktop apps, a mechanism has been provided by which packages can request legacy heap behavior for their apps. Setting the value of the **type** attribute to "win32Compatible" requests for the heap for the app to be initialized with legacy behavior and performance. This serves only as a hint to the heap initialization code which may decide on alternate settings based on internal criteria.

## Requirements

| Namespace | Manifest Path | 
|---------------|-------------------------------------------------------------|
| heap | `http://schemas.microsoft.com/appx/manifest/heap/windows10` |
| Minimum OS Version | Windows 11 version 21H2 (Build 22000) |
