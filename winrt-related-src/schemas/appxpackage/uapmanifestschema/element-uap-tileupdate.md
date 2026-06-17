---
title: uap:TileUpdate
description: Describes how the app tile receives update notifications (in Package/Applications).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:VisualElements, uap:DefaultTile, uap:TileUpdate]
---

# uap:TileUpdate

Describes how the app tile receives update notifications.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:VisualElements>`](element-uap-visualelements.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:DefaultTile>`](element-uap-defaulttile.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:TileUpdate>`**  

## Syntax

```xml
<uap:TileUpdate
  Recurrence = 'A required string that can have one of the following values: "halfHour", "hour", "sixHours", "twelveHours", or "daily".'
  UriTemplate = 'A required string between 1 and 2084 characters in length in the form of a valid URI.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Recurrence** | The recurrence interval for tile update notifications. | A string that can have one of the following values: *halfHour*, *hour*, *sixHours*, *twelveHours*, *daily*. | Yes |  |
| **UriTemplate** | The URI template for tile update notifications. | A string between 1 and 2084 characters in length in the form of a valid URI. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:DefaultTile](element-uap-defaulttile.md) | The default tile that represents your app on the Start screen. The icons specified here are displayed when your app is not showing tile notifications. To dynamically change the appearance of your tile and display relevant live content, see [Send a local tile notification](/windows/uwp/controls-and-patterns/tiles-and-notifications-sending-a-local-tile-notification). |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

The **UriTemplate** attribute must be a value URI per RFC 3986. It must be an absolute URI with only [schemes](/windows/uwp/launch-resume/launch-maps-app) of unsecure `http:` sites and secure "https:" sites permitted.

## Examples

<!-- Author content goes here -->
