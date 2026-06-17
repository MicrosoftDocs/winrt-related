---
title: com4:ClassReference (in SurrogateServer)
description: Specifies the class with which the registered in-process server is associated and sets registration details. (in com4:SurrogateServer)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com4:SurrogateServer, com4:ClassReference]
---

# com4:ClassReference (in SurrogateServer)

Specifies the class with which the registered in-process server is associated and sets registration details.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:SurrogateServer>`](element-com4-surrogateserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ClassReference>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:SurrogateServer>`](element-com4-surrogateserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ClassReference>`**

## Syntax

```xml
<com4:ClassReference
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ThreadingModel = 'A required string that can have one of the following values: "Both", "STA", "MTA", "MainSTA", or "Neutral".'
  EnableOleDefaultHandler = 'An optional boolean value.'
  Id = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The path to the surrogate server DLL. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
| **ThreadingModel** | The threading model for loading DLLs. | A string that can have one of the following values: *Both*, *STA*, *MTA*, *MainSTA*, *Neutral*. | Yes |  |
| **EnableOleDefaultHandler** | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | An optional boolean value. | No |  |
| **Id** | The Id of the [Class](element-com4-exeserver-class.md) being referenced. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [com4:SurrogateServer](element-com4-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
