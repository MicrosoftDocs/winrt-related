---
title: uap3:MainPackageDependency
description: Specifies the main app package to which this supplemental package applies.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Extensions, uap3:Package, uap3:Dependencies, uap3:MainPackageDependency]
keywords: windows 10, uwp, schema, package manifest
---

# uap3:MainPackageDependency

Specifies the main app package to which this supplemental package applies.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:MainPackageDependency>`**

## Syntax

```xml
<uap3:MainPackageDependency
  Name = 'A required value. <!-- TODO: Add description for t:ST_PackageName -->' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name as it appears in the *Name* attribute of the [Identity](element-f-identity.md) element of the dependency package. | A value. <!-- TODO: Add data type for t:ST_PackageName --> | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="uap3">
    <Dependencies>  
        <TargetDeviceFamily
            Name="Windows.Universal"
            MinVersion="11.0.0.0" 
            MaxVersionTested="12.0.0.0"/>  
        <uap3:MainPackageDependency
            Name="MyApp.Main"/>  
    </Dependencies>  
</Package>
```
