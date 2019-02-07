---
author: mcleanbyron
ms.author: mcleans
title: ForceUpdateFromAnyVersion
description: An optional element of the appinstaller file. This element contains a boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version. 
ms.topic: reference
ms.date: 02/07/2019


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# ForceUpdateFromAnyVersion

An optional element of the appinstaller file. This element contains a boolean value that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version. Available starting in Windows 10, version 1809 and later.

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt><a href="element-update-settings.md">&lt;UpdateSettings&gt;</a></dt>
            <dd><b>&lt;ForceUpdateFromAnyVersion&gt;</b></dd>
    </dl>
</dd>
</dl>

## Syntax
``` xml 
<ForceUpdateFromAnyVersion>true</ForceUpdateFromAnyVersion>
```

## Attributes and Elements

### Attributes

None.


### Child Elements

None.

### Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [UpdateSettings](element-update-settings.md) | Signifies whether or not to check for an update during the app's launch. |

## Remarks
**ForceUpdateFromAnyVersion** is an optional element. 

## Examples

In this example, deployment will check for updates at launch time and in the background. In addition, the app version can be incremented or decremented.

``` xml  
<UpdateSettings>
    <OnLaunch HoursBetweenUpdateChecks="12"/>
    <AutomaticBackgroundTask/>
    <ForceUpdateFromAnyVersion>true</ForceUpdateFromAnyVersion>
</UpdateSettings>
```


## Requirements
<table>
    <tbody>
        <tr>
            <td>Namespace</td>
            <td> http://schemas.microsoft.com/appx/appinstaller/2018  </td>
        </tr>
    </tbody>
</table>
