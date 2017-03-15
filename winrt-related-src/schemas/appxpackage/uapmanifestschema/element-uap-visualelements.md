---
Description: uap:VisualElements (Windows 10)
MS-HAID: UapManifestSchema.element\_uap\_VisualElements
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: uap:VisualElements (Windows 10)
ms.assetid: da587049-bbc3-4e42-b6b9-743be20fc9e2
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# uap:VisualElements (Windows 10)


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
<dd><b>&lt;uap:VisualElements&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<VisualElements DisplayName       = A string between 1 and 256 characters in length. This string is localizable. 
                    Description       = A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.
                    BackgroundColor   = A three-byte hexadecimal number preceded by "#" or a named color. See Remarks for a list of named colors.
                    Square150x150Logo = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                    Square44x44Logo   = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                    AppListEntry?     = "default" | "none" >

  <!-- Child elements -->
  ( uap:DefaultTile?
  & uap:LockScreen?
  & uap:SplashScreen?
  & uap:InitialRotationPreference?
  )

</uap:VisualElements>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and Elements


### Attributes

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
<td><p>The entry in the All Apps List.</p></td>
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
<td><p>Specifies the background color of the app tile. See the Remarks section for color names. Note that the background color specified here also applies to these items:</p>
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
<td><p>The description of the app. This string is localizable; see Remarks for details.</p></td>
<td>A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>DisplayName</strong></td>
<td><p>A friendly name for the app that can be displayed to users. This string is localizable; see Remarks for details.</p>
<p>There are two explicitly reserved words that may not be used as the DisplayName for apps uploaded to the Store: &quot;NoUIEntryPoints&quot; and &quot;NoUIEntryPoints-DesignMode&quot;. These identifiers are reserved for use by development tools and test suites.</p></td>
<td>A string between 1 and 256 characters in length. This string is localizable.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Square150x150Logo</strong></td>
<td><p>An image used as the app's Start Screen medium tile, and on the Task Switcher. For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Square44x44Logo</strong></td>
<td><p>An image used as the app's Start Screen small tile, and on the All Apps List. For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[uap:DefaultTile](element-uap-defaulttile.md)</td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="even">
<td>[uap:InitialRotationPreference](element-uap-initialrotationpreference.md)</td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](https://msdn.microsoft.com/library/windows/apps/dn391687) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](https://msdn.microsoft.com/library/windows/apps/dn264259) property.</p></td>
</tr>
<tr class="odd">
<td>[uap:LockScreen](element-uap-lockscreen.md)</td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="even">
<td>[uap:SplashScreen](element-uap-splashscreen.md)</td>
<td><p>Defines the appearance of the splash screen, which is displayed by the app during launch.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Application](element-application.md)</td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For more info on tile dimension requirements, see [Tile sizes](https://msdn.microsoft.com/library/windows/apps/hh781198).

For the **Square150x150Logo** and **Square44x44Logo** images, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **DisplayName** and **Description** attributes. For more info, see the [Globalization](https://msdn.microsoft.com/library/windows/apps/hh831183) topic.

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

The following example is taken from the package manifest of an SDK sample.

```XML
                   
<Applications>
    <Application Id="App" StartPage="default.html">
        <uap:VisualElements 
            DisplayName="ApplicationDataSample"
            Description="Application data sample"
            BackgroundColor="#FFFFFF"               
            Square150x150Logo="images\squareTile-sdk.png" 
            Square44x44Logo="images\smallTile-sdk.png" 
            AppListEntry="default">
            <uap:DefaultTile ShowName="allLogos" />
            <uap:LockScreen Notification="badge" BadgeLogo="images\badgeLogo.png" />
            <uap:SplashScreen BackgroundColor="white" Image="images\splash-sdk.png" />
            <uap:InitialRotationPreference> 
                <uap:Rotation Preference="portrait" />
            </uap:InitialRotationPreference>            
        </uap:VisualElements>
    </Application>
</Applications>                             
```

## See also


[App screenshots and images](https://docs.microsoft.com/en-us/windows/uwp/publish/app-screenshots-and-images)

[**Colors class**](https://msdn.microsoft.com/library/windows/apps/hh747824)

[Quickstart: Creating a default tile using the Visual Studio manifest editor](https://msdn.microsoft.com/library/windows/apps/hh465437)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



