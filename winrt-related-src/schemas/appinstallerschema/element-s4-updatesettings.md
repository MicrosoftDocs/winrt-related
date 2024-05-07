---
title: s4:UpdateSettings
description: Specifies settings related to app updates. (s4:UpdateSettings)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:UpdateSettings

## Description

Specifies settings related to app updates. (s4:UpdateSettings)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:UpdateSettings&gt;

## Syntax
```syntax
<s4:UpdateSettings>
<!-- Child elements -->
  OnLaunch?
  AutomaticBackgroundTask?
  ForceUpdateFromAnyVersion?
</s4:UpdateSettings>
```

## Key

`?`    optional (zero or one) 

## Child Elements

| Element | Description |
| -----------| -------------|
| [s4:OnLaunch](element-s4-onlaunch.md) | Specifies whether the deployment service will check for an update to the App Installer file on the app launch. |
| [s4:AutomaticBackgroundTask](element-s4-automaticbackgroundtask.md) | An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. |
| [s4:ForceUpdateFromAnyVersion](element-s4-forceupdatefromanyversion.md) | An optional element of the App Installer file that specifies if an app can be updated from any version. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:AppInstaller](element-s4-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |