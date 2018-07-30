---
Description: Describes the visual aspects of the app.
Search.Product: eADQiWindows 10XVcnh
title: uap3:VisualElements (Windows 10)
ms.assetid: f98fc3ac-5d51-4dfb-b7a0-1985b4e568af
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:VisualElements (Windows 10)


Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd><b>&lt;uap3:VisualElements&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<uap3:VisualElements DisplayName       = A string between 1 and 256 characters 
                                         in length. This string is localizable. 
                     Description       = A string between 1 and 2048 characters 
                                         in length that cannot include 
                                         characters such as tabs, carriage 
                                         returns, and line feeds.
                     BackgroundColor   = A three-byte hexadecimal number 
                                         preceded by "#" or a named color. See 
                                         Remarks for a list of named colors.
                     Square150x150Logo = A string between 1 and 256 characters 
                                         in length that ends with ".jpg", ".png", 
                                         or ".jpeg" that can't contain these 
                                         characters: <, >, :, ", |, ?, or *. In 
                                         this string, the / and \ characters can't 
                                         be the first or last characters. Also, the 
                                         string can contain / or \ but not both.
                     Square44x44Logo   = A string between 1 and 256 characters in 
                                         length that ends with ".jpg", ".png", or 
                                         ".jpeg" that can't contain these 
                                         characters: <, >, :, ", |, ?, or *. In this 
                                         string, the / and \ characters can't be the 
                                         first or last characters. Also, the string 
                                         can contain / or \ but not both.
                     AppListEntry?     = "default" | "none" 
                     VisualGroup       = A string between 1 and 256 characters in 
                                         length that does not contain one or more 
                                         backslashes ().>

  <!-- Child elements -->
  ( uap:DefaultTile?
  & uap:LockScreen?
  & uap:SplashScreen?
  & uap:InitialRotationPreference?
  )

</uap3:VisualElements>
```

**Key**

          ? optional (zero or one)

          & interleave connector (may occur in any order)

## Attributes and Elements


**Attributes**

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AppListEntry</strong></td>
<td>The entry in the All Apps List.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>default</li>
<li>none</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BackgroundColor</strong></td>
<td>Specifies the background color of the app tile. See the Remarks section for color names. Note that the background color specified here also applies to these items:
<ul>
<li>The button color in any app-owned dialog boxes</li>
<li>The App Description page in the Store</li>
</ul></td>
<td>A three-byte hexadecimal number preceded by &quot;#&quot; or a named color. See Remarks for a list of named colors.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td>The description of the app. This string is localizable; see Remarks for details.</td>
<td>A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>DisplayName</strong></td>
<td>A friendly name for the app that can be displayed to users. This string is localizable; see Remarks for details.
<p>There are two explicitly reserved words that may not be used as the DisplayName for apps uploaded to the Store: &quot;NoUIEntryPoints&quot; and &quot;NoUIEntryPoints-DesignMode&quot;. These identifiers are reserved for use by development tools and test suites.</p>
.</td>
<td>A string between 1 and 256 characters in length. This string is localizable</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Square150x150Logo</strong></td>
<td>An image used as the app's Start Screen medium tile, and on the Task Switcher. For more info about how to specify the image in this attribute, see Remarks.</td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Square44x44Logo</strong></td>
<td>An image used as the app's Start Screen small tile, and on the All Apps List. For more info about how to specify the image in this attribute, see Remarks..</td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>VisualGroup</strong></td>
<td>The name of a folder to create on the All Apps List, in which the tile for the app should be stored.</td>
<td>A string between 1 and 256 characters in length that does not contain one or more backslashes ().</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

**Child Elements**

| Child Element                                                                  | Description                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**uap:DefaultTile**](element-uap-defaulttile.md)                             | Defines the default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default. |
| [**uap:LockScreen**](element-uap-lockscreen.md)                               | Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.                                                                                                                                   |
| [**uap:SplashScreen**](element-uap-splashscreen.md)                           | Defines the appearance of the splash screen, which is displayed by the app during launch.                                                                                                                                                                  |
| [**uap:InitialRotationPreference**](element-uap-initialrotationpreference.md) | Describes the orientations in which the app would prefer to be shown for the best user experience.                                                                                                                                                         |

 

**Parent Elements**

| Parent Element                             | Description                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------|
| [**Application**](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

 

## Remarks


You cannot use the **VisualGroup** attribute to create a structure of nested folders. If you include a backslash (\) in the value, an error occurs.

The **VisualGroup** attribute is not valid if the manifest declares only one app.

For more info on tile dimension requirements, see [Tile sizes](https://msdn.microsoft.com/library/windows/apps/hh781198).

For the **Square150x150Logo** and **Square44x44Logo** images, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **DisplayName** and **Description** attributes. For more info, see the [Globalization](https://msdn.microsoft.com/library/windows/apps/hh831183) and [Localizing the package manifest]( https://go.microsoft.com/fwlink/p/?LinkId=823054) topics.

Applications/Application/Extensions/Extension/FileTypeAssociation/Logo Applications/Application/Extensions/Extension/Protocol/Logo

Size requirements of two types of logo images are shown here:

Image attribute
Scale
Image size in pixels
Applications/Application/VisualElements/@Square150x150Logo
100
150x150
250
375x375
Applications/Application/VisualElements/@Square44x44Logo
100
44x44
250
110x110
Applications/Application/VisualElements/@Tall150x310Logo
100
150x310
250
375x775
 

These are the supported background color names:

|                      |                |                 |                   |                 |                 |
|----------------------|----------------|-----------------|-------------------|-----------------|-----------------|
| aliceBlue            | antiqueWhite   | aqua            | aquamarine        | azure           | beige           |
| bisque               | black          | blanchedAlmond  | blue              | blueViolet      | brown           |
| burlyWood            | cadetBlue      | chartreuse      | chocolate         | coral           | cornflowerBlue  |
| cornsilk             | crimson        | cyan            | darkBlue          | darkCyan        | darkGoldenrod   |
| darkGray             | darkGreen      | darkKhaki       | darkMagenta       | darkOliveGreen  | darkOrange      |
| darkOrchid           | darkRed        | darkSalmon      | darkSeaGreen      | darkSlateBlue   | darkSlateGray   |
| darkTurquoise        | darkViolet     | deepPink        | deepSkyBlue       | dimGray         | dodgerBlue      |
| firebrick            | floralWhite    | forestGreen     | fuchsia           | gainsboro       | ghostWhite      |
| gold                 | goldenrod      | gray            | green             | greenYellow     | honeydew        |
| hotPink              | indianRed      | indigo          | ivory             | khaki           | lavender        |
| lavenderBlush        | lawnGreen      | lemonChiffon    | lightBlue         | lightCoral      | lightCyan       |
| lightGoldenrodYellow | lightGreen     | lightGray       | lightPink         | lightSalmon     | lightSeaGreen   |
| lightSkyBlue         | lightSlateGray | lightSteelBlue  | lightYellow       | lime            | limeGreen       |
| linen                | magenta        | maroon          | mediumAquamarine  | mediumBlue      | mediumOrchid    |
| mediumPurple         | mediumSeaGreen | mediumSlateBlue | mediumSpringGreen | mediumTurquoise | mediumVioletRed |
| midnightBlue         | mintCream      | mistyRose       | moccasin          | navajoWhite     | navy            |
| oldLace              | olive          | oliveDrab       | orange            | orangeRed       | orchid          |
| paleGoldenrod        | paleGreen      | paleTurquoise   | paleVioletRed     | papayaWhip      | peachPuff       |
| peru                 | pink           | plum            | powderBlue        | purple          | red             |
| rosyBrown            | royalBlue      | saddleBrown     | salmon            | sandyBrown      | seaGreen        |
| seaShell             | sienna         | silver          | skyBlue           | slateBlue       | slateGray       |
| snow                 | springGreen    | steelBlue       | tan               | teal            | thistle         |
| tomato               | transparent    | turquoise       | violet            | wheat           | white           |
| whiteSmoke           | yellow         | yellowGreen     |                   |                 |                 |

 

## Examples


The following example creates a folder named App1 in the All Apps List and stores the tile for App1 in that folder.

```XML
<Package ...
         xmlns:desktop="http://schemas.microsoft.com/appx/manifest/desktop/windows10"  
         IgnorableNamespaces="... desktop">
    <Applications>
        <Application>
            <uap3:VisualElements DisplayName="App1" 
                                 Square150x150Logo="images/150x150.png" 
                                 Square44x44Logo="images/44x44.png" 
                                 Description="App1" 
                                 BackgroundColor="#777777" 
                                 AppListEntry="default" 
                                 VisualGroup="App1">  
                <uap:SplashScreen BackgroundColor="#777777" 
                                  Image="images/splash.png"/>  
           </uap3:VisualElements>  
        </Application>
        <Application>
           ...
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

## Related topics


[**Colors class**](https://msdn.microsoft.com/library/windows/apps/hh747824)

[Quickstart: Creating a default tile using the Visual Studio manifest editor](https://msdn.microsoft.com/library/windows/apps/hh465437)

 

 



