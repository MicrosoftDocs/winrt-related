---
title: desktop:FullTrustProcess
description: Represents a desktop process that runs in full-trust.
ms.date: 05/10/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop:FullTrustProcess


## Description

Represents a desktop process that runs in full-trust.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop-extension.md">&lt;desktop:Extension&gt;</a></dt>
<dd><b>&lt;desktop:FullTrustProcess&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```sytnax
<desktop:FullTrustProcess >

 <!-- Child elements -->
 ParameterGroup{0,1000}
</desktop:FullTrustProcess>
```
### Key
`{}` specific range of occurrences

## Attributes

None

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [ParameterGroup](element-desktop-parametergroup.md) | Defines a group of command line parameters for the process. |

## Remarks

For more details, see [FullTrustProcessLauncher](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |