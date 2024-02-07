---
title: s3:UpdateSettings
description: Specifies settings related to app updates. (s3:UpdateSettings)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:UpdateSettings

## Description

Specifies settings related to app updates. (s3:UpdateSettings)

## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s3:UpdateSettings&gt;

## Syntax
```syntax
<s3:UpdateSettings>
<!-- Child elements -->
  OnLaunch
  AutomaticBackgroundTask
  ForceUpdateFromAnyVersion
</s3:UpdateSettings>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s3:OnLaunch](element-s3-onlaunch.md) | Specifies whether the deployment service will check for an update to the App Installer file on the app launch. |
| [s3:AutomaticBackgroundTask](element-s3-automaticbackgroundtask.md) | An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. |
| [s3:ForceUpdateFromAnyVersion](element-s3-forceupdatefromanyversion.md) | An optional element of the App Installer file that specifies if an app can be updated from any version. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:AppInstaller](element-s3-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s3) | `http://schemas.microsoft.com/appx/appinstaller/2018` |
| Minimum OS version | Windows version 1809 build 17763 |
