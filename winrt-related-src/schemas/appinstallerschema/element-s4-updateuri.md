---
title: s4:UpdateUri
description: Specifies a Uri pointing to an App Installer file for updating an installation. (s4:UpdateUri)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:UpdateUri



## Description

Specifies a Uri pointing to an App Installer file for updating an installation. (s4:UpdateUri)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:UpdateUris](element-s4-updateuris.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:UpdateUri&gt;

## Syntax

```syntax
<s4:UpdateUri>
    Web URI as a string between 1 and 2084 characters in length.
</s4:UpdateUri>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:UpdateUris](element-s4-updateuris.md) | Specifies a list of Uris pointing to App Installer files for updating an installation. |


## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |