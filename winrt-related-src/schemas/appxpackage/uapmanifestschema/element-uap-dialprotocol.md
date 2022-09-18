---
description: Declares an app extensibility point of type windows.dialProtocol.
Search.Product: eADQiWindows 10XVcnh
title: uap:DialProtocol (Windows 10)
ms.assetid: d0d0d409-f25c-4a55-b392-726ad9225a76
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:DialProtocol (Windows 10)

Declares an app extensibility point of type **windows.dialProtocol**.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:DialProtocol\>**

## Syntax

```xml
<DialProtocol
    Name = 'A string with a value between 2 and 39 characters in length that can contain numbers, uppercase and lowercase letters, periods ("."), plus signs ("+"), or dashes ("-"). The string cannot start with a period (".").' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The app's registered DIAL name. | A string with a value between 2 and 39 characters in length that can contain numbers, uppercase and lowercase letters, periods (`.`), plus signs (`+`), or dashes (`-`). The string cannot start with a period (`.`). | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Examples

```xml
<Extension
    Category="windows.dialProtocol">
    <uap:DialProtocol
        Name="Contoso"/>
</Extension>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
