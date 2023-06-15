---
title: UAP3:Protocol
description: Declares an app extensibility point of type windows.protocol. A URI association indicates the app is registered to handle URIs with the specified scheme.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# uap3:Protocol

Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:Protocol\>**

## Syntax

```xml
<uap3:Protocol
  parameters = 'A string with a value or set of string values between 1 and 32767 characters.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Parameters** | The class ID associated with this media content. | A string with a value or set of string values between 1 and 32767 characters. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Sets parameters to define the protocol of the extensions. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
