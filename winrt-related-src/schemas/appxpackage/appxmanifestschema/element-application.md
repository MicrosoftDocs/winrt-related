---
Description: Represents an app that comprises part of or all of the functionality delivered in the package.
Search.Product: eADQiWindows 10XVcnh
title: Application
ms.assetid: 39221d13-bb46-42ac-be51-117357cade81
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Application


Represents an app that comprises part of or all of the functionality delivered in the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd><b>&lt;Application&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Application Id          = An ASCII string between 1 and 64 characters in length.
             Executable? = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, %, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
             EntryPoint? = A string between 1 and 256 characters in length, representing the task  handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
If EntryPoint is not specified, the EntryPoint defined for the app is used instead.

             StartPage?  = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *. >

  <!-- Child elements -->
  ( VisualElements
  & ApplicationContentUriRules?
  & Extensions?
  )

</Application>
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
<td><strong>EntryPoint</strong></td>
<td><p>The activatable class ID, such as &quot;&quot;Office.Winword.Class&quot;.</p>
<p>If you specify this attribute, you must also specify the <strong>Executable</strong> attribute. If you specify this attribute you must not specify the <strong>StartPage</strong> attribute.</p></td>
<td>A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Executable</strong></td>
<td><p>The default launch executable for the app. This file must be present in the package.</p>
<p>If you specify this attribute you must specify the <strong>EntryPoint</strong> attribute. If you specify this attribute you must not specify the <strong>StartPage</strong> attribute.</p></td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Id</strong></td>
<td><p>The unique identifier of the application within the package. This value is sometimes referred to as the package-relative app identifier (PRAID).</p>
<p>The ID is unique within the package but not globally. There may be another package on the system that uses the same ID. The same ID cannot be used more than once in the same package.</p>
<p>This string contains alpha-numeric fields separated by periods. Each field must begin with an ASCII alphabetic character. You cannot use these as field values: &quot;CON&quot;, &quot;PRN&quot;, &quot;AUX&quot;, &quot;NUL&quot;, &quot;COM1&quot;, &quot;COM2&quot;, &quot;COM3&quot;, &quot;COM4&quot;, &quot;COM5&quot;, &quot;COM6&quot;, &quot;COM7&quot;, &quot;COM8&quot;, &quot;COM9&quot;, &quot;LPT1&quot;, &quot;LPT2&quot;, &quot;LPT3&quot;, &quot;LPT4&quot;, &quot;LPT5&quot;, &quot;LPT6&quot;, &quot;LPT7&quot;, &quot;LPT8&quot;, and &quot;LPT9&quot;.</p>
<p>When using a Visual Studio template, the default value of this attribute is &quot;App&quot;. Developers should manually change this in the manifest.</p>
<p>The app's identifier should not be changed after the app has been published to the Windows Store; doing so will disrupt the tile's position on the Start screen.</p></td>
<td>An ASCII string between 1 and 64 characters in length.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StartPage</strong></td>
<td><p>The default launch HTML page for the app. This file must be present in the package.</p>
<p>If you specify this attribute, you cannot specify either the <strong>EntryPoint</strong> attribute or the <strong>Executable</strong> attribute.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *.</td>
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
<td>[ApplicationContentUriRules](element-applicationcontenturirules.md)</td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
<tr class="even">
<td>[Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md)</td>
<td><p>Defines one or more extensibility points for the app.</p></td>
</tr>
<tr class="odd">
<td>[VisualElements](element-visualelements.md)</td>
<td><p>Describes the visual aspects of the Windows Store app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
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
<td>[Applications](element-applications.md)</td>
<td><p>Represents one or more apps that comprise the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **Application** element contains attributes that are common to the extensibility points that pertain to the app. This information is used by other extensibility points to get information about the app. Also, **Application** attributes are used in the start and management of an instance of the app.

If the **StartPage** attribute is specified, it is a Windows app using JavaScript. If **StartPage** is not specified, then both the **Executable** and **EntryPoint** attributes must be specified, and it is a Windows Store app using C# or VB and XAML.

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
                    
<Applications>
  <Application Id="App" StartPage="default.html">

    <VisualElements DisplayName="Assocation launching sample" 
         Logo="images\squareTile-sdk.png" SmallLogo="images\smallTile-sdk.png" 
         Description="SDK sample" 
         ForegroundText="dark" BackgroundColor="#FFFFFF" ToastCapable="false">
      <DefaultTile ShowName="allLogos" />
      <SplashScreen BackgroundColor="white" Image="images\splash-sdk.png" />
    </VisualElements>

    <Extensions>
      <Extension Category="windows.fileTypeAssociation">
        <FileTypeAssociation Name=".alsdkjs">
          <SupportedFileTypes>
            <FileType>.alsdkjs</FileType>
          </SupportedFileTypes>
        </FileTypeAssociation>
      </Extension>

      <Extension Category="windows.protocol">
        <Protocol Name="alsdkjs" />
      </Extension>
    </Extensions>
  </Application>
</Applications>
                
```

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

 

 



