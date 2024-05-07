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
    s4:AutomaticBackgroundTask?
    s4:ForceUpdateFromAnyVersion?
</UpdateSettings>
```

### Key
`?` optional (zero or one)


## Attributes and Elements

### Attributes

None.


### Child Elements

<!-- Include links to child elements -->

| Child Elements | Description |
|----------------|-------------|
| [OnLaunch](element-onlaunch.md) |  OnLaunch signifies that the deployment service will check for an update to the appinstaller file on the app launch. |
| [s4:AutomaticBackgroundTask](element-s4-automaticbackgroundtask.md) |Checks for updates in the background. A check is made every 8 hours independently of whether the user launched the app. This type of update cannot show UI. Available in Windows 10, version 1803 and later. |
| [s4:ForceUpdateFromAnyVersion](element-s4-forceupdatefromanyversion.md) |A boolean that allows the app's version to be incremented or decremented. Without this element, the app can only move to a higher version. Available starting in Windows 10, version 1809 and later. |

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
    <s4:AutomaticBackgroundTask/>
</UpdateSettings>
```

In this example, deployment will check for updates at launch time and in the background. In addition, the app version can be incremented or decremented.

``` xml  
<UpdateSettings>
    <OnLaunch HoursBetweenUpdateChecks="12"/>
    <s4:AutomaticBackgroundTask/>
    <s4:ForceUpdateFromAnyVersion>true</s4:ForceUpdateFromAnyVersion>
</UpdateSettings>
```


## Requirements

| Requirement | Description |
|----------------|-------------|
| `xmlns=http://schemas.microsoft.com/appx/appinstaller/2017` | This namespace is required for features introduced in Windows 10, version 1709. |
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2018` | This namespace is required for features introduced in Windows 10, version 1809. |
| Minimum OS version | Windows 10, version 1709 |

