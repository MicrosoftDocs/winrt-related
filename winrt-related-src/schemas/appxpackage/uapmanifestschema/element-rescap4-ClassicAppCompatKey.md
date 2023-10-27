---
title: rescap4:ClassicAppCompatKey
description: Registry keys for discovering classic app installations and launching executables.
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap4:ClassicAppCompatKey

Registry keys for discovering classic app installations and launching executables.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap4:Extension\>](element-rescap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap4:ClassicAppCompatKeys\>](element-rescap4-ClassicAppCompatKeys.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap4:ClassicAppCompayKey\>**

## Syntax

```xml
<rescap4:ClassicAppCompatKey
  Name = 'A valid registry path in to one of the following: "HKEY_LOCAL_MACHINE\Sofware", "HKEY_CURRENT_USER\Software", "HKEY_CURRENT_CONFIG\Software", "HKLM\Software", "HKCU\Software", or "HKCC\Software". The path is not case sensitive.'
  ValueName = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  ValueType = 'An optional string that can have one of the following values: "REG_SZ", "REG_BINARY", "REG_DWORD", "REG_QWORD", "REG_MULTI_SZ", or "REG_EXPAND_SZ".'
  Value = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

### Key

`?` optional (zero or one)  

## Attributes and elements

### Attributes

| Attribute | Description | Data Type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the registry path. | A valid registry path in to one of the following: *HKEY_LOCAL_MACHINE\Sofware*, *HKEY_CURRENT_USER\Software*, *HKEY_CURRENT_CONFIG\Software*, *HKLM\Software*, *HKCU\Software*, or *HKCC\Software*. The path is not case sensitive. | Yes |  |
| **ValueName** | Value name of a key in the registry path. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **ValueType** | A value type. | An optional string that can have one of the following values: *REG_SZ*, *REG_BINARY*, *REG_DWORD*, *REG_QWORD*, *REG_MULTI_SZ*, or *REG_EXPAND_SZ*. | No |  |
| **Value** | The value of the ValueName. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [recap4:ClassicAppCompatKeys](element-rescap4-ClassicAppCompatKeys.md) | Contains registry keys for discovering classic app installations and launching executables. |

## Remarks

Locations under "HKEY_LOCAL_MACHINE\Software\Microsoft" are not allowed for the **Name** attribute unless **CompatMode** is set to 'classic'.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
| Minimum OS Version | Windows 10 version 1803 (Build 17134) |
