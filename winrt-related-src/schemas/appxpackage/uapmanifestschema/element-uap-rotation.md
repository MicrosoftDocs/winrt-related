---
title: uap:Rotation
description: Specifies a single rotational orientation in which an app will display (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:VisualElements, uap:InitialRotationPreference, uap:Rotation]
---

# uap:Rotation

Specifies a single rotational orientation in which an app will display.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:VisualElements>`](element-uap-visualelements.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:InitialRotationPreference>`](element-uap-initialrotationpreference.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:Rotation>`**  

## Syntax

```xml
<uap:Rotation
  Preference = 'A required string that can have one of the following values: "portrait", "landscape", "portraitFlipped", or "landscapeFlipped".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Preference** | The specified orientation of the rotation. | A string that can have one of the following values: *portrait*, *landscape*, *portraitFlipped*, *landscapeFlipped*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:InitialRotationPreference](element-uap-initialrotationpreference.md) | Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

> [!NOTE]
> On devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.
>
> These orientation preference choices apply to both the [splash screen](../appxmanifestschema2013/element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [AutoRotationPreferences](/uwp/api/Windows.Graphics.Display.DisplayInformation) property.


To specify more than one preferred orientation, include multiple **uap:Rotation** elements in your [uap:InitialRotationPreference](element-uap-initialrotationpreference.md) element.

## Examples

<!-- Author content goes here -->
