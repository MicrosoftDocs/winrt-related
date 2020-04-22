---


title: UpdateSettings
description: An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. 
ms.topic: reference
ms.date: 06/10/2019


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# UpdateSettings

An optional element of the appinstaller file. UpdateSettings signifies whether or not to check for an update during the app's launch. 

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt><b>&lt;UpdateSettings&gt;</b></dt>
    </dl>
</dd>
</dl>

## Syntax
``` xml 
<UpdateSettings>
    <!-- Child elements -->
    OnLaunch?
    AutomaticBackgroundTask?
    ForceUpdateFromAnyVersion?
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
| [AutomaticBackgroundTask](element-automatic-background-task.md) |Checks for updates in the background. A check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI. Available in Windows 10, version 1803 and later. |
| [ForceUpdateFromAnyVersion](element-force-update-from-any-version.md) |A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version. Available starting in Windows 10, version 1809 and later. |

### Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [AppInstaller](element-appinstaller.md) | The root element of the appinstaller document. |

## Remarks
**UpdateSettings** is an optional element. 

## Examples

In this example, deployment will check for updates only at launch time and only if 12 or more hours have passed since the last time deployment checked for updates.

``` xml    
<UpdateSettings>
    <OnLaunch HoursBetweenUpdateChecks="12"/>
</UpdateSettings>
```

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

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/appinstaller/2017/2` |

