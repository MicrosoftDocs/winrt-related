---
title: s2:RelatedPackages
description: Specifies the related packages. These packages won't be installed as part of the deployment operation. (s2:RelatedPackages)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:RelatedPackages

## Description

Specifies the related packages. These packages won't be installed as part of the deployment operation. (s2:RelatedPackages)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:RelatedPackages&gt;

## Syntax

```syntax
<s2:RelatedPackages>
<!-- Child elements -->
  Package{0,1}
  Bundle{0,1}
</s2:RelatedPackages>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s2:Package](element-s2-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [s2:Bundle](element-s2-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:AppInstaller](element-s2-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s2) | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |
| Minimum OS version | Windows 10 version 1803 build 17134 |
