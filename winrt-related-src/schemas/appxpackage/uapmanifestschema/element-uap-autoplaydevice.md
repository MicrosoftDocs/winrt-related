---
description: Declares an app extensibility point of type windows.autoPlayDevice (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:AutoPlayDevice (Windows 10)
ms.assetid: ae471158-7ec0-4f6c-b681-76323317ac0d
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:AutoPlayDevice (Windows 10)

Declares an app extensibility point of type **windows.autoPlayDevice**. The app provides the specified AutoPlay device actions.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:AutoPlayDevice\>**

## Syntax

```xml
<uap:AutoPlayDevice>

  <!-- Child elements -->
  uap:LaunchAction{1,1000}

</uap:AutoPlayDevice>
```

### Key

`{}`  specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:LaunchAction (in type: CT_AutoPlayDevice)](element-1-uap-launchaction.md) | Describes an AutoPlay device action. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
