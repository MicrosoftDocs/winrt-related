---


title: AutomaticBackgroundTask
description: An optional element of the appinstaller file. Checks for updates in the background. 
ms.topic: reference
ms.date: 02/07/2019


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# AutomaticBackgroundTask

An optional element of the appinstaller file that checks for updates in the background. A check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI. Available in Windows 10, version 1803 and later.

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt><a href="element-update-settings.md">&lt;UpdateSettings&gt;</a></dt>
            <dd><b>&lt;AutomaticBackgroundTask&gt;</b></dd>
    </dl>
</dd>
</dl>

## Syntax
``` xml 
<AutomaticBackgroundTask/>
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
**AutomaticBackgroundTask** is an optional element. 

## Examples

In this example, deployment will check for updates in the background, every 8 hours, even if the user doesn't launch the app.

``` xml  
<UpdateSettings>
    <AutomaticBackgroundTask/>
</UpdateSettings>
```

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
            <td> http://schemas.microsoft.com/appx/appinstaller/2017/2  </td>
        </tr>
    </tbody>
</table>
