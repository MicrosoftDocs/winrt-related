---
title: desktop:ParameterGroup
description: Represents a group of command-line parameters for a full-trust process.
ms.date: 05/10/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop:ParameterGroup

Represents a group of command-line parameters for a full-trust process.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Desktop:Extension\>](element-desktop-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Desktop:FullTrustProcess\>](element-desktop-fulltrustprocess.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop:ParameterGroup\>**

## Syntax

```xml
<desktop:ParameterGroup
  GroupId = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Parameters = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **GroupId** | The name for a group of one or more related command-line parameters. You can pass this group ID to the [LaunchFullTrustProcessForAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforappasync) or [LaunchFullTrustProcessForCurrentAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforcurrentappasync) method. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Parameters** | The command line parameters to associate with the **GroupId** value. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [desktop:FullTrustProcess](element-desktop-fulltrustprocess.md) | Represents a desktop process that runs in full-trust. |

## Remarks

For more details, see [LaunchFullTrustProcessForAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforappasync) and [LaunchFullTrustProcessForCurrentAppAsync](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher.launchfulltrustprocessforcurrentappasync).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
