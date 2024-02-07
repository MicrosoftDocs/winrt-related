---
title: s2:OnLaunch
description: Specifies whether the deployment service will check for an update to the App Installer file on the app launch. (s2:OnLaunch)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:OnLaunch

## Description

Specifies whether the deployment service will check for an update to the App Installer file on the app launch. (s2:OnLaunch)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s2:UpdateSettings](element-s2-updatesettings.md);

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s2:OnLaunch&gt;

## Syntax

```syntax
<s2:OnLaunch     HoursBetweenUpdateChecks? = Unsigned byte.
></s2:OnLaunch>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| ShowPrompt | Indicates if deployment will show a prompt, informing the user about the update. For more information about the behavior of this attribute, see the remarks. Available in Windows 10, version 1903 and later. | Boolean.| No |
| UpdateBlocksActivation | Should only be used if ShowPrompt="true". Indicates if deployment will stop the user from launching the application until the update has been applied. “UpdateBlocksActivation” = true means the UI the user will see allows the user to take the update or close the app. “UpdateBlocksActivation” = false means the UI the user will see allows the user to take the update or start the app without updating. In the latter case, the update will be applied silently at an opportune time. For more information about the behavior of this attribute, see the remarks. Available in Windows 10, version 1903 and later. | Boolean.| No |
| HoursBetweenUpdateChecks | Specifies the frequency with which the the deployment service will check for an update to the App Installer file. When HoursBetweenUpdateChecks is set to 0, the deployment service will check for updates every time the application is launched. For other values, the deployment service will check for updates when the application is launched only if it hasn't previously checked within the last number of hours specified by HoursBetweenUpdateChecks. For example, if HoursBetweenUpdateChecks is set to 12, the deployments service will check for updates when the application is launched only if it hasn't already checked for updates in the previous 12 hours. | Numeric values between 0 and 255 inclusive. The default is 24.| No |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:UpdateSettings](element-s2-updatesettings.md) | Specifies settings related to app updates. |



| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s2) | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |
| Namespace (s4) | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows 10 version 1803 build 17134 |

