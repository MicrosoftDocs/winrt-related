---
title: com4:ServiceServer
description: Registers a ServiceServer with one or many class registrations. (com4:ServiceServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ServiceServer



## Description
Registers a ServiceServer with one or many class registrations.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:ServiceServer&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:ServiceServer     ServiceName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    Arguments = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    LaunchAndActivationPermission = [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).
>
<!-- Child elements -->
  Class
  ClassReference
</com4:ServiceServer>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| ServiceName | The name of the Windows service that hosts the COM server.  | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| Arguments | The command-line parameters of the service. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| DisplayName | A localizable string corresponding to the default AppID key value. | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| LaunchAndActivationPermission | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-exeserver-class.md) | Defines an ExeServer class registration. |
| [ClassReference](element-com4-exeserver-classreference.md) | Specifies the class with which the registered ExeServer is associated and sets ExeServer-specific registration details. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
