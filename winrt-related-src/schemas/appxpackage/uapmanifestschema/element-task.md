---
description: The background task associated with the app extensibility point (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Task (Windows 10)
ms.assetid: 4662ec1d-c245-4c60-b966-e27d5ce0699d
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Task (Windows 10)

The background task associated with the app extensibility point.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-1-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<BackgroundTasks\>](element-backgroundtasks.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Task\>**

## Syntax

```xml
<Task
  Type = 'A string that can have one of the following values: "general", "audio", "controlChannel", "systemEvent", "timer", "pushNotification", "location", "deviceUse", "deviceServicing", "deviceConnectionChange" or "bluetooth".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The task type. | A string that can have one of the following values: *general*, *audio*, *controlChannel*, *systemEvent*, *timer*, *pushNotification*, *location*, *deviceUse*, *deviceServicing*, *deviceConnectionChange* or *bluetooth*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [BackgroundTasks](element-backgroundtasks.md) | Defines an app extensibility point of type *windows.backgroundTasks*. Background tasks run in a dedicated background host; that is, without a UI. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
