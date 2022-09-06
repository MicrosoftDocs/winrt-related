---
title: com4:ServiceServer
description: Registers a ServiceServer with one or many class registrations. (com4:ServiceServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ServiceServer

Registers a ServiceServer with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ServiceServer\>**

## Syntax

```xml
<com4:ServiceServer
  ServiceName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
  Arguments = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
  DisplayName = A string between 1 and 256 characters in length. This string is localizable.
  LaunchAndActivationPermission = [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). >

  <!-- Child elements -->
  Class
  ClassReference

</com4:ServiceServer>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServiceName** | The name of the Windows service that hosts the COM server.  | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |  |
| **Arguments** | The command-line parameters of the service. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |  |
| **DisplayName** | A localizable string corresponding to the default AppID key value. | A string between 1 and 256 characters in length. This string is localizable.| Yes |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).| Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com4-exeserver-class.md) | Defines an ExeServer class registration. |
| [ClassReference](element-com4-exeserver-classreference.md) | Specifies the class with which the registered ExeServer is associated and sets ExeServer-specific registration details. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
