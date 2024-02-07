---
title: s4:RepairUris
description: Specifies a list of Uris pointing to App Installer files for repairing an installation. (s4:RepairUris)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:RepairUris

## Description

Specifies a list of Uris pointing to App Installer files for repairing an installation. (s4:RepairUris)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:RepairUris&gt;

## Syntax

```syntax
<s4:RepairUris>
<!-- Child elements -->
  RepairUri
</s4:RepairUris>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s4:RepairUri](element-s4-repairuri.md) | Specifies a Uri pointing to an App Installer file for repairing an installation. (s4:RepairUri) |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:AppInstaller](element-s4-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| s4 | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows version 21H2 build 22000 |
