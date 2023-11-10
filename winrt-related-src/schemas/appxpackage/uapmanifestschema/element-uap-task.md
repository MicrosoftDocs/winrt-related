---
description: The background task associated with the app extensibility point (Windows 10; uap:Task).
Search.Product: eADQiWindows 10XVcnh
title: uap:Task (Windows 10)
ms.assetid: 2e4fce9f-4db8-48e7-ab0e-03cf08f6342f
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:Task (Windows 10)

The background task associated with the app extensibility point.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-1-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<BackgroundTasks\>](element-backgroundtasks.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:Task\>**

## Syntax

```xml
<uap:Task
  Type = 'A string that can have one of the following values: "chatMessageNotification", "vpnClient", "phoneCall", or "mediaProcessing".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The type of the task. | A string that can have one of the following values: *chatMessageNotification*, *vpnClient*, *phoneCall*, or *mediaProcessing*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [BackgroundTasks](element-backgroundtasks.md) | Defines an app extensibility point of type *windows.backgroundTasks*. Background tasks run in a dedicated background host; that is, without a UI. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
