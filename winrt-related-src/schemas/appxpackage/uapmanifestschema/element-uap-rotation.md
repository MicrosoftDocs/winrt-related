---
description: Specifies a single rotational orientation in which an app will display (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:Rotation (Windows 10)
ms.assetid: c3e6abb0-05ac-4b38-a23e-3e0f7e610b4c
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:Rotation (Windows 10)

Specifies a single rotational orientation in which an app will display.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:InitialRotationPreference\>](element-uap-initialrotationpreference.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:Rotation\>**

## Syntax

```xml
<uap:Rotation
  Preference = 'A string that can have one of the following values: "portrait", "landscape", "portraitFlipped", or "landscapeFlipped".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Preference** | The specified orientation of the rotation. | A string that can have one of the following values: *portrait*, *landscape*, *portraitFlipped*, or *landscapeFlipped*. | Yes |  |

### Child Elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [uap:InitialRotationPreference](element-uap-initialrotationpreference.md) | Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate. |

> [!NOTE]
> On devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.
>
> These orientation preference choices apply to both the [splash screen](../appxmanifestschema2013/element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [AutoRotationPreferences](/uwp/api/Windows.Graphics.Display.DisplayInformation) property.

## Remarks

To specify more than one preferred orientation, include multiple **uap:Rotation** elements in your [uap:InitialRotationPreference](element-uap-initialrotationpreference.md) element.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
