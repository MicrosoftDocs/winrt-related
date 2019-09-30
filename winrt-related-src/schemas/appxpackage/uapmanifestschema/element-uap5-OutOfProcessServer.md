---
author: mcleanbyron
title: uap5:OutOfProcessServer
description: Declares a package extension point of type windows.activatableClass.outOfProcessServer. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process.
ms.author: mcleans
ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:OutOfProcessServer

## Description
Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process.

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
<dd>
<dl>
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd><b>&lt;uap5:OutOfProcessServer&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap5:OutOfProcessServer ServerName    = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
                         RunFullTrust? = Boolean. >
  <!-- Child elements -->
  ( uap5:Path,
    uap5:Arguments?,
    uap5:Instancing,
    uap5:ActivatableClass{1,65535} )
</uap5:OutOfProcessServer>
```

### Key
`?`   optional (zero or one)
`{}` specific range of occurrences

## Attributes and Elements
### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ServerName | A string value of the server name. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |
| RunFullTrust | If true, the server will be launched with a Windows Desktop Bridge token, as opposed to a UWP token. | Boolean. | No |
| IdentityType | The activation type of the server. | A string value that can be one of the following: activateAsPackage, activateAsActivator. | No | 

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [Path](element-uap5-path.md) | The path to the executable. |
| [Arguments](element-uap5-arguments.md) | Specifies the list of comma-separated arguments to pass to the executable. |
| [Instancing](element-uap5-instancing.md) | Specifies whether the executable runs as a single instance or can run as multiple instances. |
| [ActivatableClass](element-uap5-ActivatableClass.md) | Declares a runtime class associated with the extensibility point. |

## Remarks
This element is similar to the [OutOfProcessServer](element-outOfProcessServer.md) element in Package/Extensions. Activate As Package behavior is implied by using this element in the Application/Extensions level of the manifest, indicating that the server token doesn't vary based on the activating process's token. In this context, the application identity claim matches the identity of the application it's contained in.

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