---
title: s2:AutomaticBackgroundTask
description: An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. (s2:AutomaticBackgroundTask)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:AutomaticBackgroundTask

## Description

An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. (s2:AutomaticBackgroundTask)

The check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI. Available in Windows 10, version 1803 and later. 

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s2:UpdateSettings](element-s2-updatesettings.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s2:AutomaticBackgroundTask&gt;

## Syntax

```syntax
<s2:AutomaticBackgroundTask></s2:AutomaticBackgroundTask>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:UpdateSettings](element-s2-updatesettings.md) | Specifies settings related to app updates. |


## Examples

In this example, deployment will check for updates in the background, every 8 hours, even if the user doesn't launch the app.

``` xml  
<s2:UpdateSettings>
    <s2:AutomaticBackgroundTask/>
</s2:UpdateSettings>
```

In this example, deployment will check for updates at launch time and in the background. In addition, the app version can be incremented or decremented.

``` xml  
<s2:UpdateSettings>
    <s2:OnLaunch HoursBetweenUpdateChecks="12"/>
    <s2:AutomaticBackgroundTask/>
    <s4:ForceUpdateFromAnyVersion>true</ForceUpdateFromAnyVersion>
</s2:UpdateSettings>
```



## Requirements

| Requirement | Description |
|----------------|-------------|
| `xmlns:s2=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows 10, version 1803 |
