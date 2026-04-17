---
title: com4:ProxyStub
description: Registers a proxy stub. (com4:ProxyStub)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:ProxyStub, Extensions, com4:ProxyStub]
---

# com4:ProxyStub

Registers a proxy stub

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ProxyStub>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ProxyStub>`**  

## Syntax

```xml
<com4:ProxyStub
  Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ProcessorArchitecture = 'A string that can have one of the following values: "x86", "x64", "arm", "arm64", or "x86a64".'
  Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' >

  <!-- Child elements -->
  ProxyStubDll

</com4:ProxyStub>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The path relative to the package root. Path must reference a file in the package. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |  |
| **Id** | The proxy stub's CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |  |
| **DisplayName** | A localizable string corresponding to the default value of the proxy stub's CLSID key. | A string between 1 and 256 characters in length. This string is localizable.| Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [ProxyStubDll](element-com4-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

A proxy stub element must have either a Path attribute or one or more ProxyStubDll child elements, but not both.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
