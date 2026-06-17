---
title: uap4:Rule
description: Defines rules for inbound and outbound loopback connections.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap4:Extension, uap4:LoopbackAccessRules, uap4:Rule]
keywords: windows 10, uwp, schema, manifest, extension
---

# uap4:Rule

Defines rules for inbound and outbound loopback connections.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:Extension>`](element-uap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:LoopbackAccessRules>`](element-uap4-loopbackaccessrules.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:Rule>`**

## Syntax

```xml
<uap4:Rule
  Direction = 'A required string that can have one of the following values: "in", or "out".'
  PackageFamilyName = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Direction** | Specifies whether the connection will be inbound or outbound over loopback. | A string that can have one of the following values: *in*, *out*. | Yes |  |
| **PackageFamilyName** | The package family name of the app to connect to. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap4:LoopbackAccessRules](element-uap4-loopbackaccessrules.md) | Contains rules for a loopback filter that enables communication between an app and a service. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

Loopback connections are supported only for TCP connections.

> [!NOTE]
> The UDP protocol is not supported.

## Examples

<!-- Author content goes here -->
