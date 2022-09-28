---
ms.assetid: e6c37b57-76f9-403f-90a7-2b8bda57e905
title: uap4:DevicePortalProvider
description: Defines a Device Portal provider for deployment.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:DevicePortalProvider

Defines a Device Portal provider for deployment.  See [Write a custom plugin for Device Portal](/windows/uwp/debug-test-perf/device-portal-plugin) for more details on implementation.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:Extension\>](element-uap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:DevicePortalProvider\>**

## Syntax

```xml
<uap4:DevicePortalProvider
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
  AppServiceName = 'A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  ContentRoute = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  HandlerRoute = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />            
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value
|-|-|-|-|-|
| **DisplayName** | A friendly display name for the device portal provider. | A string with a value between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **AppServiceName** | The name of the app service used to launch the device portal provider. | A string with a value between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | Yes |  |
| **ContentRoute** | A route that's used to declare HTTP content (JavaScript, HTML, and CSS), e.g., /foo| An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **HandlerRoute** | The API namespace requested by the provider, e.g., /foo/bar. Any successful HTTP requests will be sent to the provider for handling. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the app. |

## Remarks

This extension requires the *devicePortalProvider* restricted capability and either the *privateNetworkClientServer* or *internetClientServer* capability.

> [!NOTE]
> `ContentRoute` and `HandlerRoute` do not need to be provided together.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
