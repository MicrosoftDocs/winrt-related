---
title: s3:ForceUpdateFromAnyVersion
description: An optional element of the App Installer file that specifies if an app can be updated from any version. (s3:ForceUpdateFromAnyVersion)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:ForceUpdateFromAnyVersion

## Description

An optional element of the App Installer file that specifies if an app can be updated from any version. (s3:ForceUpdateFromAnyVersion)


## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s3:UpdateSettings](element-s3-updatesettings.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s3:ForceUpdateFromAnyVersion&gt;

## Syntax

```syntax
<s3:ForceUpdateFromAnyVersion>Boolean.
</s3:ForceUpdateFromAnyVersion>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:UpdateSettings](element-s3-updatesettings.md) |Specifies settings related to app updates. |


## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s3) | `http://schemas.microsoft.com/appx/appinstaller/2018` |
| Minimum OS version | Windows version 1809 build 17763 |
