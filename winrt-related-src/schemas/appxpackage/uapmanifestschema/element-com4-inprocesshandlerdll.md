---
title: com4:InProcessHandlerDll
description: Specifies the path and processor architecture of an in-process handler DLL. (com4:InProcessHandlerDll)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessHandlerDll

Specifies the path and processor architecture of an in-process handler DLL.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessHandler\>](element-com4-inprocesshandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:InProcessHandlerDll\>**

## Syntax

```xml
<com4:InProcessHandlerDll
  Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  ProcessorArchitecture = 'A string that can be one of the following values: "x86", "x64", "arm", "arm64", or "x86a64".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
| -----------| -------------| -----------| ----------|
| **Path** |  The full path to the in-process handler DLL. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`, ending with the case-insensitive file extension `.dll`. | Yes |  |
| **ProcessorArchitecture** | The processor architecture of the in-process handler DLL. | A string that can be one of the following values: *x86* , *x64* , *arm* , *arm64*, or *x86a64*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Examples

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
| **Minimum OS Version** | Windows 10 (Build 20348) |
