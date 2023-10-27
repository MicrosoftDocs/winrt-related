---
title: com4:InProcessHandler
description: Registers an in-process handler with one or many class registrations. (in com4:ComServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessHandler

Registers an in-process handler with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:InProcessHandler\>**

## Syntax

```xml
<com4:InProcessHandler
  Path = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".' >

  <!-- Child elements -->
  Class
  InProcessHandlerDll
  ClassReference

</com4:InProcessHandler>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| Path | The full path to the in-process handler DLL. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`, ending with the case-insensitive file extension `.dll`. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com4-inprocesshandler-class.md) | Defines an in-process handler class registration. |
| [InProcessHandlerDll](element-com4-inprocesshandlerdll.md) | Specifies the path and processor architecture of an in-process handler DLL. |
| [ClassReference](element-com4-inprocesshandler-classreference.md) | Specifies the class with which the registered in-process handler is associated and sets registration details. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

The following example shows how to register a class and an in-process handler dll for x86 and x64 architectures.

```xml
<com4:InProcessHandler> 
  <com4:InProcessHandlerDll Path="x86\MyHandler.dll" ProcessorArchitecture="x86"/> 
  <com4:InProcessHandlerDll Path="amd64\MyHandler.dll" ProcessorArchitecture="x64"/> 
  <com4:Class Id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" DisplayName="CLSID_Bar" ThreadingModel="Both"/> 
</com4:InProcessHandler>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| Minimum OS Version | Windows 10 (Build 20348) |
