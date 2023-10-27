---
description: Defines the appearance of the splash screen, which is displayed by the app during launch (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:SplashScreen (Windows 10)
ms.assetid: 1a55627f-7014-4c8c-8ec8-957ac99457db
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:SplashScreen (Windows 10)

Defines the appearance of the splash screen, which is displayed by the app during launch.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:SplashScreen\>**

## Syntax

```xml
<uap:SplashScreen
    BackgroundColor = 'An optional three-byte hexadecimal number preceded by "#" or a named color. See the [Remarks](#remarks) for a list of named colors.'
    Image = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.' 
    uap5:Optional = 'An optional boolean value.' />
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **BackgroundColor** | Specifies the background color of the splash screen. See the [Remarks](#remarks) section for a list of color names. | An optional three-byte hexadecimal number preceded by "#" or a named color. See the [Remarks](#remarks) for a list of named colors. | No |  |
| **Image** | The path to the splash screen image. See the [Remarks](#remarks) section for size requirements. | A string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |
| **uap5:Optional** | Specifies whether an app should be launched without a splash screen. If true, the splash screen will not be shown if the app can launch fast enough. If there is a delay in the app launch time, the splash screen will be shown. If false, the splash screen will always be shown. | An optional boolean value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |

## Remarks

The splash screen image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

Size requirements of a splash screen image are shown here:

- Image attributes
- Scale
- Image size in pixels
- Applications/Application/VisualElements/SplashScreen/@Image
- 100
- 620x300
- 140
- 868x420
- 180
- 1116x540

The following are supported background color names:

:::row:::
    :::column:::
        aliceBlue  
        antiqueWhite  
        aqua  
        aquamarine  
        azure  
        beige  
        bisque  
        black  
        blanchedAlmond  
        blue  
        blueViolet  
        brown  
        burlyWood  
        cadetBlue  
        chartreuse  
        chocolate  
        coral  
        cornflowerBlue  
        cornsilk  
        crimson  
        cyan  
        darkBlue  
        darkCyan  
        darkGoldenrod  
    :::column-end:::
    :::column:::
        darkGray  
        darkGreen  
        darkKhaki  
        darkMagenta  
        darkOliveGreen  
        darkOrange  
        darkOrchid  
        darkRed  
        darkSalmon  
        darkSeaGreen  
        darkSlateBlue  
        darkSlateGray  
        darkTurquoise  
        darkViolet  
        deepPink  
        deepSkyBlue  
        dimGray  
        dodgerBlue  
        firebrick  
        floralWhite  
        forestGreen  
        fuchsia  
        gainsboro  
        ghostWhite  
    :::column-end:::
    :::column:::
        gold  
        goldenrod  
        gray  
        green  
        greenYellow  
        honeydew  
        hotPink  
        indianRed  
        indigo  
        ivory  
        khaki  
        lavender  
        lavenderBlush  
        lawnGreen  
        lemonChiffon  
        lightBlue  
        lightCoral  
        lightCyan  
        lightGoldenrodYellow  
        lightGray  
        lightGreen  
        lightPink  
        lightSalmon  
        lightSeaGreen  
    :::column-end:::
    :::column:::
        lightSkyBlue  
        lightSlateGray  
        lightSteelBlue  
        lightYellow  
        lime  
        limeGreen  
        linen  
        magenta  
        maroon  
        mediumAquamarine  
        mediumBlue  
        mediumOrchid  
        mediumPurple  
        mediumSeaGreen  
        mediumSlateBlue  
        mediumSpringGreen  
        mediumTurquoise  
        mediumVioletRed  
        midnightBlue  
        mintCream  
        mistyRose  
        moccasin  
        navajoWhite  
    :::column-end:::
    :::column:::
        navy  
        oldLace  
        olive  
        oliveDrab  
        orange  
        orangeRed  
        orchid  
        paleGoldenrod  
        paleGreen  
        paleTurquoise  
        paleVioletRed  
        papayaWhip  
        peachPuff  
        peru  
        pink  
        plum  
        powderBlue  
        purple  
        red  
        rosyBrown  
        royalBlue  
        saddleBrown  
        salmon  
    :::column-end:::
    :::column:::
        sandyBrown  
        seaGreen  
        seaShell  
        sienna  
        silver  
        skyBlue  
        slateBlue  
        slateGray  
        snow  
        springGreen  
        steelBlue  
        tan  
        teal  
        thistle  
        tomato  
        transparent  
        turquoise  
        violet  
        wheat  
        white  
        whiteSmoke  
        yellow  
        yellowGreen  
    :::column-end:::
:::row-end:::

## See also

[Colors class](/uwp/api/Windows.UI.Colors)

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **uap5** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
