---
author: laurenhughes
ms.assetid: f082edc4-0add-46b3-a232-17007783ecb2
title: desktop2:Extension
description: Declares an extensibility point for the app.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:Extension (in Package/Extensions)

## Description
Declares an extensibility point for the app.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;desktop2:Extension&gt;</b></dd>
</dl>
</dd>
</dl>


## Syntax
``` syntax
<Extension     Category       = "windows.firewallRules" | "windows.desktopEventLogging" 
               Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
               EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
               RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
               StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

  <!-- Child elements -->
  ( desktop2:FirewallRules
  | desktop2:DesktopEventLogging )?

</uap:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following: windows.firewallRules, windows.desktopEventLogging | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. | No |


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [FirewallRules](element-desktop2-appprinter.md) |  |  
| [DesktopEventLogging](element-desktop2-searchfilterhandler.md) | Enables Windows Desktop Bridge apps to register for Windows event logging. | 


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>