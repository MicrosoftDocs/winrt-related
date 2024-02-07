---
title: s4:OptionalPackages
description: Specifies the optional packages that will be installed along with the main package. (s4:OptionalPackages)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:OptionalPackages

## Description

Specifies the optional packages that will be installed along with the main package. (s4:OptionalPackages)


## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:OptionalPackages&gt;

## Syntax

```syntax
<s4:OptionalPackages>
<!-- Child elements -->
  ( Bundle{0,10000}
  | Package{0,10000}
  )
</s4:OptionalPackages>
```

### Key

`{}`   specific range of occurrences


## Child Elements

| Element | Description |
| -----------| -------------|
| [Package](element-s4-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [Bundle](element-s4-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri.  |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:AppInstaller](element-s4-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s4) | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows version 21H2 build 22000 |
