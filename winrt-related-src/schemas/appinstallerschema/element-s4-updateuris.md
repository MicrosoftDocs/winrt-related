---
title: s4:UpdateUris
description: Specifies a list of Uris pointing to App Installer files for updating an installation. (s4:UpdateUris)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:UpdateUris



## Description

Specifies a list of Uris pointing to App Installer files for updating an installation. (Version 4)



## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:UpdateUris&gt;

## Syntax

```syntax
<s4:UpdateUris>
<!-- Child elements -->
  UpdateUri
</s4:UpdateUris>
```




## Child Elements

| Element | Description |
| -----------| -------------|
| [UpdateUri](element-s4-updateuri.md) | Specifies a Uri pointing to an App Installer file for updating an installation. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:AppInstaller](element-s4-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
