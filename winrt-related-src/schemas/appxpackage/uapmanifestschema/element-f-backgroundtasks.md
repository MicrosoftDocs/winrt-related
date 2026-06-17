---
title: BackgroundTasks
description: Defines an app extensibility point of type windows.backgroundTasks (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, Extension, BackgroundTasks]
---

# BackgroundTasks

Defines an app extensibility point of type **windows.backgroundTasks**. Background tasks run in a dedicated background host; that is, without a UI.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<BackgroundTasks>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<BackgroundTasks>`**

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <BackgroundTasks
    ServerName = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
    uap4:SupportsMultipleInstances = 'An optional boolean value.' >

    <!-- Child elements -->
    BackgroundTaskChoice{0,17}

  </BackgroundTasks>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServerName** | The server name. Ensures that only one instance of the server exists at runtime. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap4:SupportsMultipleInstances** | Supports multiple, separate instances of background tasks. | An optional boolean value. | No |  |

## Child elements

| Child element | Description |
|-|-|

## Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-f-package-extension.md) | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap4** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

Extensions of type **windows.backgroundTask** must specify either a StartPage or EntryPoint attribute in the Extension element. For more info (and an example) see [Declare background tasks in the application manifest](/windows/uwp/launch-resume/declare-background-tasks-in-the-application-manifest).

## Examples

<!-- Author content goes here -->
