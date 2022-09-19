---
description: Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:LockScreen (Windows 10)
ms.assetid: 65e0cc4e-af42-4852-a9ca-ee09a5fee5f2
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:LockScreen (Windows 10)

Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:LockScreen\>**

## Syntax

```xml
<uap:LockScreen
  Notification = 'A string that can have one of the following values: "badge" or "badgeAndTileText".'
  BadgeLogo = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Notification** | The type of tile that can be shown for an app on the lock screen. This can either be simply a badge which displays either a number or a glyph to communicate status, or both a badge and text, which can display detailed status. If LockScreen Notification type 'badgeAndTileText' is selected, then the optional WideLogo must be specified, since only the WideLogo template provides the right information to display with tile text. If this image is not provided, the tile can only display in the square format and cannot accept notifications based on [wide template types](/previous-versions/windows/apps/hh761491(v=win.10)). This rule is semantically enforced through the manifest API. | A string that can have one of the following values: *badge* or *badgeAndTileText*. | Yes |  |
| **BadgeLogo** | A logo image that is shown next to the badge to identify the app. This image must be monochromatic, of type .png, and measure 24 x 24 pixels. For more info about how to specify the image in this attribute, see [Remarks](#remarks). | A string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |

## Remarks

For an app to have a presence on the lock screen, it must also register to handle background tasks. For more information, see the [Lock screen overview](/previous-versions/windows/apps/hh779720(v=win.10)) and the [uap:BackgroundTasks](/previous-versions/windows/dn934782(v=win.10)) element.

The **BadgeLogo** image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

Size requirements of a badge logo image are shown here:

- Image attribute
- Scale
- Image size in pixels
- Applications\\Application\\VisualElements\\LockScreen\\@BadgeLogo
- 100
- 24x24
- 140
- 33x33
- 180
- 43x43

## See also

- [Lock screen overview](/uwp/api/Windows.System.UserProfile.LockScreen)
- [How to show notifications on the lock screen](/previous-versions/windows/apps/hh700416(v=win.10))
- [Lock screen apps sample](/samples/browse/)
- [Windows.ApplicationModel.LockScreen namespace](/uwp/api/windows.applicationmodel.lockscreen)

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
