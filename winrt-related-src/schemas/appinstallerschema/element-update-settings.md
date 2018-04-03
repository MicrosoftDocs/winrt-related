---
author: laurenhughes
ms.author: lahugh
title: UpdateSettings
description: An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. 
ms.topic: reference
ms.date: 4/2/2018
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
    <!-- Child elements -->
    OnLaunch?
</UpdateSettings>
```

### Key
`?` optional (zero or one)


## Attributes and Elements

### Attributes
None.

### Child Elements

<Include links to child elements>

| Child Elements | Description |
|----------------|-------------|
| [OnLaunch](element-onlaunch.md) |  OnLaunch signifies that the deployment service will check for an update to the appinstaller file on the app launch. |

### Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [AppInstaller](element-appinstaller.md) | The root element of the appinstaller document. |

## Remarks
**UpdateSettings** is an optional element. 

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
            <td> http://schemas.microsoft.com/appx/appinstaller/2017/2  </td>
        </tr>
    </tbody>
</table>