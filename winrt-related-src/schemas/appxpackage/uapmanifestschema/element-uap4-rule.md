---
ms.assetid: 7ec485fd-ecd8-49f3-82cd-fbf1e0656222
title: uap4:Rule
description: Defines rules for inbound and outbound loopback connections.
ms.date: 05/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# uap4:Rule

Defines rules for inbound and outbound loopback connections.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:Extension\>](element-uap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:LoopbackAccessRules\>](element-uap4-loopbackaccessrules.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:Rule\>**

## Syntax

```xml
<uap4:Rule
  Direction = 'A string that can have one of the following values: "in" or "out".'
  PackageFamilyName = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >                  
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Direction** | Specifies whether the connection will be inbound or outbound over loopback. | A string that can have one of the following values: *in* or *out*. | Yes |  |
| **PackageFamilyName** | The package family name of the app to connect to. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap4:LoopbackAccessRules](element-uap4-loopbackaccessrules.md) | Contains rules for a loopback filter that enables communication between an app and a service. |

## Remarks

Loopback connections are supported only for TCP connections.

> [!NOTE]
> The UDP protocol is not supported.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
