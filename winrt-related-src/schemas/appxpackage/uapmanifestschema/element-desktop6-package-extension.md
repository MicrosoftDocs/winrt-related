---
author: mcleanbyron
title: desktop6:Extension
description: Declares an extensibility point for the app.
ms.author: mcleans
ms.date: 03/05/2019
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:Extension (in Package/Extensions)

## Description
Declares an extensibility point for the desktop application.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;desktop6:Extension&gt;</b></dd>
</dl>
</dd>
</dl>


## Syntax
``` xml
<desktop6:Extension Category = "windows.mutablePackageDirectories" | "windows.customInstall"
                    Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                    EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                    RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                    StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

  <!-- Child elements -->
  ( desktop6:MutablePackageDirectories
  | desktop6:CustomInstall )?

</desktop6:Extension>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following: windows.mutablePackageDirectories, windows.customInstall | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: &lt:, &gt;, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | No |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [MutablePackageDirectories](element-desktop6-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |  
| [CustomInstall](element-desktop6-custominstall.md) | Enables your desktop application to specify one or more additional installer files (.exe or .msi) that are installed with your desktop application. For example, this is useful for applications that bundle a 3rd party redistributable component. | 


### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extensions (type: CT_PackageExtensions)](element-extensions.md) | Defines one or more extensibility points for the package. |  

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/6</p></td>
</tr>
</tbody>
</table>
