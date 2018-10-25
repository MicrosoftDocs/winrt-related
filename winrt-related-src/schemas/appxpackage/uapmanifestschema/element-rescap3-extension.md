---
author: laurenhughes
ms.assetid: d90b7275-21bd-46c7-89a7-c832a95186c6
title: rescap3:Extension
description: Declares an extensibility point for the app.
ms.author: lahugh
ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:Extension

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
<dd><b>&lt;rescap3:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<rescap3:Extension Category       = "windows.desktopAppMigration" | "windows.lockScreenComponent" 
                   Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                   EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                   RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                   StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

  <!-- Child elements -->
  ( rescap3:DesktopAppMigration | 
    rescap3:LockScreenComponent )?
</rescap3:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following: windows.desktopAppMigration, windows.lockScreenComponent | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [DesktopAppMigration](element-rescap3-desktopappmigration.md) | Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app. |   

## Remarks
**windows.lockScreenComponent** is an empty extension declaration that supports hosting UWP apps inside the welcome screen.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3</p></td>
</tr>
</tbody>
</table>