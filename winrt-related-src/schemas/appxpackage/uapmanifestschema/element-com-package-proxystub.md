---
ms.assetid: 04c01463-ed54-428c-b26a-0fc36310eb67
title: com:ProxyStub
description: Registers a proxy stub (in Package/Extensions).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---


# com:ProxyStub

Registers a proxy stub.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-package-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Interface\>](element-com-package-interface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:ProxyStub\>**

## Syntax

```xml
<ProxyStub
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    DisplayName = 'An optional string with a value between 1 and 256 characters in length. This string is localizable.'
    Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' >

    <!-- Child elements -->
    com2:ProxyStubDll?

</ProxyStub>
```

## Key

`?`    optional (zero or one)  

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The proxy stub's CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| **DisplayName** | A localizable string corresponding to the default value of the proxy stub's CLSID key. | An optional string with a value between 1 and 256 characters in length. | No |
| **Path** | The path relative to the package root. Path must reference a file in the package. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |

### Child elements

| Child element | Description |
|-|-|
| [com2:ProxyStubDll](element-com2-package-proxystubdll.md) | Specifies the path and processor architecture of a ProxyStub DLL. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:ComInterface](element-com-package-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |

## Remarks

Proxy stub registrations correspond to the CLSID registration for the Interface's [ProxyStubClsid32](/windows/win32/com/proxystubclsid32) keys.

A proxy stub element must have either a Path attribute or one or more ProxyStubDll child elements, but not both.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
