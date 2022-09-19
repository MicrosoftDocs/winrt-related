---
description: Specifies the main app package to which this supplemental package applies.
Search.Product: eADQiWindows 10XVcnh
title: uap3:MainPackageDependency (Windows 10)
ms.assetid: 8de4b12b-0f0d-48d0-b3ff-28aae81fb13c
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:MainPackageDependency (Windows 10)

Specifies the main app package to which this supplemental package applies.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Dependencies\>](element-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:MainPackageDependency\>**

## Syntax

```xml
<uap3:MainPackageDependency
    Name = 'A string with a value between 3 and 50 characters in length that consists of alpha-numeric characters, periods, and dashes.' >
</uap3:MainPackageDependency>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name**  | The name as it appears in the *Name* attribute of the [Identity](element-identity.md) element of the dependency package. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric characters, periods, and dashes. | Yes |  |

### Child elements

None.

### Parent elements

| Parent Element | Description |
|-|-|
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
