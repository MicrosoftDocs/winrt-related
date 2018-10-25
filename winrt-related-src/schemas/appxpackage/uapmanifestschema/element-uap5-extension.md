---
author: laurenhughes
title: uap5:Extension
description: Declares an extensibility point for the app.
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, extension 
---

# uap5:Extension

## Description
Declares an extensibility point for the app.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;uap5:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<uap5:Extension Category       = "windows.userActivity" | "windows.mediaSource" | "windows.videoRendererEffect" | "windows.activatableClass.outOfProcessServer" | "windows.startupTask" | "windows.appExecutionAlias"
                   Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                   EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                   RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                   StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. 
                   ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. >

  <!-- Child elements -->
  ( uap5:UserActivity
  | uap5:MediaSource
  | uap5:VideoRendererEffect 
  | uap5:ActivatableClass.OutOfProcessServer
  | uap5:StartupTask
  | uap5:AppExecutionAlias )?

</uap5:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following:<ul><li>windows.userActivity</li><li>windows.mediaSource</li><li>windows.videoRendererEffect</li><li>windows.activatableClass.outOfProcessServer</li><li>windows.startupTask</li><li>windows.appExecutionAlias</li></ul> | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [UserActivity](element-uap5-UserActivity.md) | Allows an app to specify the web site associated with this application for cross platform UserActivity publishing. |
| [MediaSource](element-uap5-MediaSource.md) | Specifies the media source and the app service that it exposes. | 
| [VideoRendererEffect](element-uap5-VideoRendererEffect.md) | Enables activation of video renderer effects in apps. |
| [ActivatableClass.OutOfProcessServer](element-uap5-OutOfProcessServer.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process. |
| [StartupTask](element-uap5-StartupTask.md) | Specifies a startup task for your application. |
| [AppExecutionAlias](element-uap5-AppExecutionAlias.md) | Specifies the application's execution alias to determine the entry point for an app to be activated. |

## Remarks

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>
