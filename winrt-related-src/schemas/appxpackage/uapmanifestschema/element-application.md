---
description: Represents an app that comprises part of or all of the functionality delivered in the package.
Search.Product: eADQiWindows 10XVcnh
title: Application (Windows 10)
ms.assetid: 39221d13-bb46-42ac-be51-117357cade81


keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 03/21/2019
---

# Application (Windows 10)


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
<Application Id                  = An ASCII string between 1 and 64 characters in length. See the Attributes table for more information on character restrictions.
             Executable?         = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
             EntryPoint?         = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
             StartPage?          = Any valid URI or IRI (the non-ASCII version of a URI). See below for more details. 
             ResourceGroup?      = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
             desktop4:Subsystem? = String value. Can be one of the following: "console", "windows"
             uap10:Subsystem?    = String value. Can be one of the following: "console", "windows"
             desktop4:SupportsMultipleInstances? = Boolean.
             uap10:SupportsMultipleInstances? = Boolean.
             uap10:TrustLevel?   = String value. Can be one of the following: "appContainer", "mediumIL".
             uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
             uap10:HostId?       = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
             uap10:Parameters?   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( uap:VisualElements
  & uap:ApplicationContentUriRules?
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
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Id</strong></td>
<td><p>The unique identifier of the application within the package. This value is sometimes referred to as the package-relative app identifier (PRAID).</p>
<p>The ID is unique within the package but not globally. There may be another package on the system that uses the same ID. The same ID cannot be used more than once in the same package.</p>
<p>This string contains alpha-numeric fields separated by periods. Each field must begin with an ASCII alphabetic character. You cannot use these as field values: &quot;CON&quot;, &quot;PRN&quot;, &quot;AUX&quot;, &quot;NUL&quot;, &quot;COM1&quot;, &quot;COM2&quot;, &quot;COM3&quot;, &quot;COM4&quot;, &quot;COM5&quot;, &quot;COM6&quot;, &quot;COM7&quot;, &quot;COM8&quot;, &quot;COM9&quot;, &quot;LPT1&quot;, &quot;LPT2&quot;, &quot;LPT3&quot;, &quot;LPT4&quot;, &quot;LPT5&quot;, &quot;LPT6&quot;, &quot;LPT7&quot;, &quot;LPT8&quot;, and &quot;LPT9&quot;.</p>
<p>When using a Visual Studio template, the default value of this attribute is &quot;App&quot;. Developers should manually change this in the manifest.</p>
<p>The app's identifier should not be changed after the app has been published to the Microsoft Store; doing so will disrupt the tile's position on the Start screen.</p></td>
<td>An ASCII string between 1 and 64 characters in length.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ResourceGroup</strong></td>
<td><p>ResourceGroup is a tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). See <a href="element-uap-extension.md"><strong>Extension@ResourceGroup</strong></a>.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>StartPage</strong></td>
<td><p>The default launch HTML page for the app. This can be a relative Windows file path referencing a document in the app's package, or it can be an absolute URL (so that a web site can publish as an app in the Store). The URL can only be starting with http://, https:// or ms-appx-web://. This is the entry point document that will be loaded by WWAHost when starting a WWA for that app. </p>
<p>Technically, the value may be a URL or an IRI—the non-ASCII version of a URI. An IRI must support up to 2084 characters and must be allowed to contain the %, and reserved and unreserved characters as described in <a href="https://tools.ietf.org/html/rfc3986#appendix-a">RFC 3986 Appendix A</a>.</p>
<p>If you specify this attribute, you cannot specify either the <strong>EntryPoint</strong> attribute or the <strong>Executable</strong> attribute.</p></td>
<td>Any valid URI or IRI (the non-ASCII version of a URI).</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>desktop4:Subsystem</strong></td>
<td><p>Indicates whether the app is a standard UWP app or a UWP console app. </p></td>
<td>String value. Can be one of the following: "console", "windows".</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:Subsystem</strong></td>
<td><p>Indicates whether the app is a standard UWP app or a UWP console app. </p></td>
<td>String value. Can be one of the following: "console", "windows".</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>desktop4:SupportsMultipleInstances</strong></td>
<td><p>Indicates support of multiple, separate instances of UWP apps. For more information, see the remarks section. </code> namespace.</p></td>
<td>Boolean value.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:SupportsMultipleInstances</strong></td>
<td><p>Indicates support of multiple, separate instances of UWP apps. For more information, see the remarks section. </code> namespace.</p></td>
<td>Boolean value.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap10:TrustLevel</strong></td>
<td><p>Specifies the trust level of the app.</p></td>
<td>String value. Can be one of the following: "appContainer", "mediumIL". </td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:RuntimeBehavior</strong></td>
<td><p>Specifies the run time behavior of the app.</p></td>
<td>String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App". </td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap10:HostId</strong></td>
<td><p>This value specifies the app ID of the host app for the current app. This attribute is used for <a href="/windows/uwp/launch-resume/hosted-apps">hosted apps</a>.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap10:Parameters</strong></td>
<td><p>Contains command line parameters to pass to the app. Only supported for desktop apps that have package identity.</p></td>
<td>A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. </td>
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
<td><a href="element-1-extensions.md">Extensions (type: CT_ApplicationExtensions)</a> </td>
<td><p>Defines one or more extensibility points for the app.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-applicationcontenturirules.md">uap:ApplicationContentUriRules</a> </td>
<td><p>Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap-visualelements.md">uap:VisualElements</a> </td>
<td><p>Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tr>
<tr class="even">
<td><a href="element-uap7-properties.md">uap7:Properties</a> </td>
<td><p>Specifies properties of the app.</p></td>
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
<td><a href="element-applications.md">Applications</a> </td>
<td><p>Represents one or more apps that comprise the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **Application** element contains attributes that are common to the extensibility points that pertain to the app. This information is used by other extensibility points to get information about the app. Also, **Application** attributes are used in the start and management of an instance of the app.

The **StartPage** applies only to a JavaScript app. If **StartPage** is not specified, then both the **Executable** and **EntryPoint** attributes must be specified, and this applies only to a C#, C++, or VB app.

Important notes about multi-instancing apps:

- If an app declares **SupportsMultipleInstances** within the **Application** element, then all foreground extensions will also be multi-instanced.
- If the app declares **SupportsMultipleInstances** within the **Application** element, then it does not need to be declared at the [Extensions](element-1-extensions.md) level (for example, in a [BackgroundTasks](element-backgroundtasks.md) or [AppService](element-uap3-appservice-manual.md) element).
- The app should only declare **SupportsMultipleInstances** on background tasks, background audio, or app services.
- Console apps will always be multi-instanced and must explicitly declare **SupportsMultipleInstances**.
- Apps can use the **ResourceGroup** declaration in the manifest to group multiple background tasks into the same host. This conflicts with multi-instancing, where each activation goes into a separate host. Therefore, an app cannot declare both **SupportsMultipleInstances** and **ResourceGroup** in the manifest.

For more information about using the **SupportsMultipleInstances** attribute to support multiple, separate instances of UWP apps, see [Create a multi-instance Universal Windows App](/windows/uwp/launch-resume/multi-instance-uwp).

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10`<br/><br/>**desktop4** attributes: `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4`<br/><br/>**uap10** attributes: `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
