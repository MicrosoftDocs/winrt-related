---
author: laurenhughes
ms.author: lahugh
title: UpdateSettings
description: An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. 
ms.topic: reference
ms.date: 1/4/2018
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# UpdateSettings

An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. 

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt>**UpdateSettings**</dt>
    </dl>
</dd>
</dl>

## Syntax
```syntax
<UpdateSettings>
    <OnLaunch HoursBetweenUpdateChecks="12" />
</UpdateSettings>

```


## Attributes and Elements

### Attributes
None

### Child Elements

<Include links to child elements>

| Child Elements | Description |
|----------------|-------------|
| OnLaunch       |  OnLaunch signifies that the deployment service will check for an update to the appinstaller file on the app launch.  |
| HoursBetweenUpdateChecks       |  Allows values between 0 and 255. HoursBetweenUpdateChecks speficies the frequency with which the the deployment service will check for an update to the appinstaller file. The default value of HouyrsBetweenUpdateChecks is 24, meaning the deployments service will check for updates every 24 hours unless otherwise specified. |


### Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [AppInstaller](element-appinstaller.md) | The root element of the appinstaller document. |

## Remarks
**UpdateSettings** is an optional element that may have up to two elements inside it. 
## Examples
``` xml    
    <UpdateSettings>
        <OnLaunch HoursBetweenUpdateChecks="12"/>
    </UpdateSettings>
```
## Requirements
<table>
    <tbody>
        <tr>
            <td>Namespace</td>
            <td> http://schemas.microsoft.com/appx/appinstaller/2017  </td>
        </tr>
    </tbody>
</table>