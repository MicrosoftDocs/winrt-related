---
title: com4:InProcessHandler
description: Registers an in-process handler with one or many class registrations. (in com4:ComServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessHandler



## Description
Registers an in-process handler with one or many class registrations.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:InProcessHandler&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:InProcessHandler     Path? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".
>
<!-- Child elements -->
  Class
  InProcessHandlerDll
  ClassReference
</com4:InProcessHandler>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The full path to the in-process handler DLL. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *, ending with the case-insensitive file extension ".dll".| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-inprocesshandler-class.md) | Defines an in-process handler class registration.  |
| [InProcessHandlerDll](element-com4-inprocesshandlerdll.md) | Specifies the path and processor architecture of an in-process handler DLL. |
| [ClassReference](element-com4-inprocesshandler-classreference.md) | Specifies the class with which the registered in-process handler is associated and sets registration details. |

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
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
