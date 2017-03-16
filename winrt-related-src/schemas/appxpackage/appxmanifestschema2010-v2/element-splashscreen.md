---
Description: SplashScreen
MS-HAID: AppxManifestSchema2010\_v2.element\_SplashScreen
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: SplashScreen
ms.assetid: eecce5dd-09c3-4f47-b271-0a04fcd64d44
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# SplashScreen

Defines the appearance of the splash screen, which is displayed by the app during launch.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd><b>&lt;SplashScreen&gt;</b></dd>
</dl>

## Syntax

``` syntax
<SplashScreen BackgroundColor? = A three-byte hexadecimal number preceded by "#" or a named color.
              Image            = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both. />
```

### Key

`?`   optional (zero or one)

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
<td><p>Specifies the background color of the splash screen. See the Remarks section for color names.</p></td>
<td>A three-byte hexadecimal number preceded by &quot;#&quot; or a named color.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Image</strong></td>
<td><p>The path to the splash screen image. See the Remarks section for size requirements.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

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
<td>[VisualElements](element-visualelements.md)</td>
<td><p>Describes the visual aspects of the Windows Store app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The splash screen image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](https://msdn.microsoft.com/library/windows/apps/hh831183) topic.

Size requirements of a splash screen image are shown here:

Image attributes
Scale
Image size in pixels
Applications\\Application\\VisualElements\\SplashScreen\\@Image
100
620x300
140
868x420
180
1116x540
 

The following are supported background color names:

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

 

## See also


[**Colors class**](https://msdn.microsoft.com/library/windows/apps/hh747824)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



