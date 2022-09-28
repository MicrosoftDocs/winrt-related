---
description: Defines a dependency on a host app package for the current app package.
title: uap10:HostRuntimeDependency
keywords: windows 10, uwp, schema, package manifest, host app, hosted app
ms.topic: reference
ms.date: 04/20/2020
---

# uap10:HostRuntimeDependency

Defines a dependency on a host app for the current app. For more information, see [Create hosted apps](/windows/uwp/launch-resume/hosted-apps).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Dependencies\>](element-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:HostRuntimeDependency\>**

## Syntax

```xml
<uap10:HostRuntimeDependency
  Name = 'An alphanumeric string that can contain periods and dashes.'
  Publisher = 'A string with a value between 1 and 8192 characters in length that fits the regular expression of a distinguished name.'
  MinVersion = 'A version string in quad notation ("Major.Minor.Build.Revision"), where "Major" cannot be "0".'  />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the host app. | An alphanumeric string that can contain periods and dashes. | Yes |  |
| **Publisher** | The publisher of the host app. | A string with a value between 1 and 8192 characters in length that fits the regular expression of a distinguished name. | Yes |  |
| **MinVersion** | The minimum version of the host app that the current app depends on. | A version string in quad notation (`Major.Minor.Build.Revision`), where `Major` cannot be `0`. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
