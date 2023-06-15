---
title: uap13:HostRuntimeDependency
description: Declares publisher information for the app.
keywords: windows 10, uwp, schema, manifest, extension
ms.date: 05/03/2022
ms.topic: reference
---

# uap13:HostRuntimeDependency

Declares publisher information for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap13:Extension\>](element-uap13-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**<\uap13:HostRuntimeDependency\>**

## Syntax

```xml
<uap13:HostRuntimeDependency
  Name = 'An alphanumeric string with a value between 1 and 32767 characters that can contain periods and dashes only.'
  Publisher = 'A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name.'
  MinVersion = 'A version string in quad notation ("Major.Minor.Build.Revision") where "Major" cannot be "0". />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the application. | An alphanumeric string with a value between 1 and 32767 characters that can contain periods and dashes only. | Yes |  |
| **Publisher** | The publisher of the application | A string between 1 and 8192 characters in length that fits the regular expression of a distinguished name. | Yes |  |
| **MinVersion** | The minimum Windows version required to install the application. | A version string in quad notation (`Major.Minor.Build.Revision`) where `Major` cannot be `0`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in Package/Applications)](element-extension.md) | Declares an extensibility point for the app. |

### Requirements

| Item | Value |
|-|-|
| **UAP12** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |
