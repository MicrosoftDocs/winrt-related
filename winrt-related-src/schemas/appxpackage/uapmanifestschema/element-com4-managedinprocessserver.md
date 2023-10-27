---
title: com4:ManagedInProcessServer
description: Registers a managed in-process server with one or many class registrations. (com4:ManagedInProcessServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ManagedInProcessServer

Registers a managed in-process server with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ManagedInProcessServer\>**

## Syntax

```xml
<com4:ManagedInProcessServer
  Assembly = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  RuntimeVersion = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  Class
  ClassReference

</com4:ManagedInProcessServer>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Assembly** | The name of the assembly for the managed in-process server. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **RuntimeVersion** | The runtime version targeted by the managed in-proces server. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com4-managedinprocessserver-class.md) | Registers a managed in-process server with one or more classes.  |
| [ClassReference](element-com4-managedinprocessserver-classreference.md) | Specifies the class with which the managed in-process server is associated and sets registration details. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
