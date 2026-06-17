---
title: com4:InProcessHandler
description: Registers an in-process handler with one or many class registrations. (in com4:ComServer)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com4:InProcessHandler]
---

# com4:InProcessHandler

Registers an in-process handler with one or many class registrations.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:InProcessHandler>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:InProcessHandler>`**

## Syntax

```xml
<com4:InProcessHandler
  Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".' >

  <!-- Child elements -->
  com4:Class{0,4000}
  com4:InProcessHandlerDll{0,4000}
  com4:ClassReference{0,4000}

</com4:InProcessHandler>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The full path to the in-process handler DLL. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com4:Class](element-com4-inprocesshandler-class.md) | Defines an in-process handler class registration. |
| [com4:InProcessHandlerDll](element-com4-inprocesshandlerdll.md) | Specifies the path and processor architecture of an in-process handler DLL. |
| [com4:ClassReference](element-com4-inprocesshandler-classreference.md) | Specifies the class with which the registered in-process handler is associated and sets registration details. |

## Parent elements

| Parent element | Description |
|-|-|
| [com4:ComServer](element-com4-comserver.md) | Declares a package extension point of type windows.comServer. The comServer extension may include class registrations, including activation details for the servers that implement these classes, and ProgId and TreatAsClass registrations, which provide additional identifiers used to reference these classes at runtime. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

The following example shows how to register a class and an in-process handler dll for x86 and x64 architectures.

```xml
<com4:InProcessHandler> 
  <com4:InProcessHandlerDll Path="x86\MyHandler.dll" ProcessorArchitecture="x86"/> 
  <com4:InProcessHandlerDll Path="amd64\MyHandler.dll" ProcessorArchitecture="x64"/> 
  <com4:Class Id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" DisplayName="CLSID_Bar" ThreadingModel="Both"/> 
</com4:InProcessHandler>
```

## Examples

<!-- Author content goes here -->
