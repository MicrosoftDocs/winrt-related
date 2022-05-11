---
title: com4:SurrogateServer
description: Registers a SurrogateServer with one or many class registrations. (com4:SurrogateServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:SurrogateServer



## Description
Registers a SurrogateServer with one or many class registrations.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:SurrogateServer&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:SurrogateServer     CustomSurrogateExecutable = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    LaunchAndActivationPermission = [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).
    AppId = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    SystemSurrogate = "PreviewHost"
>
<!-- Child elements -->
  Class
  InProcessServerClassReference
  ClassReference
</com4:SurrogateServer>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| CustomSurrogateExecutable |  A path to the DllSurrogate in the AppId key. This path is relative to the package root and must reference a file in the package. This is mututally exclusive with SystemSurrogate. | One of the following values: A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| DisplayName | DisplayName is a localizable string corresponding to the default AppID key value. | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| LaunchAndActivationPermission | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).| Yes |
| AppId | The AppId that references the associated AppId key.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| SystemSurrogate | A value that corresponds to well-known values from the DllSurrogate value of the AppId key. This is mututally exclusive with CustomSurrogateExecutable. | "PreviewHost"| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-surrogateserver-class.md) | Defines a surrogate server class registration. |
| [InProcessServerClassReference](element-com4-inprocessserverclassreference.md) | Specifies the class with which the managed in-process server is associated and sets registration details. |
| [ClassReference](element-com4-surrogateserver-classreference.md) | Specifies the class with which the registered in-process server is associated and sets registration details. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
