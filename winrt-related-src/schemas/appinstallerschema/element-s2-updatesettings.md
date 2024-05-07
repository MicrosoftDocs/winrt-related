---
title: s2:UpdateSettings
description: Specifies settings related to app updates. (s2:UpdateSettings)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:UpdateSettings

## Description

Specifies settings related to app updates. (s2:UpdateSettings)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:UpdateSettings&gt;

## Syntax

```syntax
<s2:UpdateSettings>
<!-- Child elements -->
  OnLaunch{0,1}
  AutomaticBackgroundTask{0,1}
  s4:ForceUpdateFromAnyVersion{0,1}
</s2:UpdateSettings>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s2:OnLaunch](element-s2-onlaunch.md) | Specifies whether the deployment service will check for an update to the App Installer file on the app launch. |
| [s2:AutomaticBackgroundTask](element-s2-automaticbackgroundtask.md) | An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. |
| [s4:ForceUpdateFromAnyVersion](element-s4-forceupdatefromanyversion.md) | An optional element of the App Installer file that specifies if an app can be updated from any version. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:AppInstaller](element-s2-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s2=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows 10 version 1803 build 17134 |

