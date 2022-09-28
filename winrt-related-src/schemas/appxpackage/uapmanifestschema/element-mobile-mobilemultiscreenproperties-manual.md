---
description: Declares an app extensibility point of type windows.MobileMultiScreenProperties.
Search.Product: eADQiWindows 10XVcnh
title: mobile:MobileMultiScreenProperties (Windows 10)
ms.assetid: 86ea3e53-23e4-4c7a-9490-2944dbcca460
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# mobile:MobileMultiScreenProperties (Windows 10)

Declares an app extensibility point of type **windows.MobileMultiScreenProperties**.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<mobile:Extension\>](element-mobile-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<mobile:MobileMultiScreenProperties\>**

## Syntax

```xml
<mobile:Extension
  RestrictToInternalScreen = 'A boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **RestrictToInternalScreen** | Determines whether to restrict the app's display output to the mobile device's integral screen. Setting this to true prevents the app's display from being sent to an external display. | A boolean value. | Yes | true |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [mobile:Extension](element-mobile-extension-manual.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/mobile/windows10` |
