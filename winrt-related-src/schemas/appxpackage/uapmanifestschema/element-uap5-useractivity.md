---
title: uap5:UserActivity
description: Allows an app to opt out of engagement data tracking.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:UserActivity

Allows an app to specify the web site associated with this application for cross platform UserActivity publishing.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:UserActivity\>**

## Syntax

```xml
<uap5:UserActivity
  ActivitySourceHost = 'A string with a value between 1 and 255 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActivitySourceHost** | The fully-qualified domain name of the web site associated with the app. | A string with a value between 1 and 255 characters in length. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
