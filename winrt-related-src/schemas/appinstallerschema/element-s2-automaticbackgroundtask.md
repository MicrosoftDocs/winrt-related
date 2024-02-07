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


## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s2) | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |
| Minimum OS version | Windows 10 version 1803 build 17134 |
