---
description: A friendly description that can be displayed to users (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Description (Windows 10)
ms.assetid: e113111a-1d9b-4d04-bd86-86beece204dd
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

A friendly description that can be displayed to users.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Description\>**

## Syntax

```xml
<Description>
  A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.
</Description>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Remarks

This string is localizable.

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
