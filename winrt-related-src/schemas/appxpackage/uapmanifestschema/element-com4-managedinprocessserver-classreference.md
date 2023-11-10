---
title: com4:ClassReference (in ManagedInProcessServer)
description: Specifies the class with which the managed in-process server is associated and sets registration details. (in com4:ManagedInProcessServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ClassReference (in ManagedInProcessServer)

Specifies the class with which the managed in-process server is associated and sets registration details.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:ManagedInProcessServer\>](element-com4-managedinprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ClassReference\>**

## Syntax

```xml
<com4:ClassReference
    ThreadingModel = 'A string with that can have one of the following values: "Both", "STA", "MTA", "MainSTA", or "Neutral".'
    ImplementationClass = 'An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1).'
    Virtualization = 'A string with that can have one of the following values: "enabled" or "disabled".'
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
></com4:ClassReference>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ThreadingModel** | A string with that can have one of the following values: *Both*, *STA*, *MTA*, *MainSTA*, or *Neutral*. | Yes |  |
| **ImplementationClass** | The implementation class associated with the class reference. | An alphanumeric string, separated by a period, with a value between 1 and 255 characters in length (for example, Foo.Bar or Foo.Bar.1). | Yes |  |
| **Virtualization** | Specifies whether virtualization is used when loading the class. | A string with that can have one of the following values: *enabled* or *disabled* | Yes |  |
| **Id** | The Id of the [Class](element-com4-class.md) being referenced. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:ManagedInProcessServer](element-com4-managedinprocessserver.md) | Registers a managed in-process server with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
