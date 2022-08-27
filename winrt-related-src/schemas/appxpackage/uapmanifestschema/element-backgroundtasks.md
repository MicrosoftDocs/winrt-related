---
description: Defines an app extensibility point of type windows.backgroundTasks (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: BackgroundTasks (Windows 10)
ms.assetid: 0e9cbbc5-3852-4158-87e7-12ea87be62e7
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# BackgroundTasks (Windows 10)

Defines an app extensibility point of type **windows.backgroundTasks**. Background tasks run in a dedicated background host; that is, without a UI.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-1-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<BackgroundTasks\>**

## Syntax

```xml
<BackgroundTasks 
  ServerName = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap4:SupportsMultipleInstances = 'A boolean value.' >

  <!-- Child elements -->
  Task{1,17},
  uap:Task{1,17}

</BackgroundTasks>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| ServerName | The server name. Ensures that only one instance of the server exists at runtime. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| uap4:SupportsMultipleInstances | Supports multiple, separate instances of background tasks. | A boolean value. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Task](element-task.md) | The background task associated with the app extensibility point. |
| [uap:Task](element-uap-task.md) | The background task associated with the app extensibility point. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extension *(global)*](element-1-extension.md) | Declares an extensibility point for the package. |

## Remarks

Extensions of type "windows.backgroundTask" must specify either a StartPage or EntryPoint attribute in the Extension element. For more info (and an example) see [Declare background tasks in the application manifest](/windows/uwp/launch-resume/declare-background-tasks-in-the-application-manifest).

## Requirements

|   |  Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
