---
author: laurenhughes
ms.author: lahugh
title: OnLaunch
description: This element signifies that the deployment service will check for an update to the appinstaller file on the app launch.
ms.topic: reference
ms.date: 04/03/2017
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, app installer, AppInstaller, sideload
---

# OnLaunch

This element signifies that the deployment service will check for an update to the appinstaller file on the app launch.

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
```syntax
<OnLaunch HoursBetweenUpdateChecks? = String with numeric values between 0 and 255 inclusive. />
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| HoursBetweenUpdateChecks | HoursBetweenUpdateChecks speficies the frequency with which the the deployment service will check for an update to the appinstaller file. When HoursBetweenUpdateChecks is set to 0, the deployment service will check for updates every time the application is launched. If HoursBetweenUpdateChecks is set to 12, the deployments service will check for updates every 12 hours. The default value of HouyrsBetweenUpdateChecks is 24, meaning the deployments service will check for updates every 24 hours unless otherwise specified. | String with numeric values between 0 and 255 inclusive. | No |

### Parent Elements

| Parent Elements | Description |
|----------------|-------------|
| [UpdateSettings](element-update-settings.md) | An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. |

## Requirements
<table>
    <tbody>
        <tr>
            <td>Namespace</td>
            <td> http://schemas.microsoft.com/appx/appinstaller/2017/2 </td>
        </tr>
    </tbody>
</table>