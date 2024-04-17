---
title: s4:ForceUpdateFromAnyVersion
description: An optional element of the App Installer file that specifies if an app can be updated from any version. (s4:ForceUpdateFromAnyVersion)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:ForceUpdateFromAnyVersion

## Description

An optional element of the App Installer file that specifies if an app can be updated from any version. (s4:ForceUpdateFromAnyVersion)

If the value is true, then the app can be updated to a higher or lower version number. The default value, false, indicates that the app can only be updated to a higher version.

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:UpdateSettings](element-s4-updatesettings.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:ForceUpdateFromAnyVersion&gt;


## Syntax

```syntax
<s4:ForceUpdateFromAnyVersion>Boolean.
</s4:ForceUpdateFromAnyVersion>
```

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:UpdateSettings](element-s4-updatesettings.md) |Specifies settings related to app updates. |

## Examples

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
| Namespace (s4) | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows version 21H2 build 22000 |
