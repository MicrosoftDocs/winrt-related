---
title: s4:AutomaticBackgroundTask
description: An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. (s4:AutomaticBackgroundTask)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:AutomaticBackgroundTask

## Description

An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. (s4:AutomaticBackgroundTask)

The check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI. Available in Windows 10, version 1803 and later. 

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:UpdateSettings](element-s4-updatesettings.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:AutomaticBackgroundTask&gt;

## Syntax

```syntax
<s4:AutomaticBackgroundTask></s4:AutomaticBackgroundTask>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:UpdateSettings](element-s4-updatesettings.md) | Specifies settings related to app updates. |

## Examples

In this example, deployment will check for updates in the background, every 8 hours, even if the user doesn't launch the app.

``` xml  
<s4:UpdateSettings>
    <s4:AutomaticBackgroundTask/>
</s4:UpdateSettings>
```

In this example, deployment will check for updates at launch time and in the background. In addition, the app version can be incremented or decremented.

``` xml  
<s4:UpdateSettings>
    <s4:OnLaunch HoursBetweenUpdateChecks="12"/>
    <s4:AutomaticBackgroundTask/>
    <s4:ForceUpdateFromAnyVersion>true</ForceUpdateFromAnyVersion>
</s4:UpdateSettings>
```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
