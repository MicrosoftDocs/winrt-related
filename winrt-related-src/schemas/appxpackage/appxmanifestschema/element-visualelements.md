---
description: Describes the visual aspects of the UWP app.
Search.Product: eADQiWindows 10XVcnh
title: VisualElements (Windows 8 package schema)
ms.assetid: f0db5141-8aba-4ac4-939f-4fe3debcc761


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# VisualElements (package schema for Windows 8)


Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd><b>&lt;VisualElements&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<VisualElements DisplayName     = A string between 1 and 256 characters in length.
                Logo            = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, %, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                SmallLogo       = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, %, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                Description     = A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.
                ForegroundText  = "light" | "dark"
                BackgroundColor = A three-byte hexadecimal number preceded by "#" or a named color.
                ToastCapable?   = boolean >

  <!-- Child elements -->
  ( DefaultTile?
  & LockScreen?
  & SplashScreen
  & InitialRotationPreference?
  )

</VisualElements>
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
<td><strong>BackgroundColor</strong></td>
<td><p>Specifies the background color of the app tile. See the Remarks section for color names. Note that the background color specified here also applies to these items:</p>
<ul>
<li>The button color in any app-owned dialog boxes</li>
<li>The App Description page in the Microsoft Store</li>
<li>Applies to Windows Phone: Choosing &quot;transparent&quot; causes the system accent color to be used.</li>
</ul>
</td>
<td>A three-byte hexadecimal number preceded by &quot;#&quot; or a named color.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p>The description of the app. This string is localizable; see Remarks for details.</p></td>
<td>A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>DisplayName</strong></td>
<td><p>A friendly name for the app that can be displayed to users. This string is localizable; see Remarks for details.</p>
<p>There are two explicitly reserved words that may not be used as the DisplayName for apps uploaded to the Microsoft Store: &quot;NoUIEntryPoints&quot; and &quot;NoUIEntryPoints-DesignMode&quot;. These identifiers are reserved for use by development tools and test suites.</p></td>
<td>A string between 1 and 256 characters in length.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ForegroundText</strong></td>
<td><p>Specifies the foreground color of the app tile.</p>
<ul>
<li>Applies to Windows Phone: This value is ignored. All tiles use the light text color.</li>
</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>light</li>
<li>dark</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Logo</strong></td>
<td><p>An image used as the app's square tile. For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>SmallLogo</strong></td>
<td><p>A small image shown in the corner of the tile to identify the app. For more info on how to specify the image in this attribute, see Remarks.</p>
<ul>
<li>Applies to Windows Phone: Windows Phone does not display the small logo on the tile. It is used only in the Apps list.</li>
</ul>
</td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ToastCapable</strong></td>
<td><p>A value of <strong>true</strong> indicates that the app is allowed to provide toast notifications. The default value is <strong>false</strong>. If you don't want toast notifications to appear, do not specify a value for this attribute. Note that apps should not make decisions about whether to send toast notifications based on this value.</p></td>
<td>boolean</td>
<td>No</td>
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
<td><a href="element-defaulttile.md">DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
<tr class="even">
<td><a href="element-initialrotationpreference.md">InitialRotationPreference</a> </td>
<td><p>Describes the orientations in which the app would prefer to be shown for the best user experience. On a device that can be rotated, such as a tablet, the app will not be redrawn for orientations that are not specified here. For instance, if the app specifies only Landscape and LandscapeFlipped orientations, and the device is rotated to a Portrait orientation, the app will not rotate.</p>
<p>Note that on devices that can't be rotated, an app might be shown in that device's default orientation and the app's preferred orientation will be ignored. However, on a device with a rotation lock activated, your app's preferred rotation will still be honored.</p>
<p>These orientation preference choices apply to both the [<strong>splash screen</strong>](element-splashscreen.md) and the app UI when a new session is launched for your app. The preferences can be changed during run time through the [<strong>AutoRotationPreferences</strong>](/uwp/api/Windows.Graphics.Display.DisplayProperties) property.</p></td>
</tr>
<tr class="odd">
<td><a href="element-lockscreen.md">LockScreen</a> </td>
<td><p>Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.</p></td>
</tr>
<tr class="even">
<td><a href="element-splashscreen.md">SplashScreen</a> </td>
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
<td><a href="element-application.md">Application</a> </td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For more info on tile dimension requirements, see [Tile sizes](/previous-versions/windows/apps/hh781198(v=win.10)).

**Logo** and **SmallLogo** images can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **DisplayName** and **Description** attributes. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

Applications/Application/Extensions/Extension/FileTypeAssociation/Logo Applications/Application/Extensions/Extension/Protocol/Logo

Size requirements of two types of logo images are shown here:

Image attribute
Scale
Image size in pixels
Applications\\Application\\VisualElements\\@Logo
100
150x150
140
210x210
180
270x270
Applications\\Application\\VisualElements\\@SmallLogo
100
30x30
140
42x42
180
54x54
 

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
        <VisualElements 
            DisplayName="ApplicationDataSample" 
            Logo="images\squareTile-sdk.png" 
            SmallLogo="images\smallTile-sdk.png" 
            Description="Application data sample" 
            ForegroundText="dark" 
            BackgroundColor="#FFFFFF" 
            ToastCapable="false">
            <DefaultTile ShowName="allLogos"/>
            <SplashScreen BackgroundColor="white" Image="images\splash-sdk.png"/>
        </VisualElements>
    </Application>
</Applications>
                
```

## See also


[App screenshots and images](/windows/uwp/publish/app-screenshots-and-images)

[**Colors class**](/uwp/api/Windows.UI.Colors)

[Quickstart: Creating a default tile using the Visual Studio manifest editor](/previous-versions/windows/apps/hh465437(v=win.10))

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
