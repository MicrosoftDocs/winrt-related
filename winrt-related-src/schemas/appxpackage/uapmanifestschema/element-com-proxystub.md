---
title: com:ProxyStub
description: Registers a proxy stub. 
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com:Extension, com:ComInterface, com:ProxyStub]
---

# com:ProxyStub

Registers a proxy stub.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:ProxyStub>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com:ComInterface>`](element-com-cominterface.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com:ProxyStub>`**  


## Syntax

```xml
<com:ProxyStub
  Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  Id = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  com:ProxyStubDll{0,4}

</com:ProxyStub>
```

### Key

`{}` specific range of occurrences


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**Path**| The path relative to the package root. Path must reference a file in the package. |An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *.|No||
|**Id**| The proxy stub's CLSID. |A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|Yes||
|**DisplayName**| A localizable string corresponding to the default value of the proxy stub's CLSID key. |An optional string between 1 and 256 characters in length. This string is localizable.|No||

## Child elements
| Child element | Description |
|-|-|
| [com2:ProxyStubDll](element-com2-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |

## Parent elements

| Parent element | Description |
|-|-|
| [com:ComInterface](element-com-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

Proxy stub registrations correspond to the CLSID registration for the Interface's [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) keys.

A proxy stub element must have either a **Path** attribute or one or more **ProxyStubDll** child elements, but not both.

## Examples

<!-- Author content goes here -->
