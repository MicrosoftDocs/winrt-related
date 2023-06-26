---
title: com5:InProcessHandler
description: Registers an in-process handler with one or many class registrations. (in com5:ComServer)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com5:InProcessHandler



## Description

Registers an in-process handler with one or many class registrations.



## Element Hierarchy
[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp; [\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com4:Extension\>](element-com4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com4:ComServer\>](element-com4-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:InProcessHandler&gt;**


## Syntax

```syntax
<com5:InProcessHandler     Path? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
>
<!-- Child elements -->
  Class
  InProcessHandlerDll
  ClassReference
</com5:InProcessHandler>
```

## Key

`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The full path to the in-process handler DLL. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com5-inprocesshandler-class.md) | Defines an in-process handler class registration. |
| [InProcessHandlerDll](element-com5-inprocesshandlerdll.md) | Specifies the path and processor architecture of an in-process handler DLL. |
| [ClassReference](element-com5-inprocesshandler-classreference.md) | Specifies the class with which the registered in-process handler is associated and sets registration details. |

## Remarks

This element is identical to [com5:InProcessHandler](element-com4-inprocesshandler.md) except that the child **Class** element can specify a [TypeLib](element-com5-typelib.md).

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com5 | http://schemas.microsoft.com/appx/manifest/com/windows10/5 |
