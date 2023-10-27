---
title: uap8:PosPaymentConnector
description: Contains device information for Point-of-Sale/Point-of-Service devices.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap8:PosPaymentConnector

Contains device information for Point-of-Sale/Point-of-Service devices.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap8:Extension\>](element-uap8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap8:PosPaymentConnector\>**

## Syntax

```xml
<uap8:POSPaymentConnector
  DisplayName = 'A string with a value between 1 and 256 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The display name of the device. | A string with a value between 1 and 256 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap8:Extension](element-uap8-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| Minimum OS Version | Windows 10 version 1903 (Build 18362) |
