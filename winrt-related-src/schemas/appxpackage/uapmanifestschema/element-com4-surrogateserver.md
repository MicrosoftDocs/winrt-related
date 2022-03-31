---
title: com4:SurrogateServer
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:SurrogateServer



## Description
TBD



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
| CustomSurrogateExecutable | TBD | One of the following values: A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| DisplayName | TBD | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| LaunchAndActivationPermission | TBD | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).| Yes |
| AppId | TBD | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| SystemSurrogate | TBD | "PreviewHost"| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-surrogateserver-class.md) | TBD |
| [InProcessServerClassReference](element-com4-inprocessserverclassreference.md) | TBD |
| [ClassReference](element-com4-surrogateserver-classreference.md) | TBD |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
