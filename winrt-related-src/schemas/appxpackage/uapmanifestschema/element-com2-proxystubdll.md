---
title: com2:ProxyStubDll
description: Specifies the path and processor architecture of a ProxyStub DLL. (com2)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com2:Extension, com2:ComInterface, com2:ProxyStub, com2:ProxyStubDll]
---

# com2:ProxyStubDll

Specifies the path and processor architecture of a ProxyStub DLL.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com2:Extension>`](element-com2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com2:ComInterface>`](element-com2-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com2:ProxyStub>`](element-com2-proxystubdll.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com2:ProxyStubDll>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com2:Extension>`](element-com2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com2:ComInterface>`](element-com2-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com2:ProxyStub>`](element-com2-proxystubdll.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com2:ProxyStubDll>`**  


## Syntax

```xml
<com2:ProxyStubDll
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ProcessorArchitecture = 'A required string that can have one of the following values: "x86", "x64", "arm", "arm64", or "x86a64".' />
```


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**Path**| A relative path to the .dll file in the app package. |A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *.|Yes||
|**ProcessorArchitecture**| The processor architecture of the ProxyStub registration. |A string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *x86a64*.|Yes||

## Child elements

None.


## Parent elements

| Parent element | Description |
|-|-|
| [com:ProxyStub](element-com-proxystub.md) | Registers a proxy stub. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
