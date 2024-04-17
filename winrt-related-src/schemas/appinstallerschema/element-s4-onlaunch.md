---
title: s4:OnLaunch
description: Specifies whether the deployment service will check for an update to the App Installer file on the app launch. (s4:OnLaunch)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:OnLaunch

## Description

Specifies whether the deployment service will check for an update to the App Installer file on the app launch. (s4:OnLaunch)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; [s4:UpdateSettings](element-s4-updatesettings.md);

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &lt;s4:OnLaunch&gt;

## Syntax

```syntax
<s4:OnLaunch     ShowPrompt? = Boolean.
    UpdateBlocksActivation? = Boolean.
    HoursBetweenUpdateChecks? = Unsigned byte.
></s4:OnLaunch>
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
| [s4:UpdateSettings](element-s4-updatesettings.md) | Specifies settings related to app updates. |


## Remarks

Setting the `ShowPrompt="true"` attribute currently shows a prompt for UWP applications but not for desktop applications that have been packaged in a Windows app package (that is, desktop applications that use the Desktop Bridge). For desktop applications, this functionality provides a silent update; the same default functionality provided by the OnLaunch element.

The `ShowPrompt` and `UpdateBlocksActivation` attributes have effect only when the user starts the app from a menu item or tile in the Start menu. These attributes have no effect if the user starts the app from a desktop shortcut or from the Taskbar.

## Examples

In this example, deployment will check for updates every time the app is launched. If updates are found, deployment will show a prompt telling the user they must take the update before launching the app. Also the app version can be incremented or decremented.

``` xml  
<s4:UpdateSettings> 
    <s4OnLaunch s4:HoursBetweenUpdateChecks="0" s4:ShowPrompt="true" s4:UpdateBlocksActivation="true"/>
    <s4:ForceUpdateFromAnyVersion>true</s4:ForceUpdateFromAnyVersion>
</s4UpdateSettings>
```


## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
