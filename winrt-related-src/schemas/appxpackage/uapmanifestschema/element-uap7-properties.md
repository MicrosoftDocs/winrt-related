---
description: Properties of an application.
title: uap7:Properties
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/03/2018
---

# uap7:Properties

Properties of an application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap7:Properties\>**

## Syntax

```xml
<uap7:Properties>

  <!-- Child elements -->
  uap7:ImportRedirectionTable

</uap7:Properties>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap7:ImportRedirectionTable](element-uap7-importredirectiontable.md) | Allows for a packaged app to declare API redirections.|

### Parent elements

| Parent element | Description |
|-|-|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
