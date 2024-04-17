---
title: s4:RepairUri
description: Specifies a Uri pointing to an App Installer file for repairing an installation. (s4:RepairUri)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:RepairUri



## Description

Specifies a Uri pointing to an App Installer file for repairing an installation. (s4:RepairUri)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:RepairUris](element-s4-repairuris.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:RepairUris&gt;

## Syntax
```syntax
<s4:RepairUri>Web URI as a string between 1 and 2084 characters in length.
</s4:RepairUri>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:RepairUris](element-s4-repairuris.md) | Specifies a list of Uris pointing to App Installer files for repairing an installation. |


## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
