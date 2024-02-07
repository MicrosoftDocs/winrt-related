---
title: s3:RelatedPackages
description: Specifies the related packages. These packages won't be installed as part of the deployment operation. (s3:RelatedPackages)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:RelatedPackages

## Description

Specifies the related packages. These packages won't be installed as part of the deployment operation. (s3:RelatedPackages)


## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s3:RelatedPackages&gt;

## Syntax

```syntax
<s3:RelatedPackages>
<!-- Child elements -->
  Package
  Bundle
</s3:RelatedPackages>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s3:Package](element-s3-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [s3:Bundle](element-s3-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:AppInstaller](element-s3-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s3) | `http://schemas.microsoft.com/appx/appinstaller/2018` |
| Minimum OS version | Windows version 1809 build 17763 |
