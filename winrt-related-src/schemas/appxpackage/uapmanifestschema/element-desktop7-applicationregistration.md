---
title: desktop7:ApplicationRegistration
description: Registers an application, replacing the need to register the application in the system PATH variable.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ApplicationRegistration

Registers an application in the registry, replacing the need to register the application in the system PATH variable.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:ApplicationRegistration\>**

## Syntax

```xml
<desktop7:ApplicationRegistration 
  Name =  'A string with a value between 1 and 256 characters in length. This string is localizable.'
  Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'  
  ApplicationName = 'A string with a value between 1 and 256 characters in length.'
  ApplicationDescription = 'A string with a value between 1 and 256 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A display name for the application. | A string with a value between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Path** | The path to the application. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ApplicationName** | The name of the application. | A string with a value between 1 and 256 characters in length. | Yes |  |
| **ApplicationDescription** | The description of the application. | A string with a value between 1 and 256 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  

## Remarks

For information on registering applications, see [Application Registration](/windows/win32/shell/app-registration).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| Minimum OS Version | Windows 10 (Build 19645) |
