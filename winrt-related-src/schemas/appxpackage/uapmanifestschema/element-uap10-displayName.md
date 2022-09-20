---
title: uap10:DisplayName
description: A friendly name that can be displayed to users.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:DisplayName

A friendly name that can be displayed to users.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\< UAP10:Extension\>](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:Protocol\>](element-uap10-protocol.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**<\uap10:DisplayName\>**

## Syntax

```xml
<uap10:DisplayName>
  A string with a value between 1 and 256 characters in length.
</uap10:DisplayName>
```

## Attributes and elements

### Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap10:Protocol](element-uap10-protocol.md) | Sets parameters to define the protocol of the extensions. |

## Requirements

| Item | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
