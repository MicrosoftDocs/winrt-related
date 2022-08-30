---
ms.assetid: 66534b5a-4f04-4fc6-9a3f-91a7b82930e9
title: com:SurrogateServer
description: Registers a SurrogateServer with one or many class registrations.
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:SurrogateServer

Registers a SurrogateServer with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:SurrogateServer\>**

## Syntax

```xml
<com:SurrogateServer  
    CustomSurrogateExecutable = 'An optional string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
    DisplayName = 'An optional string with a value between 1 and 256 characters in length. This string is localizable.'
    LaunchAndActivationPermission = 'A [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value.'
    AppId = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' 
    SystemSurrogate = 'An optional string value.' >

  <!-- Child elements -->
  Class{1,10000}

</com:SurrogateServer>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |Default value |
|-|-|-|-|-|
| **CustomSurrogateExecutable** | A path to the DllSurrogate in the AppId key. This path is relative to the package root and must reference a file in the package. This is mututally exclusive with SystemSurrogate. | An optional string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*` | No |  |
| **DisplayName** | DisplayName is a localizable string corresponding to the default AppID key value. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | A [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value. | No |  |
| **AppId** | The AppId that references the associated AppId key. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **SystemSurrogate** | A value that corresponds to well-known values from the DllSurrogate value of the AppId key. This is mututally exclusive with CustomSurrogateExecutable. | An optional string value. | No |  |

### Child Elements

| Child Element | Description |
|-|-|
| [Class](element-com-surrogateserver-class.md) | Defines a SurrogateServer class registration. |

### Parent Elements

| Child Element | Description |
|-|-|
| [com:ComServer](element-com-comserver.md) | Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*. |

## Remarks

If there is no value for the DllSurrogate in the [AppId key](/windows/win32/com/appid-key), do not use the CustomSurrogateExecutable attribute.

**LaunchAndActivationPermission** is an [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the [AppID key](/windows/win32/com/appid-key).

The **SystemSurrogate** corresponds to the values of the DllSurrogate value of the AppId key. For example, if the DllSurrogate value is `%System32%\prevhost.exe` or `%SysWow64%\prevhost.exe`, then **SystemSurrogate** should be set to `PreviewHost` and the **CustomSurrogateExecutable** should not be set.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
