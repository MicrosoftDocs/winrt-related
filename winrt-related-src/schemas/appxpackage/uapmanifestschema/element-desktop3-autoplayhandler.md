---
title: desktop3:AutoPlayHandler
description: Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:AutoPlayHandler

Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop3:AutoPlayHandler\>**

## Syntax

```xml
<desktop3:AutoPlayHandler>

    desktop3:InvokeAction{0,1000}

</desktop3:AutoPlayHandler>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop3:InvokeAction](element-desktop3-invokeaction.md) | Contains content and device information for invoking an AutoPlay action. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop3:Extension](element-desktop3-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
