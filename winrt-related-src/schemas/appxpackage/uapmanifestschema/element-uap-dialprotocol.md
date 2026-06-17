---
title: uap:DialProtocol
description: Declares an app extensibility point of type windows.dialProtocol.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:DialProtocol]
---

# uap:DialProtocol

Declares an app extensibility point of type **windows.dialProtocol**.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:DialProtocol>`**  

## Syntax

```xml
<uap:DialProtocol
  Name = 'A required string with a value between 2 and 39 characters in length that can contain numbers, uppercase and lowercase letters, periods (`.`), plus signs (`+`), or dashes (`-`). The string cannot start with a period (`.`).' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The app's registered DIAL name. | A string with a value between 2 and 39 characters in length that can contain numbers, uppercase and lowercase letters, periods (`.`), plus signs (`+`), or dashes (`-`). The string cannot start with a period (`.`). | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Extension
    Category="windows.dialProtocol">
    <uap:DialProtocol
        Name="Contoso"/>
</Extension>
```
