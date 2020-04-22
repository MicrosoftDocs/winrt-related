---
Description: A relative path used specify where to load content from an app package.
title: uap6:LoaderSearchPathEntry


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/10/2018
---

# uap6:LoaderSearchPathEntry
A path in the app package, relative to the app package root path, to be included in the loader search path for the app's processes.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap6-loadersearchpathoverride.md">&lt;uap6:LoaderSearchPathOverride&gt;</a></dt>
<dd><b>&lt;uap6:LoaderSearchPathEntry&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap6:LoaderSearchPathEntry FolderPath = A path relative to the package root. Paths cannot contain a leading or trailing slash or backslash. This value can also be an empty string. />
```

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| FolderPath | A relative path used specify where to load content from an app package. | A path relative to the package root. Paths cannot contain a leading or trailing slash or backslash. This value can also be an empty string. | Yes |

### Child Elements
None.

## Remarks 
Note that a **LoaderSearchPathEntry** can contain an empty **FolderPath**, which has a different behavior than omitting the **LoaderSearchPathEntry**. If the **LoaderSearchPathEntry** is omitted, the default path is the app package root path. Duplicate paths are not permitted.

Main app packages, related set package, optional packages, and framework packages can all declare a **LoaderSearchPathEntry**.

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |


 

 



