---
description: Describes the visual aspects of the app (in uap3:VisualElements).
Search.Product: eADQiWindows 10XVcnh
title: uap3:VisualElements (Windows 10)
ms.assetid: f98fc3ac-5d51-4dfb-b7a0-1985b4e568af
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:VisualElements (Windows 10)

Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:VisualElements\>**

## Syntax

```xml
<uap3:VisualElements
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' 
    Description = 'A string between 1 and 2048 characters in length.'
    BackgroundColor = 'A three-byte hexadecimal number preceded by "#" or a named color. See Remarks for a list of named colors.'
    Square150x150Logo = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.'
    Square44x44Logo = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.'
    AppListEntry = 'An optional string that can have one of the following values: "default" or "none".' 
    VisualGroup = 'A string with a value between 1 and 256 characters in length that does not contain backslashes ("\").' />

  <!-- Child elements -->
  uap:DefaultTile?
  & uap:LockScreen?
  & uap:SplashScreen?
  & uap:InitialRotationPreference?

</uap3:VisualElements>
```

### Key

`?`  optional (zero or one)
`&`  interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | A friendly name for the app that can be displayed to users. This string is localizable; see Remarks for details. | A string with a value between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Description** | The description of the app. This string is localizable; see [Remarks](#remarks) for details. | A string between 1 and 2048 characters in length. | Yes |  |
| **BackgroundColor** | Specifies the background color of the app tile. | A three-byte hexadecimal number preceded by `#` or a named color. See [Remarks](#remarks) for a list of named colors. | Yes |  |
| **Square150x150Logo** | An image used as the app's Start Screen medium tile, and on the Task Switcher. For more info about how to specify the image in this attribute, see [Remarks](#remarks). | A string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |
| **Square44x44Logo** | An image used as the app's Start Screen small tile, and on the All Apps List. For more info about how to specify the image in this attribute, see [Remarks](#remarks). | A string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |
| **AppListEntry** | The entry in the All Apps List. | An optional string that can have one of the following values: *default* or *none*. | No |  |
| **VisualGroup** | The name of a folder to create on the All Apps List, in which the tile for the app should be stored. | A string with a value between 1 and 256 characters in length that does not contain backslashes (`\`) or spaces. | No |  |

> [!NOTE]
> The background color specified here also applies to these items:
>
>- The button color in any app-owned dialog boxes.
>- The App Description page in the Store.

### Child elements

| Child Element | Description |
|-|-|
| [uap:DefaultTile](element-uap-defaulttile.md) | Defines the default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default. |
| [uap:LockScreen](element-uap-lockscreen.md) | Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked. |
| [uap:SplashScreen](element-uap-splashscreen.md) | Defines the appearance of the splash screen, which is displayed by the app during launch. |
| [uap:InitialRotationPreference](element-uap-initialrotationpreference.md) | Describes the orientations in which the app would prefer to be shown for the best user experience. |

### Parent elements

| Parent Element | Description |
|-|-|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Remarks

You cannot use the **VisualGroup** attribute to create a structure of nested folders. If you include a backslash (`\`) in the value, an error occurs.

The **VisualGroup** attribute is not valid if the manifest declares only one app.

For more info on tile dimension requirements, see [Tile sizes](/previous-versions/windows/apps/hh781198(v=win.10)).

For the **Square150x150Logo** and **Square44x44Logo** images, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **DisplayName** and **Description** attributes. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) and [Localizing the package manifest]( https://go.microsoft.com/fwlink/p/?LinkId=823054) topics.

Size requirements of two types of logo images are shown here:

| Image attribute | Scale (Image size in pixels) |
|-|-|-|
| `Applications/Application/VisualElements/@Square150x150Logo` | 100 (150x150) |
|  | 250 (375x375) |
| `Applications/Application/VisualElements/@Square44x44Logo` | 100 (44x44) |
|  | 250 (110x110) |
| `Applications/Application/VisualElements/@Tall150x310Logo` | 100 (150x310) |
|  | 250 (375x775) |

These are the supported background color names:

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

The following example creates a folder named App1 in the All Apps List and stores the tile for App1 in that folder.

```xml
<Package
    xmlns:desktop="http://schemas.microsoft.com/appx/manifest/desktop/windows10"  
    IgnorableNamespaces="... desktop">
    <Applications>
        <Application>
            <uap3:VisualElements
                DisplayName="App1" 
                Square150x150Logo="images/150x150.png" 
                Square44x44Logo="images/44x44.png" 
                Description="App1" 
                BackgroundColor="#777777" 
                AppListEntry="default" 
                VisualGroup="App1">  
                <uap:SplashScreen
                    BackgroundColor="#777777" 
                    Image="images/splash.png"/>  
           </uap3:VisualElements>  
        </Application>
    </Applications>
</Package>
```

## Related topics

- [**Colors class**](/uwp/api/Windows.UI.Colors)
- [Quickstart: Creating a default tile using the Visual Studio manifest editor](/previous-versions/windows/apps/hh465437(v=win.10))

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
