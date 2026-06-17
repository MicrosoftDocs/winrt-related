---
title: uap:SplashScreen
description: Defines the appearance of the splash screen, which is displayed by the app during launch (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:VisualElements, uap:SplashScreen]
---

# uap:SplashScreen

Defines the appearance of the splash screen, which is displayed by the app during launch.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:VisualElements>`](element-uap-visualelements.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:SplashScreen>`**  

## Syntax

```xml
<uap:SplashScreen
  uap5:Optional = 'An optional boolean value.'
  BackgroundColor = 'An optional value. <!-- TODO: Add description for t:ST_Color -->'
  Image = 'A required string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **uap5:Optional** | Specifies whether an app should be launched without a splash screen. If true, the splash screen will not be shown if the app can launch fast enough. If there is a delay in the app launch time, the splash screen will be shown. If false, the splash screen will always be shown. | An optional boolean value. | No |  |
| **BackgroundColor** | Specifies the background color of the splash screen. See the [Remarks](#remarks) section for a list of color names. | An optional value. <!-- TODO: Add data type for t:ST_Color --> | No |  |
| **Image** | The path to the splash screen image. See the [Remarks](#remarks) section for size requirements. | A string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `&#124;`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **uap5** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

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

## Examples

<!-- Author content goes here -->

## See also
[Colors class](/uwp/api/Windows.UI.Colors)
