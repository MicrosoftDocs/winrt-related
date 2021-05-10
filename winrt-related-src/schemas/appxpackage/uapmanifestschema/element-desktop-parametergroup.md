---
title: desktop:ParameterGroup
description: Represents a group of command-line parameters for a full-trust process.
ms.date: 05/10/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop:ParameterGroup


## Description

Represents a group of command-line parameters for a full-trust process.

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
<dd>
<dl>
<dt><a href="element-desktop-fulltrustprocess.md">&lt;desktop:FullTrustProcess&gt;</a></dt>
<dd><b>&lt;desktop:ParameterGroup&gt;</b></dd>
</dl>
</dd>
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
<desktop:ParameterGroup  GroupId = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and 
                         end.
                         Parameters = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
```
### Key
`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| GroupId | The name for a group of one or more related command-line parameters. You can pass this group ID to the [LaunchFullTrustProcessForAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforappasync) or [LaunchFullTrustProcessForCurrentAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforcurrentappasync) method. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| Parameters | The command line parameters to associate with the **GroupId** value. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

## Child Elements

None

## Remarks

For more details, see [LaunchFullTrustProcessForAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforappasync) and [LaunchFullTrustProcessForCurrentAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforcurrentappasync).

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |