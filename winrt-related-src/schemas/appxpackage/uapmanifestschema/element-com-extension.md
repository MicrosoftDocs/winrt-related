---
ms.assetid: ae4a725d-10f9-4e03-a579-c3db2d859a9f
title: com:Extension (Windows 10)
description: Provides functionality to expose COM registrations to clients outside of the app package (com:Extension).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Extension (Windows 10)

Provides functionality to expose COM registrations to clients outside of the app package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Extension\>**

## Syntax

```xml
<com:Extension
  Category = 'A string that can be one of the following values: "windows.comServer" or "windows.comInterface".' 
  uap10:TrustLevel = 'An optional string value that can one of the following value: "appContainer" or "mediumIL".'
  ap10:RuntimeBehavior = 'An optional string with a value that can be one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  ap10:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  com:ComServer
  com:ComInterface

</com:Extension>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of app extensibility point. | A string that can be one of the following values: *windows.comServer* or *windows.comInterface*. | Yes |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string value that can one of the following value: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. | An optional string with a value that can be one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*.  | No |  |
| **uap10:HostId** | Specifies the app ID of the host app for the extension. | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [com:ComServer](element-com-comserver.md) | Declares a package extension point of type **windows.comServer**. |
| [com:ComInterface](element-com-cominterface.md) | Declares a package extension point of type **windows.comInterface**. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
