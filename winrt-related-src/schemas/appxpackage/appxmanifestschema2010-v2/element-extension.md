---
description: Declares an extensibility point for the app (CT_ApplicationExtension).
Search.Product: eADQiWindows 10XVcnh
title: 'Extension (type: CT_ApplicationExtension)'
ms.assetid: 72f0d1ae-15a4-4eba-a3ca-990f4de2b697


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Extension (type: CT_ApplicationExtension)


Declares an extensibility point for the app.

## Element hierarchy

**&lt;Extension&gt;**

## Syntax

``` syntax
<Extension Category     = "windows.fileTypeAssociation" | "windows.protocol" | "windows.autoPlayContent" | "windows.autoPlayDevice" | "windows.shareTarget" | ...
           Executable?  = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
           EntryPoint?  = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
If EntryPoint is not specified, the EntryPoint defined for the app is used instead.

           RuntimeType? = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
           StartPage?   = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

  <!-- Child elements -->
  ( FileTypeAssociation
  | Protocol
  | AutoPlayContent
  | AutoPlayDevice
  | ShareTarget
  | FileOpenPicker
  | FileSavePicker
  | BackgroundTasks
  )?

</Extension>
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
<td><strong>Category</strong></td>
<td><p>The type of app extensibility point.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>windows.fileTypeAssociation</li>
<li>windows.protocol</li>
<li>windows.autoPlayContent</li>
<li>windows.autoPlayDevice</li>
<li>windows.shareTarget</li>
<li>windows.search</li>
<li>windows.fileOpenPicker</li>
<li>windows.fileSavePicker</li>
<li>windows.cachedFileUpdater</li>
<li>windows.contactPicker</li>
<li>windows.backgroundTasks</li>
<li>windows.cameraSettings</li>
<li>windows.accountPictureProvider</li>
<li>windows.printTaskSettings</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>EntryPoint</strong></td>
<td><p>The activatable class ID.</p></td>
<td>A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Executable</strong></td>
<td><p>The default launch executable.</p></td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>RuntimeType</strong></td>
<td><p>The runtime provider. This attribute is used typically when there are mixed frameworks in an app.</p></td>
<td>A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, &quot;, /, \, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>StartPage</strong></td>
<td><p>The web page that handles the extensibility point.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
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
<td><a href="element-autoplaycontent.md">AutoPlayContent</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayContent</strong>. The app provides the specified AutoPlay content actions.</p></td>
</tr>
<tr class="even">
<td><a href="element-autoplaydevice.md">AutoPlayDevice</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.autoPlayDevice</strong>. The app provides the specified AutoPlay device actions.</p></td>
</tr>
<tr class="odd">
<td><a href="element-backgroundtasks.md">BackgroundTasks</a> </td>
<td><p>Defines an app extensibility point of type <strong>windows.backgroundTasks</strong>. Background tasks run in a dedicated background host; that is, without a UI.</p></td>
</tr>
<tr class="even">
<td><a href="element-fileopenpicker.md">FileOpenPicker</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileOpenPicker</strong>. The app lets the user choose and open the specified types of files.</p></td>
</tr>
<tr class="odd">
<td><a href="element-filesavepicker.md">FileSavePicker</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileSavePicker</strong>. The app lets the user choose the file name, extension, and storage location for the specified types of files.</p></td>
</tr>
<tr class="even">
<td><a href="element-filetypeassociation.md">FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
<tr class="odd">
<td><a href="element-protocol.md">Protocol</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.protocol</strong>. A URI association indicates that the app is registered to handle URIs with the specified scheme.</p></td>
</tr>
<tr class="even">
<td><a href="element-sharetarget.md">ShareTarget</a> </td>
<td><p>Declares an app extension point of type <strong>windows.shareTarget</strong>. The app can share the specified types of files.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[Extension (in type: CT_PackageExtensions)](element-1-extension.md)**

## Remarks

These extensibility points can be declared only once per app:

-   **windows.accountPictureProvider**
-   **windows.cachedFileUpdater**
-   **windows.cameraSettings**
-   **windows.contactPicker**
-   **windows.fileOpenPicker**
-   **windows.fileSavePicker**
-   **windows.printTaskSettings**
-   **windows.search**
-   **windows.shareTarget**

**Note about semantic rules for extensions:  **For any Extension element the following semantic rules are enforced in the manifest API:

If /Application/@StartPage specified, it is a Windows app using JavaScript and the App Extension :

-   Can be empty
-   Can specify just the StartPage
-   Can specify both Executable and EntryPoint (optional RuntimeType allowed), unless it is a BackgroundTask extension, in which case it can omit the Executable and default to the BackgroundTaskHost.exe executable.

If /Application/@StartPage is not specified, it is a UWP app using C# or VB and XAML and the App Extension :

-   Can be empty
-   Can specify just the StartPage
-   Must specify EntryPoint if either Executable or RuntimeType is specified.

## See also


**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
