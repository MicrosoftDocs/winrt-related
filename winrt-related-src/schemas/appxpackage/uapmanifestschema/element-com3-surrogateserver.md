---
title: com3:SurrogateServer
description: Registers a SurrogateServer with one or many class registrations (com3:SurrogateServer).
ms.date: 04/20/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com3:SurrogateServer

Registers a SurrogateServer with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com2:Extension\>](element-com2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com2:ComServer\>](element-com2-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com3:SurrogateServer\>**

## Syntax

```xml
<com3:SurrogateServer  
    CustomSurrogateExecutable = 'An optional string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
    DisplayName = 'An optional string with a value between 1 and 256 characters in length. This string is localizable.'
    LaunchAndActivationPermission = 'An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value.'
    AppId = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    SystemSurrogate = 'An optional string value.' >

  <!-- Child elements -->
  Class{1,10000}

</com3:SurrogateServer>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **CustomSurrogateExecutable** | A path to the DllSurrogate in the AppId key. This path is relative to the package root and must reference a file in the package. This is mutually exclusive with SystemSurrogate. | An optional string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **DisplayName** | DisplayName is a localizable string corresponding to the default AppID key value. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value. | No |  |
| **AppId** | The AppId that references the associated AppId key. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **SystemSurrogate** | A value that corresponds to well-known values from the DllSurrogate value of the AppId key. This is mututally exclusive with CustomSurrogateExecutable. | An optional string value. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com-surrogateserver-class.md) | Defines a SurrogateServer class registration. |

### Parent elements

| Parent element | Description |
|-|-|
| [com2:ComServer](element-com2-comserver.md) | Declares a package extension point of type **windows.comServer**. The **comServer** extension may include the following types of registrations: *ServiceServer*, *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*. |

## Remarks

If there is no value for the DllSurrogate in the [AppId key](/windows/win32/com/appid-key), do not use the CustomSurrogateExecutable attribute.

**LaunchAndActivationPermission** is an [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the [AppID key](/windows/win32/com/appid-key).

The **SystemSurrogate** corresponds to the values of the DllSurrogate value of the AppId key. For example, if the DllSurrogate value is `%System32%\prevhost.exe` or `%SysWow64%\prevhost.exe`, then **SystemSurrogate** should be set to `PreviewHost` and the **CustomSurrogateExecutable** should not be set.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |
