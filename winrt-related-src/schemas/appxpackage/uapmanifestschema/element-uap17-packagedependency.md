---
title: uap17:PackageDependency
description: Declares other packages that a package depends on. This dependency can be specified as required for both install time and runtime or just install time but not runtime.
ms.date: 10/12/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# uap17:PackageDependency



## Description

Declares other packages that a package depends on. This dependency can be specified as required for both install time and runtime or just install time but not runtime.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;uap17:PackageDependency&gt;</b></dd></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap17:PackageDependency     Type? = "install" | "installAndRuntime"
    Name = A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.
    Publisher = A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.
    MinVersion = A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".
    MaxMajorVersionTested? = Unsigned short.
    uap6:Optional? = Boolean.
></uap17:PackageDependency>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Type | If set to "install" the package dependency is only required at install time. If set to "installAndRuntime" the package dependency is required for both install and runtime. | One of the following values: "install" , "installAndRuntime"| No |
| Name | The name as it appears in the *Name* attribute of the [Identity](element-identity.md) element of the dependency package. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.| Yes |
| Publisher | The publisher as it appears in the *Publisher* attribute of the [Identity](element-identity.md)  element of the dependency package. | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.| Yes |
| MinVersion | The minimum version of the dependency package. | A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".| Yes |
| MaxMajorVersionTested | The maximum version of the dependency package tested against. Used to determine whether frameworks will be staged side-by-side, and what framework gets loaded into the package graph for the package. | An optional number with a value between 0 and 512 characters in length. | Unsigned short.| No |
| uap6:Optional | Indicates that a framework package dependency is optional for the app, meaning the app can be installed even if the optional framework dependencies are not installed. | Boolean.| No |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| uap17 | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| uap6 | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |