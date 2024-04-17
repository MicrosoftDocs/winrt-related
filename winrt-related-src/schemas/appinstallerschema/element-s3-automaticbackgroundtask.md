---
title: s3:AutomaticBackgroundTask
description: An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. (s3:AutomaticBackgroundTask)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:AutomaticBackgroundTask



## Description

An optional element of the App Installer file, the presence of which indicates that the system should check for updates in the background. (s3:AutomaticBackgroundTask)

The check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI. Available in Windows 10, version 1803 and later. 

## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s3:UpdateSettings](element-s3-updatesettings.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s3:AutomaticBackgroundTask&gt;

## Syntax

```syntax
<s3:AutomaticBackgroundTask></s3:AutomaticBackgroundTask>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:UpdateSettings](element-s3-updatesettings.md) | Specifies settings related to app updates. |

## Examples

In this example, deployment will check for updates in the background, every 8 hours, even if the user doesn't launch the app.

``` xml  
<s3:UpdateSettings>
    <s3:AutomaticBackgroundTask/>
</s3:UpdateSettings>
```

In this example, deployment will check for updates at launch time and in the background. In addition, the app version can be incremented or decremented.

``` xml  
<s3:UpdateSettings>
    <s3:OnLaunch HoursBetweenUpdateChecks="12"/>
    <s3:AutomaticBackgroundTask/>
    <s3:ForceUpdateFromAnyVersion>true</ForceUpdateFromAnyVersion>
</s3:UpdateSettings>
```


## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s3=http://schemas.microsoft.com/appx/appinstaller/2018` | Windows version 1809 build 17763 |
| Minimum OS version | Windows version 1809 build 17763 |
