---
description: Declares an app extensibility point of type windows.appService (uap:AppService).
Search.Product: eADQiWindows 10XVcnh
title: uap:AppService (Windows 10)
ms.assetid: 53420864-d8b4-4f30-bb74-5148d89be5f1
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:AppService (Windows 10)

Declares an app extensibility point of type **windows.appService**. Application Contracts are a way for an app to invoke a background task belonging to another app; or for a background task invoked to service an app contract a way to communicate with its caller.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:AppService\>**

## Syntax

```xml
<uap:AppService
  Name = 'A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  ServerName = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap4:SupportsMultipleInstances = 'A boolean value'. />
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The service name (used to match the caller of the Application Contract with the provider). | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |  |
| **ServerName** | The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes. | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap4:SupportsMultipleInstances** | Supports multiple, separate instances of an app service. | A boolean value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
