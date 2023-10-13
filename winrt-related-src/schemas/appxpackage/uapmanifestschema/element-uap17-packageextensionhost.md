---
title: uap17:PackageExtensionHost
description: Declares an app extensibility point of type *windows.packageExtensionHost*. This element indicates which categories of extensions the package can host.
ms.date: 10/12/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# uap17:PackageExtensionHost



## Description

Declares an app extensibility point of type *windows.packageExtensionHost*. This element indicates which categories of extensions the package can host. Those category names are provided as child elements, of which at least one is required.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-uap17-extension.md">&lt;uap17:Extension&gt;</a></dt>
<dd>
<b>&lt;uap17:PackageExtensionHost&gt;</b>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap17:PackageExtensionHost>
<!-- Child elements -->
  Name{0,unbounded}
</uap17:PackageExtensionHost>
```

## Key
`{}`   specific range of occurrences




## Child Elements

| Element | Description |
| -----------| -------------|
| [Name](element-uap17-name.md) | Specifies the name of an extension category that can be hosted by a **PackageExtensionHost**.  |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| uap17 | http://schemas.microsoft.com/appx/manifest/uap/windows10/17 |
