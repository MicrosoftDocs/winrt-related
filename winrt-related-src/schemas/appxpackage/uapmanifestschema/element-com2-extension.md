---
title: com2:Extension (Windows 10)
description: Provides functionality to expose COM registrations to clients outside of the app package.
ms.date: 04/20/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---


# com2:Extension (Windows 10)

## Description
Provides functionality to expose COM registrations to clients outside of the app package.

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
<dd><b>&lt;com2:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<com2:Extension Category = "windows.comServer" | "windows.comInterface" 
               uap10:TrustLevel?   = String value. Can be one of the following: "appContainer", "mediumIL".
               uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
               uap10:HostId?       = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
               uap10:Parameters?   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( com2:ComServer
  | com2:ComInterface )
</com2:Extension>
```

## Key

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The type of app extensibility point. | This attribute can have one of the following values: <ul><li>windows.comServer</li><li>windows.comExtension</li></ul>| Yes |
| uap10:TrustLevel | Specifies the trust level of the extension. | String value. Can be one of the following: "appContainer", "mediumIL".  | No |
| uap10:RuntimeBehavior | Specifies the run time behavior of the extension. | String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".  | No |
| uap10:HostId | Specifies the app ID of the host app for the extension. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.  | No |
| uap10:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.  | No |


## Child Elements

| Child Element         | Description |
|-----------------------|-------------|
| [com2:ComServer](element-com2-comserver.md) | Declares a package extension point of type **windows.comServer**. |
| [com2:ComInterface](element-com2-cominterface.md) | Declares a package extension point of type **windows.comInterface**. |

## Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

## Examples

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/2`<br/><br/>`http://schemas.microsoft.com/appx/manifest/uap/windows10/10` (for the **uap10** attributes) |
