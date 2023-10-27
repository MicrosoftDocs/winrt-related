---
description: Describes how the app tile receives update notifications (in Package/Applications).
Search.Product: eADQiWindows 10XVcnh
title: uap:TileUpdate (Windows 10)
ms.assetid: cf529081-b711-4c35-b50c-da0f95ebf3c1
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:TileUpdate (Windows 10)

Describes how the app tile receives update notifications.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:DefaultTitle\>](element-uap-defaulttile.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:TileUpdate\>**

## Syntax

```xml
<uap:TileUpdate
  Recurrence = 'A string that can have one of the following values: "halfHour", "hour", "sixHours", "twelveHours", or "daily".'
  UriTemplate = 'A string with a value between 1 and 2084 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Recurrence** | The recurrence interval for tile update notifications. | A string that can have one of the following values: *halfHour*, *hour*, *sixHours*, *twelveHours*, or *daily*. | Yes |  |
| **UriTemplate** | The URI template for tile update notifications. | A string between 1 and 2084 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:DefaultTile](element-uap-defaulttile.md) | The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default. |

## Remarks

The **UriTemplate** attribute must be a value URI per RFC 3986. It must be an absolute URI with only [schemes](/windows/uwp/launch-resume/launch-maps-app) of unsecure `http:` sites and secure "https:" sites permitted.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
