---
title: uap10:DisplayName
description: A friendly name that can be displayed to users.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:DisplayName

A friendly name that can be displayed to users.

## Element Hierarchy

[ <  Package  > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP10:Extension > ](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP10:Extension > ](element-uap10-protocol.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< uap10:DisplayName >**

## Syntax
```syntax
<uap10:DisplayName>
  A string value that must be between 1 and 256 characters in length.

</uap10:DisplayName>
```


## Attributes

None.

## Child Elements

None.

## Parent Elements
| Parent Element | Description |
|---------------|-------------|
| [UAP10:Protocol](element-uap10-protocol.md) | Sets parameters to define the protocol of the extensions. |

## Requirements
|   | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |