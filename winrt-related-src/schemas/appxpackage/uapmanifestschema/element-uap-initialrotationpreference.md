---
title: uap:InitialRotationPreference
description: Describes the orientations in which the app would prefer to be shown for the best user experience (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:VisualElements, uap:InitialRotationPreference]
---

# uap:InitialRotationPreference

Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.

Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.

These orientation preference choices apply to both the [splash screen](../appxmanifestschema2013/element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [AutoRotationPreferences](/uwp/api/Windows.Graphics.Display.DisplayInformation) property.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:VisualElements>`](element-uap-visualelements.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:InitialRotationPreference>`**  

## Syntax

```xml
<uap:InitialRotationPreference>

  <!-- Child elements -->
  uap:Rotation{1,4}

</uap:InitialRotationPreference>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:Rotation](element-uap-rotation.md) | Specifies a single rotational orientation in which an app will display. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
