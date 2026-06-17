---
title: rescap4:ClassicAppCompatKey
description: Registry keys for discovering classic app installations and launching executables.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, rescap4:Extension, rescap4:ClassicAppCompatKeys, rescap4:ClassicAppCompatKey]
---

# rescap4:ClassicAppCompatKey

Registry keys for discovering classic app installations and launching executables.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:Extension>`](element-rescap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:ClassicAppCompatKeys>`](element-rescap4-classicappcompatkeys.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap4:ClassicAppCompatKey>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:Extension>`](element-rescap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:ClassicAppCompatKeys>`](element-rescap4-classicappcompatkeys.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap4:ClassicAppCompatKey>`**  

## Syntax

```xml
<rescap4:ClassicAppCompatKey
  Name = 'A required string between 1 and 2048 characters in length.'
  ValueName = 'An optional string value.'
  ValueType = 'An optional string that can have one of the following values: "REG_SZ", "REG_BINARY", "REG_DWORD", "REG_QWORD", "REG_MULTI_SZ", or "REG_EXPAND_SZ".'
  Value = 'An optional string value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the registry path. | A string between 1 and 2048 characters in length. | Yes |  |
| **ValueName** | Value name of a key in the registry path. | An optional string value. | No |  |
| **ValueType** | A value type. | An optional string that can have one of the following values: *REG_SZ*, *REG_BINARY*, *REG_DWORD*, *REG_QWORD*, *REG_MULTI_SZ*, *REG_EXPAND_SZ*. | No |  |
| **Value** | The value of the ValueName. | An optional string value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [rescap4:ClassicAppCompatKeys](element-rescap4-classicappcompatkeys.md) | Contains registry keys for discovering classic app installations and launching executables. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

Locations under "HKEY_LOCAL_MACHINE\Software\Microsoft" are not allowed for the **Name** attribute unless **CompatMode** is set to 'classic'.

## Examples

<!-- Author content goes here -->
