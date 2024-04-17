---
title: OnLaunch
description: This element signifies that the deployment service will check for an update to the appinstaller file on the app launch.
ms.topic: reference
ms.date: 01/22/2020
keywords: windows 10, uwp, app installer, AppInstaller, sideload
---

# OnLaunch

This element signifies that the deployment service will check for an update to the App Installer file when the app launches.

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt><a href="element-update-settings.md">&lt;UpdateSettings&gt;</a></dt>
            <dd><b>&lt;OnLaunch&gt;</b></dd>
    </dl>
</dd>
</dl>

## Syntax
``` xml 
<OnLaunch s4:HoursBetweenUpdateChecks? = String with numeric values between 0 and 255 inclusive.
    s4:ShowPrompt? = Boolean
    s4:UpdateBlocksActivation? = Boolean />
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| s4:HoursBetweenUpdateChecks | HoursBetweenUpdateChecks specifies the frequency with which the the deployment service will check for an update to the App Installer file. When HoursBetweenUpdateChecks is set to 0, the deployment service will check for updates every time the application is launched. For other values, the deployment service will check for updates when the application is launched only if it hasn't previously checked within the last number of hours specified by HoursBetweenUpdateChecks. For example, if HoursBetweenUpdateChecks is set to 12, the deployments service will check for updates when the application is launched only if it hasn't already checked for updates in the previous 12 hours. | Numeric values between 0 and 255 inclusive. The default is 24. | No |
| s4:ShowPrompt | Indicates if deployment will show a prompt, informing the user about the update. For more information about the behavior of this attribute, see the remarks. Available in Windows 10, version 1903 and later.  |Boolean | No |
| s4:UpdateBlocksActivation| Should only be used if ShowPrompt="true". Indicates if deployment will stop the user from launching the application until the update has been applied. “UpdateBlocksActivation” = true means the UI the user will see allows the user to take the update or close the app. “UpdateBlocksActivation” = false means the UI the user will see allows the user to take the update or start the app without updating. In the latter case, the update will be applied silently at an opportune time. For more information about the behavior of this attribute, see the remarks. Available in Windows 10, version 1903 and later. | Boolean | No |

### Parent Elements

| Parent Elements | Description |
|----------------|-------------|
| [UpdateSettings](element-update-settings.md) | An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. |

## Remarks

Setting the `ShowPrompt="true"` attribute currently shows a prompt for UWP applications but not for desktop applications that have been packaged in a Windows app package (that is, desktop applications that use the Desktop Bridge). For desktop applications, this functionality provides a silent update; the same default functionality provided by the OnLaunch element.

The `ShowPrompt` and `UpdateBlocksActivation` attributes have effect only when the user starts the app from a menu item or tile in the Start menu. These attributes have no effect if the user starts the app from a desktop shortcut or from the Taskbar.

## Examples

In this example, deployment will check for updates every time the app is launched. If updates are found, deployment will show a prompt telling the user they must take the update before launching the app. Also the app version can be incremented or decremented.

``` xml  
<UpdateSettings> 
    <OnLaunch s4:HoursBetweenUpdateChecks="0" s4:ShowPrompt="true" s4:UpdateBlocksActivation="true"/>
    <s4:ForceUpdateFromAnyVersion>true</s4:ForceUpdateFromAnyVersion>
</UpdateSettings>
```

## Requirements 

| Requirement | Description |
|----------------|-------------|
| `xmlns=http://schemas.microsoft.com/appx/appinstaller/2017` | This namespace is required for features introduced in Windows 10, version 1709. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows 10, version 1709 |
