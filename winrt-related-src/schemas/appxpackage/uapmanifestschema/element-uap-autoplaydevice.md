---
title: uap:AutoPlayDevice
description: Declares an app extensibility point of type windows.autoPlayDevice (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:AutoPlayDevice]
---

# uap:AutoPlayDevice

Declares an app extensibility point of type **windows.autoPlayDevice**. The app provides the specified AutoPlay device actions.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:AutoPlayDevice>`**  

## Syntax

```xml
<uap:AutoPlayDevice>

  <!-- Child elements -->
  uap:LaunchAction{1,1000}

</uap:AutoPlayDevice>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:LaunchAction](element-uap-autoplaydevice-launchaction.md) | Describes an AutoPlay device action. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

When a device that is not volume-based is connected to a computer, the system raises an AutoPlay device event. This extensibility point enables your app to be listed as an AutoPlay choice for one or more AutoPlay device events. Because these devices are not volume-based, the system provides the app with device information rather than a file folder.

## Examples

```xml
<uap:Extension
  Category="windows.autoPlayDevice">
  <uap:AutoPlayDevice>
    <uap:LaunchAction
      Verb="startDeviceApp"
      ActionDisplayName="Start my device app"
      DeviceEvent="CustomDeviceEvent"/>
  </uap:AutoPlayDevice>
</uap:Extension>
```

## See also
**Tasks**
[Auto-launching with AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))
